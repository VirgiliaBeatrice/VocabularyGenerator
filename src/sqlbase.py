#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15/09/05

import sqlite3


#TODO: Add more class method for Database Class.
class Database():
    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name.decode('utf-8'))
        # self.db = sqlite3.connect(':memory:')
        self.cr = self.db.cursor()

    def create_table(self, table_name, columns_detail):
        command = [
            ('', False),
            'CREATE TABLE',
            table_name,
            columns_detail
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

    def query(self, table_name, columns_name, conditions):
        command = [
            ('', False),
            'SELECT',
            columns_name,
            'FROM',
            table_name,
            'WHERE',
            conditions
        ]
        print create_str(command)
        self.cr.execute(create_str(command))
        return self.cr.fetchall()

    def update(self, table_name, values, conditions):
        command = [
            ('', False),
            'UPDATE',
            table_name,
            'SET',
            values,
            'WHERE',
            conditions
        ]

        print create_str(command)
        self.cr.execute(create_str(command))
        self.db.commit()

    def insert(self, table_name, values):
        query_qmark = ['?' for dummy_idx in range(len(values))]
        query_qmark.insert(0, (',', True))

        command = [
            ('', False),
            'INSERT INTO',
            table_name,
            'VALUES',
            query_qmark
        ]
        print create_str(command)
        self.cr.execute(create_str(command), values)
        self.db.commit()

    def disconnect(self):
        self.db.close()



def create_str(target):
    return_str = u''

    if isinstance(target, dict):
        iter_target = target.copy()
        sep = iter_target.pop('sep')
        hasBracket = iter_target.pop('hasBracket')
        for element_key, element_value in iter_target.iteritems():
            return_str += (element_key.decode('utf-8') + u'=' + element_value.decode('utf-8') +
                           sep.decode('utf-8') + u' ')
    else:
        sep = target[0][0]
        hasBracket = target[0][1]
        for element in target[1:]:
            if isinstance(element, tuple) or isinstance(element, list) or isinstance(element, dict):
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
    # db.create_table('Vocabulary', columns)
    # db.insert('Vocabulary', ('A', 'A', 'A', 'A', 'A'))
    # db.update('Vocabulary', {'sep': ',', 'hasBracket': False, 'Word': '\'abandon\'', 'Pronunciation': '\'aa\''},
    #           {'sep': '', 'hasBracket': False, 'Word': '\'A\''})
    print db.query('Vocabulary', ((',', False), 'Word'), {'sep': '', 'hasBracket': False, 'Word': '\'abandon\''})
    pass