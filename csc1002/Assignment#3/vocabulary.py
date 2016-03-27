# coding=utf-8
# ********************************************************
#   > OS     : Ubuntu 15.10
# 	> Author : JasonGUTU
# 	> Mail   : intergujinjin@foxmail.com
# 	> Time   : 2016/3/19
# ********************************************************
import re  # To compile words
import logging  # To log debug message
import os
import sys  # To obtain argument. If you can't open this with argument, That is fine.
import sqlite3  # Import the database
import webbrowser  # Use browser to display html
import platform  # check the system because Windows may execute this bed

# Config logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='Vocabulary.log',
                    filemode='w')

# get argument
ARGVs = sys.argv

# set re compile to compile words, synonyms and antonym
WORD = re.compile(r'^[A-Z]+$')
SYNONYM = re.compile(r'Synonym')
ANTONYM = re.compile(r'Antonym')

# initialize database
def init_DB(DB_file_name):
    # check if database file exist
    existed = False
    if DB_file_name in os.listdir('.'):
        existed = True
    # connect database and set cursor
    db = sqlite3.connect(DB_file_name, check_same_thread=False)
    db.row_factory = sqlite3.Row
    curs = db.cursor()
    # create table
    SQL_create_wordList = 'create table wordTable(word varchar(255),rword varchar(255),mean varchar(255),eg varchar(255),synonym varchar(255),antonym varchar(255));'
    if not existed:
        try:
            curs.execute(SQL_create_wordList)
            db.commit()
            logging.critical('Success when create table wordTable')
        except sqlite3.OperationalError:
            logging.warning(DB_file_name + 'Error when create table')
            raise sqlite3.OperationalError('Error when create table')
    # return the database object and the cursor object
    return db, curs

# function to insert into database
def _insert_word(list_every_word):
    try:
        SQl_insert = 'insert into wordTable (word,rword,mean,eg,synonym,antonym) values (?,?,?,?,?,?);'
        cursor_obj.execute(SQl_insert, (list_every_word[0], list_every_word[1], list_every_word[2], list_every_word[3], list_every_word[4], list_every_word[5]))
        logging.critical('Success when insert word \'%s\'' % list_every_word[0])
    except sqlite3.OperationalError:
        logging.critical('Error when insert word \'%s\' ' % list_every_word[0])
        logging.critical('R   %s' % list_every_word[1])

# function to select word from database
def _select_word(cursor_obj, reverse_order):
    # reverse select
    SQL_select = 'select * from wordTable order by word' if not reverse_order else 'select * from wordTable order by rword'
    try:
        select_cursor = cursor_obj.execute(SQL_select)
    except sqlite3.OperationalError:
        logging.warning('Error when select words from wordTable')
    return select_cursor

# read the txt file, and insert every word
def generate_words_DB(file_name):
    file_obj = open(file_name, 'r').readlines()
    # set a buffer to insert word conveniently
    buffer_word = None
    buffer_list = ['', '', '', None, None, None]  # ['word', 'word reversed', 'mean', 'example', 'synonyms', 'antonyms']
    # read file line by line
    for line in file_obj:
        line = line.strip()  # drop the '\n' and space
        title, content = line.split(':')  # split lien by ':'
        if WORD.match(title.rstrip()):  # check if word line
            if buffer_word == None:  # for the first word
                buffer_word = title  # when I read the first line, there isn't word in buffer, So I need to jump the first word
            elif buffer_word != title:  # if it is a new word, then insert the buffer list into database
                _insert_word(buffer_list)  # and set a new buffer word and list
                buffer_list = ['', '', '', None, None, None]
            buffer_word = title
            buffer_list[0] = title ; buffer_list[1] = title[::-1].strip()  # for reverse word
            if len(content.split(' - ')) != 2:  # set the mea and eg
                buffer_list[2] = content
            else:
                buffer_list[2], buffer_list[3] = content.split(' - ')
        elif SYNONYM.match(title):  # match synonym
            buffer_list[4] = content.strip()
        elif ANTONYM.match(title):  # match antonym
            buffer_list[5] = content.strip()
    _insert_word(buffer_list)  # insert the latest word

