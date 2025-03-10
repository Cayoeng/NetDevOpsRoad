import paramiko
import time


def qytang_multicmd(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    """
    依次执行 cmd_list 中的命令
    :param ip: 设备 IP
    :param username: SSH 用户名
    :param password: SSH 密码
    :param cmd_list: 要执行的命令列表
    :param enable: 如果有 enable 密码则传入，没有则保持为 ''
    :param wait_time: 每条命令执行后等待时间
    :param verbose: 是否打印命令输出信息
    :return: 每条命令执行返回信息组成的列表
    """
    output_list = []
    try:
        # 创建 SSHClient 实例
        ssh = paramiko.SSHClient()
        # 如没有本地主机密钥则自动添加
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接到网络设备
        ssh.connect(hostname=ip, port=22, username=username, password=password,
                    timeout=5, compress=True)
        # 激活交互式 shell
        chan = ssh.invoke_shell()
        time.sleep(wait_time)

        # 清空初始登录提示信息
        if chan.recv_ready():
            chan.recv(65535).decode('utf-8', 'ignore')

        # 如果有 enable 密码，则进入特权模式
        if enable:
            chan.send('enable\n')
            time.sleep(1)
            if chan.recv_ready():
                output = chan.recv(65535).decode('utf-8', 'ignore')
                # 如果路由器提示输入密码，则输入 enable 密码
                if 'assword' in output:
                    chan.send(enable + '\n')
                    time.sleep(wait_time)
                    if chan.recv_ready():
                        enable_output = chan.recv(65535).decode('utf-8', 'ignore')
                        if verbose:
                            print(enable_output, end='')

        # 依次执行 cmd_list 中的命令
        for cmd in cmd_list:
            # 发送命令
            chan.send(cmd + '\n')
            time.sleep(wait_time)
            # 接收输出
            if chan.recv_ready():
                cmd_output = chan.recv(65535).decode('utf-8', 'ignore')
                output_list.append(cmd_output)
                if verbose:
                    print(cmd_output, end='')

        # 关闭连接
        chan.close()
        ssh.close()
        return output_list
    except Exception as e:
        print(f"Fail to connect {ip}: {str(e)}")
        return output_list


# =======================
# 以下为测试代码示例
# =======================
if __name__ == '__main__':
    ip_test = '192.168.64.102'
    username_test = 'admin'
    password_test = 'Cisc0123'

    # 待执行命令列表：查看版本信息 + 配置 OSPF (process 1 并宣告一个网络)
    commands = [
        'terminal length 0',  # 防止分页
        'show version',  # 查看完整版本信息
        'conf t',
        'router ospf 1',
        'network 10.1.1.0 0.0.0.255 area 0',
        'end',
        'wr'
    ]

    # 如果需要 enable 密码，就填入；如果没有则保持为空字符串
    enable_password = ''

    qytang_multicmd(
        ip=ip_test,
        username=username_test,
        password=password_test,
        cmd_list=commands,
        enable=enable_password,
        wait_time=2,
        verbose=True
    )