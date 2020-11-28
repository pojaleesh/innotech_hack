import pickle
import coras
import pymorphy2
import string
import ParsFromVK
import requests
import math

def get_normal_form(word, morth=pymorphy2.MorphAnalyzer()): # Нормальная форма слова

    return morth.parse(word)[0].normal_form


def delete_punctuation(word): # Удаление всех знаков пунктуации

    tt = str.maketrans(dict.fromkeys(string.punctuation))

    return word.translate(tt)

file_1 = open('data1', 'rb')
res = pickle.load(file_1)
vertex_edges = res[0]
count_occ = res[1]
sum_cnt = res[2]
professions = {'Агроном', 'Бухгалтер', 'Грузчик', 'Менеджер', 'Облицовщик', 'Пожарный', 'Учитель'}


Tree = []
Tree.append(coras.node())
Tree[0].prevNode = 0

cnt = {}
a = set()

for key in vertex_edges:
    if key in professions:
        cnt[key] = 0
        for j in vertex_edges[key]:
            cnt[key] += j[1]
    else:
        a.add(key)

numb = []

for word in a:
    coras.add_string(word, len(numb))
    numb.append(word)

def get_profession(cur_id):
    main_information, groups = ParsFromVK.pars_from_vk(cur_id)
    score = {}
    for prof in professions:
        score[prof] = 0
    s1 = ''
    s2 = ''
    words_count = 0
    word_count = {}
    for group in groups:
        words = group.split()
        for word in words:
            word = delete_punctuation(word)
            word = get_normal_form(word)
            s1 += word
            words_count += 1
    for key in main_information:
        words = str(main_information[key]).split()
        for word in words:
            word = delete_punctuation(word)
            word = get_normal_form(word)
            s2 += word
            words_count += 1
    number_occurrences = coras.find_entry(s1)
    for key in number_occurrences:
        curOccur = numb[key]
        if curOccur not in word_count:
            word_count[curOccur] = 1
        else:
            word_count[curOccur] += 1
    number_occurrences = coras.find_entry(s2)
    for key in number_occurrences:
        curOccur = numb[key]
        if curOccur not in word_count:
            word_count[curOccur] = 1
        else:
            word_count[curOccur] += 1
    for key in word_count:
        curOccur = key
        curCnt = word_count[key]
        for j in vertex_edges[curOccur]:
            if j[0] in professions:
                score[j[0]] += (curCnt / words_count) * ((math.log2(len(count_occ[key] ) * 10) / sum_cnt))
    maxVal = -100
    ans = ''
    for key in score:
        if score[key] > maxVal:
            maxVal = score[key]
            ans = key
    return ans

if __name__ == "__main__":
    cur_id = 'vladimir_pugach'
    print(get_profession(cur_id))
