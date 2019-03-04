import os
import argparse

def main(database, url_list_file):
    print('Db: ' + database)
    print('input list: ' + url_list_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="db filename")
    parser.add_argument("-i", "--input", help="url file")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)

