# !/usr/bin/env python3

import mysql.connector
from mysql.connector import errorcode


class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                    host='localhost',
                    user='sanjay',
                    database='player_info'
                    )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(err)

    def create_table(self):
        try:
            self.cursor.execute("CREATE TABLE players(id INT AUTO_INCREMENT PRIMARY KEY\
                                    ,player_name varchar(40) not null\
                                    ,position varchar(20) not null\
                                    ,height varchar(20) not null\
                                    ,rank int(3) not null\
                                    ,image_url blob not null\
                                    ,player_info_link varchar(255) not null)")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print('table already exists')
                pass

    def insert_into_table(self, values):
        sql = 'INSERT IGNORE INTO players(id, player_name, rank, position, image_url, height, player_info_link)\
                    values(%s, %s, %s, %s, %s, %s, %s)'
        self.cursor.execute(sql, values)
        self.connection.commit()

    def select_from_database(self):
        sql = 'select * from players'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result
