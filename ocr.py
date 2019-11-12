#!/usr/bin/env python3
# encoding: utf-8
# Author: Linus Boyle <linusboyle@gmail.com> 

from aip import AipOcr
import sys

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No image provided")
        exit(2)
    else:
        image = get_file_content(sys.argv[1])
        res = client.basicAccurate(image)
        if 'words_result' in res:
            for word in res['words_result']:
                print(word['words'])
        else:
            print("Error")
            exit(2)
