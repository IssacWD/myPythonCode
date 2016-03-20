# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 15.10
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/3/19
# ********************************************************
import re
import logging
import os
import sys
import sqlite3
import webbrowser

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='Vocabulary.log',
                    filemode='w')

ARGVs = sys.argv
WORD = re.compile(r'^[A-Z]+$')
SYNONYM = re.compile(r'Synonym')
ANTONYM = re.compile(r'Antonym')

def init_DB(DB_file_name):
    existed = False
    if DB_file_name in os.listdir('.'):
        existed = True
    db = sqlite3.connect(DB_file_name, check_same_thread=False)
    db.row_factory = sqlite3.Row
    curs = db.cursor()
    SQL_create_wordList = 'create table wordTable(word varchar(255),rword varchar(255),mean varchar(255),eg varchar(255),synonym varchar(255),antonym varchar(255));'
    if not existed:
        try:
            curs.execute(SQL_create_wordList)
            db.commit()
            logging.critical('Success when create table wordTable')
        except sqlite3.OperationalError:
            logging.warning(DB_file_name + 'Error when create table')
            raise sqlite3.OperationalError('Error when create table')
    return db, curs


def _insert_word(list_every_word):
    try:
        SQl_insert = 'insert into wordTable (word,rword,mean,eg,synonym,antonym) values (?,?,?,?,?,?);'
        cursor_obj.execute(SQl_insert, (list_every_word[0], list_every_word[1], list_every_word[2], list_every_word[3], list_every_word[4], list_every_word[5]))
        logging.critical('Success when insert word \'%s\'' % list_every_word[0])
    except sqlite3.OperationalError:
        logging.critical('Error when insert word \'%s\' ' % list_every_word[0])
        logging.critical('R   %s' % list_every_word[1])


def _select_word(cursor_obj, reverse_order):
    SQL_select = 'select * from wordTable order by word' if not reverse_order else 'select * from wordTable order by rword'
    try:
        select_cursor = cursor_obj.execute(SQL_select)
    except sqlite3.OperationalError:
        logging.warning('Error when select words from wordTable')
    return select_cursor


def generate_words_DB(file_name):
    file_obj = open(file_name, 'r').readlines()
    buffer_word = None
    buffer_list = ['', '', '', None, None, None]
    for line in file_obj:
        line = line.strip()
        title, content = line.split(':')
        if WORD.match(title.rstrip()):
            if buffer_word == None:
                buffer_word = title
            elif buffer_word != title:
                _insert_word(buffer_list)
                buffer_list = ['', '', '', None, None, None]
            buffer_word = title
            buffer_list[0] = title ; buffer_list[1] = title[::-1]
            if len(content.split(' - ')) != 2:
                buffer_list[2] = content
            else:
                buffer_list[2], buffer_list[3] = content.split(' - ')
        elif SYNONYM.match(title):
            buffer_list[4] = content.strip()
        elif ANTONYM.match(title):
            buffer_list[5] = content.strip()
    _insert_word(buffer_list)


def view_help_HTML():
    webbrowser.open('static/help.html')


def view_word_HTML():
    webbrowser.open('static/Vocabulary.html')


def generate_word_text_from_DB(DB_obj, tips=True):
    head = open('static/head.html', 'r').readline()
    if tips: head += '<h2 id="vocabulary-toefl">If you want doc file, please use \'python vocabulary.py -b\'</h2>'
    foot = open('static/foot.html', 'r').readline()
    word_tag = '<h4 id="1.-word">%d. %s</h4>'
    content_tag = '<pre><code>%s</code></pre>'
    output_text = head
    word_text_list = list()
    index = 0
    select_cursor = _select_word(DB_obj.cursor(), args[4])
    while True:
        item = select_cursor.fetchone()
        if item == None: break
        index += 1
        word_text = word_tag % (index, item['word'].lower())
        content = '\tMean: %s\n' % item['mean']
        if item['eg']: content = content + '\tE.g: %s\n\t' % item['eg']
        if item['synonym']:
            synonym_list = item['synonym'].split(',')
            synonym_content = '%s' % 'Synonym' if len(synonym_list) == 1 else 'Synonyms'
            synonym_content += ':\n'
            for synonym in synonym_list:
                synonym_content = synonym_content + '\t    %s\n' % synonym.strip() if synonym != None else ''
            content = content + synonym_content
        if item['antonym']:
            antonym_list = item['antonym'].split(',')
            antonym_content = '\t'
            antonym_content += '%s:' % 'Antonym' if len(antonym_list) == 1 else 'Antonyms'
            antonym_content += '\n'
            for antonym in antonym_list:
                antonym_content = antonym_content + '\t    %s\n' % antonym.strip() if antonym != None else ''
            content = content + antonym_content
        word_text = word_text + content_tag % content
        word_text_list.append(word_text)
    output_text = output_text + ''.join(word_text_list) + foot
    logging.critical('Success when generate text of word list.')
    return output_text


def generate_file(output_text, doc_name):
    output_file_html = open('static/Vocabulary.html', 'w') ; output_file_html.write(output_text)
    logging.critical('Success when write into html file.')
    if doc_name:
        output_file_doc = open('%s.doc' % doc_name, 'w') ; output_file_doc.write(output_text)
        logging.critical('Success when write into doc file.')

'''
argument:
-b(--both):default output html. if not -b it will not output doc file
-db:db file name. default word.db
-o:output file name. default Vocabulary.doc
-t:txt file name. default TOEFL.txt
-r:reverse or not. default to be False
'''

def check_argument(argv, length):
    if len(argv) <= length:
        logging.warning('Wrong argument %s!!' % argv)
        return False
    return True



if __name__ == '__main__':
    if len(ARGVs) == 1:
        view_help_HTML()
        exit()
    args = [True, 'word.db', None, 'TOEFL.txt', False]
    for argv in ARGVs:
        if argv.startswith('-b') or argv.startswith('--both'):
            args[0] = False ; args[2] = 'Vocabulary'
        elif argv.startswith('-db'):
            if check_argument(argv, 3): args[1] = argv[3:]
        elif argv.startswith('-o'):
            if check_argument(argv, 2):
                args[2] = argv[2:]
                args[0] = False
        elif argv.startswith('-t'):
            if check_argument(argv,2): args[3] = argv[2:]
        elif argv.startswith('-r'): args[4] = True
    DB_obj, cursor_obj = init_DB(args[1])
    generate_words_DB(args[3])
    output_text = generate_word_text_from_DB(DB_obj, args[0])
    generate_file(output_text, args[2])
    view_word_HTML()











