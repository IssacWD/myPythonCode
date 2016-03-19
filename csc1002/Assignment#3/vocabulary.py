# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 15.10
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/3/19
# ********************************************************
import re
import threading
import logging
import os
import sys
import sqlite3
import webbrowser
import socket

logging.basicConfig(level=logging.WARNING,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='vocabulary.log',
                filemode='w')

WORD = re.compile(r'^[A-Z]+$')
SYNONYM = re.compile(r'Synonym')
ANTONYM = re.compile(r'Antonym')

def _init_DB(DB_file_name):
    existed = False
    if DB_file_name in os.listdir('.'):
        existed = True
    db = sqlite3.connect(DB_file_name, check_same_thread=False)
    curs = db.cursor()
    SQL_create_wordList = 'create table word(' \
                          'word varchar(255),' \
                          'mean varchar(255),' \
                          'eg varchar(255),' \
                          'synonym varchar(255),' \
                          'antonym varchar(255));'
    if not existed:
        try:
            curs.execute(SQL_create_wordList)
            db.commit()
        except sqlite3.OperationalError:
            logging.warning(DB_file_name + 'Error when create table')
    return db, curs

def insert_word(list_every_word):
    try:
        SQl_insert = 'insert into word (word,mean,eg,synonym,antonym) values (?,?,?,?,?);'
        word_cursor.execute(SQl_insert, (list_every_word[0], list_every_word[1], list_every_word[2], list_every_word[3], list_every_word[4]))
    except sqlite3.OperationalError:
        logging.warning('Error when insert word %s' % list_every_word[0])

def generate_words_DB(file_name):
    file_obj = open(file_name, 'r').readlines()
    buffer_word = None
    buffer_list = ['', '', None, None, None]
    for line in file_obj:
        line = line.strip()
        title, content = line.split(':')
        if WORD.match(title):
            if buffer_word == None:
                buffer_word = title
            elif buffer_word != title:
                insert_word(buffer_list)
            buffer_word = title ; buffer_list[0] = title
            if len(content.split(' - ')) != 2:
                buffer_list[1] = content
            else:
                buffer_list[1], buffer_list[2] = content.split(' - ')
        elif SYNONYM.match(title):
            buffer_list[3] = content.strip()
        elif ANTONYM.match(title):
            buffer_list[4] = content.strip()
    insert_word(buffer_list)


if __name__ == '__main__':
    DB_file, word_cursor = _init_DB('test.db')
    generate_words_DB('TOEFL.txt')
    DB_file.commit()












