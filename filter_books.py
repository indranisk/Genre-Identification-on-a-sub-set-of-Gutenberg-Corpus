import pandas as pd
import re
import shutil
import os

BOOKS_PATH = "books"
NEW_BOOKS_PATH = './books_996'

def in_master_csv(book_id):
    df = pd.read_csv('master996.csv', encoding='latin1', sep=';')
    master_book_list = []
    for c, col in enumerate(df['book_id']):
        master_book_list.append(re.findall('(^pg[0-9]*)', col))
    return (bool([i for i, pg_id in enumerate(master_book_list) if book_id in pg_id]))


books_list = os.listdir(BOOKS_PATH)

count = 0
for book in books_list:
    book_id = re.findall('(^pg[0-9]*)', book)
    # print(book_id[0])
    if in_master_csv(book_id[0]):
        count += 1
        shutil.copy2(os.path.join(BOOKS_PATH, book), NEW_BOOKS_PATH)

print("books added: ", count)
