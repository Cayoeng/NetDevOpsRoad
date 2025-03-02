import psycopg2
#PostgreSQL数据源
def get_asa_connection_data_from_db():
    """
    从 PostgreSQL 数据库中读取 asa_conn 数据
    并返回用于后续解析的完整字符串。
    """
    # 连接到数据库
    conn = psycopg2.connect(
        host="198.19.249.56",
        port=5432,
        database="mydb",
        user="myuser",
        password="mypass"
    )
    cursor = conn.cursor()

    # 从数据库中获取数据
    cursor.execute("SELECT log_line FROM asa_data")
    records = cursor.fetchall()

    # 将多条记录拼接成一个字符串，可以使用换行分隔
    asa_conn = "\n ".join(row[0] for row in records)

    # 关闭连接
    cursor.close()
    conn.close()

    return asa_conn
