from ssh import qytang_ssh
import re
import hashlib
import time


def qytang_get_config(ip, username='admin', password='Cisc0123'):
    try:
        curren_config = qytang_ssh(ip, username, password, cmd='show run')
        if curren_config:
            return curren_config

    except Exception:
        return print(f'\nFail to get config from {ip}!')


def qytang_check_diff(ip):
    before_md5 = ''
    while True:
        time.sleep(5)

#        trim_config = re.findall('^hostname', qytang_get_config(ip), re.DOTALL)
        trim_config = qytang_get_config(ip)
        current_md5 = hashlib.md5(trim_config.encode('utf-8')).hexdigest()

        if current_md5 != before_md5:
            before_md5 = current_md5
            print(f'\nConfig has been changed on {ip}!')
        else:
            print(before_md5)


if __name__ == '__main__':
    target_ip = input('Please input device\'s IP address: ')
    qytang_check_diff(target_ip)