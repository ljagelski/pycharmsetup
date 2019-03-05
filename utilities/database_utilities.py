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
              "(dword varchar(25) NOT NULL,wcount int(6) NOT NULL DEFAULT 1)".format(table)
        cur.execute(sql)
        print('created table: {}'.format(table))


def save_words_to_database(words_list):
    wdcount = -1
    openConnection()
    with conn.cursor() as cur:
        # sql = "SELECT * FROM table"
        # sql = "drop table if exists dbtbl"
        #sql = "drop table if exists {}".format(table)
        # sql = "insert into {} (word, count) Values " \
        #       "('watsup', 25)," \
        #       "('catsup', 5)," \
        #       "('dogsup', 75)".format(table)
        for word in words_list:
            #sql = "select count(word) from {} where word ='" + word + "'".format(table)
            #assert isinstance(word, object)
            sql = "SELECT wcount FROM dbtbl WHERE dword = '"  + word + "'"
            #sql = "SELECT wcount FROM {} WHERE dword = '"  + word + "'".format(table)
            #sql.rstrip()
            print("%%", sql, "%%")
            try:
                cur.execute(sql)
                #wdcount = cur.fetchone()[0]
                wdcount = cur.fetchone()[0]
            except:
                wdcount = -1 #call above fails if word not in dict

            #wcount = cur.fetchone()[0] #first entry in fetchone
            if wdcount > 0:
                sql = "UPDATE dbtbl SET wcount = wcount + 1 where dword ='" + word + "'"
                #cur.execute(sql)
            else:
                sql = "Insert into dbtbl (dword) Values ('" + word + "')"
            cur.execute(sql)
        conn.commit()
        cur.close()
        print('save words complete')


if __name__ == '__main__':
    wlist = ['big', 'dogsup', 'catty', 'dogsup']
    create_database('dbtbl')
    save_words_to_database(wlist)

