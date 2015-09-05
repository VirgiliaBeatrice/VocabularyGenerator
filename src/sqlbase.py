#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15/09/05

import sqlite3

class Database():
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name.decode('utf-8'))
        # self.db = sqlite3.connect(':memory:')
        self.cr = self.db.cursor()

    def create_table(self, table_name, columns):
        command = [
            ('', False),
            'CREATE TABLE',
            table_name,
            columns
        ]
        # print create_str(command)

        try:
            self.cr.execute(create_str(command))
        except sqlite3.OperationalError, e:
            print 'Exception: ' + e.message

    def delete_table(self, table_name):
        command = [
            ('', False),
            'DROP TABLE',
            table_name
        ]

        try:
            self.cr.execute(create_str(command))
        except sqlite3.OperationalError, e:
            print 'Exception: ' + e.message

    def query(self, query_name, query_column):
        command = [
            ('', False),
            'SELECT',
            query_name,
            'FROM',
            query_column
        ]

        self.cr.execute(create_str(command))

    def update(self, table_name, value, column_name):
        pass
        # self.cr.execute('UPDATE ')

    def insert(self, table_name, values):
        command = [
            ('', False),
            'INSERT INTO',
            table_name,
            'VALUES',
            values
        ]

        self.cr.execute(create_str(command))
        self.db.commit()


# def create_tuple_str(target_tuple, sep=''):
#     tuple_str = u''
#     for element in target_tuple:
#         tuple_str += element.decode('utf-8') + sep.decode('utf-8') + u' '
#     return u'(' + tuple_str[:-len(sep.decode('utf-8') + u' ')] + u')'

def create_str(target_tuple):
    return_str = u''
    sep = target_tuple[0][0]
    hasBracket = target_tuple[0][1]

    for element in target_tuple[1:]:
        if isinstance(element, tuple) or isinstance(element, list):
            return_str += create_str(element) + sep.decode('utf-8') + u' '
        else:
            return_str += element.decode('utf-8') + sep.decode('utf-8') + u' '

    if hasBracket:
        return u'(' + return_str[:-len(sep.decode('utf-8') + u' ')] + u')'
    else:
        return return_str[:-len(sep.decode('utf-8') + u' ')]

# columns = [
#     (',', True),
#     (('', False), 'Word', 'TEXT'),
#     (('', False), 'Pronunciation', 'TEXT'),
#     (('', False), 'Grammar', 'TEXT'),
#     (('', False), 'Definition', 'TEXT'),
#     (('', False), 'Example', 'TEXT')
# ]
# command_1 = [
#     ('', False),
#     'CREATE',
#     'TABLE',
#     'table_name',
#     columns
# ]

# print create_str(command_1)


# cur.execute("insert into people values (?, ?)", (who, age))
# UPDATE Customers
#  SET ContactName='Alfred Schmidt', City='Hamburg'
#  WHERE CustomerName='Alfreds Futterkiste';
if __name__ == '__main__':
    db = Database('Vocabulary.db')
    columns = [
        (',', True),
        (('', False), 'Word', 'TEXT'),
        (('', False), 'Pronunciation', 'TEXT'),
        (('', False), 'Grammar', 'TEXT'),
        (('', False), 'Definition', 'TEXT'),
        (('', False), 'Example', 'TEXT')
    ]
    # print create_tuple_str(columns[1], ',')
    # db.delete_table('Vocabulary')
    db.create_table('Vocabulary', columns)
    # db.insert('Vocabulary', (u'A', u'A', u'A', u'A', u'A'))
    pass