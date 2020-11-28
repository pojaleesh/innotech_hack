#Aho-Corasik

import sys

sys.setrecursionlimit(1500)

sz = 1

class node:
    
    def __init__(self):
    
        self.next_ = {}
        self.go_ = {}
        self.prevNode = -1
        self.prevLetter = 0
        self.link = -1
        self.shortLink = -1
        self.isLeaf = False
        self.num = 0

    
Tree = []
Tree.append(node())
Tree[0].prevNode = 0


def add_string(new_string, num):
    global sz
    v = 0
    for letter in new_string:
        if letter not in Tree[v].next_:
            Tree.append(node())
            Tree[sz].prevNode = v
            Tree[sz].prevLetter = letter
            Tree[v].next_[letter] = sz
            sz += 1
        v = Tree[v].next_[letter]
    Tree[v].isLeaf = True
    Tree[v].num = num
    

def is_have_string(string):
    global sz
    v = 0
    for letter in string:
        if letter not in Tree[v].next_:
            return False
        v = Tree[v].next_[letter]
    if Tree[v].isLeaf:
        return True
    else:
        return False

    
def go(vertex, ch):
    pass


def get_link(vertex):
    if Tree[vertex].link == -1:
        if vertex == 0 or Tree[vertex].prevNode == 0:
            Tree[vertex].link = 0
        else:
            Tree[vertex].link = go(get_link(Tree[vertex].prevNode), Tree[vertex].prevLetter)
    return Tree[vertex].link


def go(vertex, ch):
    if ch not in Tree[vertex].go_:
        if ch in Tree[vertex].next_:
            Tree[vertex].go_[ch] = Tree[vertex].next_[ch]
        else:
            if vertex == 0:
                Tree[vertex].go_[ch] = 0
            else:
                Tree[vertex].go_[ch] = go(get_link(vertex), ch)
    return Tree[vertex].go_[ch]


def get_short_link(vertex):
    if Tree[vertex].shortLink == -1:
        tempVertex = get_link(vertex)
        if tempVertex == 0:
            Tree[vertex].shortLink = 0
        else:
            if Tree[tempVertex].isLeaf:
                Tree[vertex].shortLink = tempVertex
            else:
                Tree[vertex].shortLink = get_short_link(tempVertex)
    return Tree[vertex].shortLink


def check(vertex, number_occurrences):
    while vertex != 0:
        if Tree[vertex].isLeaf:
            if Tree[vertex].num not in number_occurrences:
                number_occurrences[Tree[vertex].num] = 1
            else:
                number_occurrences[Tree[vertex].num] += 1
        vertex = get_short_link(vertex)
    
        
def find_entry(string):
    number_occurrences = {}
    vertex = 0
    for letter in string:
        vertex = go(vertex, letter)
        check(vertex, number_occurrences)
    return number_occurrences