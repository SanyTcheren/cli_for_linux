#!/home/sany/anaconda3/bin/python
"""Normalize phone number to a pattern: +N NNN NNN-NN-NN."""

import re
import pyperclip


def main():
    """Normalize phone number."""
    phone_rx = re.compile(
        r'''
        [+7,8]    #  internetional code
        [\s,-]?
        \(?
        (\d\d\d)  # 1 group - operator code
        \)?
        [\s,-]?
        (\d\d\d)  # 2 group number
        [\s,-]?
        (\d\d)    # 3 group number
        [\s,-]?
        (\d\d)    # 4 group number
        ''', re.VERBOSE)
    phone_am_rx = re.compile(
        r'''
        [+7,8]
        (\d\d)    # 1 group
        -
        (\d\d\d)  # 2 group
        -
        (\d\d\d\d\d)# 3 group
        ''', re.VERBOSE)
    while True:
        buff = pyperclip.waitForNewPaste()
        phone = phone_rx.search(buff)
        if phone:
            pyperclip.copy(f'+7 {phone[1]} {phone[2]}-{phone[3]}-{phone[4]}')
            continue
        phone = phone_am_rx.search(buff)
        if phone:
            pyperclip.copy(
                f'+7 {phone[1]+phone[2][0]} {phone[2][1:]+phone[3][0]}-' +
                f'{phone[3][1:3]}-{phone[3][3:]}'
            )


if __name__ == '__main__':
    main()
