import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode('utf-8')
        return x
    except Exception as e:
        print(f'Fail to connect {ip}!{e}')

if __name__ == '__main__':
    print(qytang_ssh('192.168.64.16', 'root', 'B1216.123'))
    print(qytang_ssh('192.168.64.16', 'root', 'B1216.123', cmd='pwd'))