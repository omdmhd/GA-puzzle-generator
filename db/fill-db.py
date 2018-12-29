#!/usr/bin/env python3
from database import Db
db = Db()
#db.execute('CREATE TABLE words(name VARCHAR(200) PRIMARY KEY) ;')

f = open("import/Farsi to English Advanced.dict", "r")
array = f.readlines()

def just_pick_persian_chars(sentence):
    allowed = ['ا', 'آ', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 
                   'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق',         
                   ' ', 'ی', 'ه', 'و', 'ن', 'م', 'ل', 'گ', 'ک',         
     ]
    text = ''
    for c in sentence:
        if c in allowed:
            text += c
    return text

def check_word_exists(word):
    global db
    count = db.execute_and_fetch("SELECT COUNT(*) as count FROM words WHERE name = ?",  (word, ), 'o' )
    if int(count[0]) >= 1:
        return True
    return False

for line in array:
    line = just_pick_persian_chars(line)
    words = line.split(" ")
    for word in words:
        if len(word) > 2:
            if not check_word_exists(word):
                db.execute("INSERT INTO words(name) values(?) ", (word, ))

