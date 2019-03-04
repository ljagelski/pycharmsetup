import os
import argparse
from utilities import url_utilities

def main(database, url_list_file):
    big_word_list = []
    print('Db: ' + database)
    print('input list: ' + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print('reading: ', url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="db filename")
    parser.add_argument("-i", "--input", help="url file")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)

