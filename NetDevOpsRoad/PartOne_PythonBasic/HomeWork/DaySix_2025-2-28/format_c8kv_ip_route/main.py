
from get_asa_connection_data_from_db import *
from parse_asa_conn import parse_asa_connections
from print_asa_conn import print_asa_connections

from fetch_and_store_routes import paramiko_ssh
from insertFetchedData import insert_new_line


if __name__ == "__main__":

    # 获取测试环境c8k 192.168.64.101的路由表
    route_table = paramiko_ssh(input("Please input c8k ip: "))

    # 将从c8k获取的路由表写入PostgreSQL数据库
    insert_new_line(route_table)

    # 从数据库中获取数据
    asa_conn = get_asa_connection_data_from_db()

    # 解析数据
    asa_dict = parse_asa_connections(asa_conn)

    # 打印数据
    print_asa_connections(asa_dict)
