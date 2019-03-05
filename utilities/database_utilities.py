import pymysql
import logger
import sys


conn = None
rds_host = 'localhost'
name = 'lenj'
password = 'lenj'
db_name = 'sakila'

def openConnection():
    global conn
    try:
        if (conn is None):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        elif (not conn.open):
            conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()



def create_database(table):
    openConnection()
    with conn.cursor() as cur:
        # sql = "SELECT * FROM table"
        #sql = "drop table if exists dbtbl"
        sql = "drop table if exists {}".format(table)
        cur.execute(sql)
        #sql = "CREATE TABLE dbtbl" \
        sql = "CREATE TABLE {}" \
              "(word varchar(25) NOT NULL,count int(6) NOT NULL DEFAULT 1)".format(table)
        cur.execute(sql)
        print('created table: {}'.format(table))




def save_words_to_database(database_path, words_list):
    # todo: do it
    pass

create_database('dbtbl')
