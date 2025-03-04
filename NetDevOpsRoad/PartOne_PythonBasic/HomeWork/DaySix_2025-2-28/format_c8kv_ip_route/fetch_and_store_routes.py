import paramiko
import psycopg2

def get_ip_routes(host, port=22, username='admin', password='Cisc0123', cmd='show ip route'):
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


def store_routes_in_db(route_output, db_config):
    def insert_new_line(log_line):
        conn = psycopg2.connect(
            host="198.19.249.56",
            port=5432,
            database="mydb",
            user="myuser",
            password="mypass"
        )
        cursor = conn.cursor()

        insert_query = "INSERT INTO asa_data (log_line) VALUES (%s)"
        cursor.execute(insert_query, (log_line,))
        conn.commit()  # 关闭连接

        cursor.close()
        conn.close()
        print("Data inserted successfully.")