# use browser to view help html
def view_help_HTML():
    webbrowser.open('static/help.html')

# use browser to view word html page
def view_word_HTML():
    webbrowser.open('static/Vocabulary.html')

# read database and generate html text
def generate_word_text_from_DB(DB_obj, reverse=False):
    head = open('static/head.html', 'r').readline()  # read html head
    # if there no argument, display this
    foot = open('static/foot.html', 'r').readline()  # read the html footer
    word_tag = '<h4 id="1.-word">%d. %s</h4>'  # word html tag
    content_tag = '<pre><code>%s</code></pre>'  # content html tag
    output_text = head  # prepare the output html code
    word_text_list = list()  # prepare a list for every words
    index = 0  # count the words
    select_cursor = _select_word(DB_obj.cursor(), reverse)  # read the database
    while True:  # start a loop to read every words
        item = select_cursor.fetchone()  # fetch a word
        if item == None: break  # if there is not word exist, break loop
        index += 1
        word_text = word_tag % (index, item['word'].lower())  # write into word tag
        content = '\tMean: %s\n' % item['mean']  # write into content tag
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
        word_text = word_text + content_tag % content  # combine two things
        word_text_list.append(word_text)  # add every word into output list
    output_text = output_text + ''.join(word_text_list) + foot  # combine all elements into output list
    logging.critical('Success when generate text of word list.')  # log
    return output_text

# put output text into files
def generate_file(output_text, doc_name):
    output_file_html = open('static/Vocabulary.html', 'w') ; output_file_html.write(output_text)
    logging.critical('Success when write into html file.')
    if doc_name:
        output_file_doc = open('%s.doc' % doc_name, 'w') ; output_file_doc.write(output_text)
        logging.critical('Success when write into doc file.')


# argument:
# -b(--both):default output html. if not -b it will not output doc file
# -db:db file name. default word.db
# -o:output file name. default Vocabulary.doc
# -t:txt file name. default TOEFL.txt
# -r:reverse or not. default to be False

# check the arguments
def check_argument(argv, length):
    if len(argv) <= length:
        logging.warning('Wrong argument %s!!' % argv)
        return False
    return True


# main
if __name__ == '__main__':
#     if len(ARGVs) == 1:
#         view_help_HTML()
#         exit()
# # ################################################################
# # !!!! I'M THINKING THAT MAYBE TA's COMPUTER IS WINDOWS OS
# #     SO I SET THE FIRST ARGUMENT IS FALSE
# #     WHICH MEANS YOU DON'T NEED TO PUT -b ARGUMENT TO GET DOC FILE
# # ################################################################
#     args = [False, 'word.db', None, 'TOEFL.txt', False]
#     for argv in ARGVs:
#         if argv.startswith('-b') or argv.startswith('--both'):
#             args[0] = False ; args[2] = 'Vocabulary'
#         elif argv.startswith('-db'):
#             if check_argument(argv, 3): args[1] = argv[3:]
#         elif argv.startswith('-o'):
#             if check_argument(argv, 2):
#                 args[2] = argv[2:]
#                 args[0] = False
#         elif argv.startswith('-t'):
#             if check_argument(argv,2): args[3] = argv[2:]
#         elif argv.startswith('-r'): args[4] = True
    # initialize database
    DB_obj, cursor_obj = init_DB('word.db')
    # read txt file
    generate_words_DB('TOEFL.txt')
    # get the output text
    output_text = generate_word_text_from_DB(DB_obj, False)
    re_output_text = generate_word_text_from_DB(DB_obj, True)
    generate_file(output_text, 'Vocabulary')
    generate_file(re_output_text, 're_Vocabulary')
    # view_word_HTML()

