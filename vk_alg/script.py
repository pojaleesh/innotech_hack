# %%

import pickle
import coras
import ParsFromVK
import pymorphy2
import string
import ParsFromVK
import requests
import math


def get_normal_form(word, morth=pymorphy2.MorphAnalyzer()):  # Нормальная форма слова

    return morth.parse(word)[0].normal_form


def delete_punctuation(word):  # Удаление всех знаков пунктуации

    tt = str.maketrans(dict.fromkeys(string.punctuation))

    return word.translate(tt)


file_1 = open('../vk_alg/data1', 'rb')
res = pickle.load(file_1)
vertex_edges = res[0]
count_occ = res[1]
sum_cnt = res[2]
professions = {'Агроном', 'Бухгалтер', 'Грузчик', 'Менеджер', 'Облицовщик', 'Пожарный', 'Учитель'}
cities = {'Москва', 'Санкт-Петербург', 'Санкт Петербург', 'Moscow', 'Saint-Petersburg',
          'Saint Petersburg' 'Екатеринбург', 'Московская область'}
salary = {}
# Несколько средних зарплат по России
salary['Агроном+Москва'] = 74196
salary['Агроном+Moscow'] = 74196
salary['Агроном+Санкт-Петербург'] = 64779
salary['Агроном+Санкт Петербург'] = 64779
salary['Агроном+Екатеринбург'] = 50307
salary['Агроном+Saint-Petersburg'] = 64779
salary['Агроном+Saint Petersburg'] = 64779
salary['Агроном+Московская область'] = 54323
salary['Агроном'] = 38080

salary['Бухгалтер'] = 39857
salary['Бухгалтер+Московская область'] = 49245
salary['Бухгалтер+Москва'] = 54048
salary['Бухгалтер+Moscow'] = 54048
salary['Бухгалтер+Санкт-Петербург'] = 43595
salary['Бухгалтер+Санкт Петербург'] = 43595
salary['Бухгалтер+Екатеринбург'] = 35435
salary['Бухгалтер+Saint-Petersburg'] = 43595
salary['Бухгалтер+Saint Petersburg'] = 43595

salary['Грузчик'] = 34500
salary['Грузчик+Московская область'] = 43976
salary['Грузчик+Москва'] = 47312
salary['Грузчик+Moscow'] = 47312
salary['Грузчик+Санкт-Петербург'] = 34306
salary['Грузчик+Санкт Петербург'] = 34306
salary['Грузчик+Екатеринбург'] = 30726
salary['Грузчик+Saint-Petersburg'] = 34306
salary['Грузчик+Saint Petersburg'] = 34306

salary['Менеджер'] = 35868
salary['Менеджер+Московская область'] = 54220
salary['Менеджер+Москва'] = 62158
salary['Менеджер+Moscow'] = 62158
salary['Менеджер+Санкт-Петербург'] = 49771
salary['Менеджер+Санкт Петербург'] = 49771
salary['Менеджер+Екатеринбург'] = 45445
salary['Менеджер+Saint-Petersburg'] = 49771
salary['Менеджер+Saint Petersburg'] = 49771

salary['Облицовщик'] = 53619
salary['Облицовщик+Московская область'] = 55663
salary['Облицовщик+Москва'] = 49936
salary['Облицовщик+Moscow'] = 49936
salary['Облицовщик+Санкт-Петербург'] = 59411
salary['Облицовщик+Санкт Петербург'] = 59411
salary['Облицовщик+Екатеринбург'] = 60068
salary['Облицовщик+Saint-Petersburg'] = 59411
salary['Облицовщик+Saint Petersburg'] = 59411

salary['Пожарный'] = 36571
salary['Пожарный+Московская область'] = 43158
salary['Пожарный+Москва'] = 50840
salary['Пожарный+Moscow'] = 50840
salary['Пожарный+Санкт-Петербург'] = 38085
salary['Пожарный+Санкт Петербург'] = 38085
salary['Пожарный+Екатеринбург'] = 45474
salary['Пожарный+Saint-Petersburg'] = 38085
salary['Пожарный+Saint Petersburg'] = 38085

salary['Учитель'] = 40101
salary['Учитель+Московская область'] = 45132
salary['Учитель+Москва'] = 61910
salary['Учитель+Moscow'] = 61910
salary['Учитель+Санкт-Петербург'] = 35360
salary['Учитель+Санкт Петербург'] = 35360
salary['Учитель+Екатеринбург'] = 25757
salary['Учитель+Saint-Petersburg'] = 35360
salary['Учитель+Saint Petersburg'] = 35360

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
    city = ''
    if 'city' in main_information:
        probably_city = main_information['city']['title']
        if probably_city in cities:
            city = probably_city
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
                score[j[0]] += (curCnt / words_count) * ((math.log2(len(count_occ[key]) * 10) / sum_cnt))
    maxVal = -100
    ans = ''
    for key in score:
        if score[key] > maxVal:
            maxVal = score[key]
            ans = key
    first_name = main_information['first_name']
    last_name = ''
    if 'last_name' in main_information:
        last_name = main_information['last_name']
    if city == '':
        return ans, city, salary[ans], first_name, last_name
    else:
        return ans, city, salary[ans + '+' + city], first_name, last_name

if __name__ == "__main__":
    cur_id = 'vladimir_pugach'
    print(get_profession(cur_id))
