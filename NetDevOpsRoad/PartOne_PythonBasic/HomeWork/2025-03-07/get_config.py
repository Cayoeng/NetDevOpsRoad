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
        running_config = qytang_get_config(ip)
        trim_config = re.match(r'(^hostname[\s\S]*?end$)', '', running_config)
        current_md5 = trim_config.__hash__()
        if current_md5 != before_md5:
            before_md5 = current_md5
            return print(f'\nConfig has been changed on {ip}!')
        else:
            return before_md5


if __name__ == '__main__':
    target_ip = input('Please input device\'s IP address: ')
    qytang_check_diff(target_ip)