import re
import paramiko
from ssh import qytang_ssh

def ssh_get_route(ip, username, password, port=22, cmd='route -n'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode('utf-8')
        gateway = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})\s+\S+\s+UG', x)[0]
        return gateway
    except Exception as e:
        print(f'Fail to get route gateway {ip}!{e}')

if __name__ == '__main__':
    print(qytang_ssh('192.168.64.16', 'root', 'B1216.123'))
    print(qytang_ssh('192.168.64.16', 'root', 'B1216.123', cmd='pwd'))
    print('Gateway:')
    print(ssh_get_route('192.168.64.16', 'root', 'B1216.123'))