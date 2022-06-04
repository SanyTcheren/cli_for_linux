#!/home/sany/anaconda3/bin/python3
"""
Преобразует системный буффер обмена, добавляя в начало каждой строки *
"""
import pyperclip


def main():
    count = 0
    while True:
        buffer = pyperclip.waitForNewPaste()
        buffer_list = buffer.split('\n')
        result = map(lambda a: '--ХУЙ--' + a, buffer_list)
        pyperclip.copy('\n'.join(result))
        count += 1
        print(f'{count} added')

if __name__ == '__main__':
    main()
