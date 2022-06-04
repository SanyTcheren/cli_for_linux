#!/home/sany/anaconda3/bin/python3
#mybuffer.py - копирует в системный буфер обмена фразу из mybuffer.json
#Для корректной работы требуется установить xclip!!!!!!

import sys
import json
import pyperclip

def main():
    with open('mybuffer.json') as phrases:
        TEXT=json.load(phrases)
    if len(sys.argv) == 1 or sys.argv[1] not in TEXT.keys():
        print('Используйте с одним из следующий аргументов:')
        length = max([len(x) for x in TEXT.keys()])+5
        for key,value in TEXT.items():
            print('\t'+key.ljust(length,'.')+value)
    else:
        text = TEXT[sys.argv[1]]
        pyperclip.copy(text)
        print('Скопированно в буфер обмена:')
        print(pyperclip.paste())

if __name__ == '__main__':
    main()
