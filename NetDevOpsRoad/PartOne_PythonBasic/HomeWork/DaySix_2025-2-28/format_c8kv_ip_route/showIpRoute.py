import paramiko

def paramiko_ssh(host, port=22, username='admin', password='Cisc0123', cmd='show ip route'):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        x = stdout.read().decode('utf-8')
        return x
    except Exception as e:
        print(f'Fail to connect {host}!{e}')