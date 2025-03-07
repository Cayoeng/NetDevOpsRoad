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
        str1 = qytang_get_config(ip)

        trim_config = re.search(r'hostname.*', str1, re.DOTALL)

        current_md5 = hashlib.md5(trim_config.group(0).encode('utf-8')).hexdigest()

        if before_md5 == '':
            before_md5 = current_md5
            print(current_md5)
        elif current_md5 == before_md5:
            print(current_md5)
        else:
            print(current_md5)
            break


if __name__ == '__main__':
    target_ip = input('Please input device\'s IP address: ')
    qytang_check_diff(target_ip)