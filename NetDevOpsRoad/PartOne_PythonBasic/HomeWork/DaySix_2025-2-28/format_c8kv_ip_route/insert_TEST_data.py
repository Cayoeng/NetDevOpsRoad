import psycopg2

def insert_new_asa_log_line(log_line):

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
    conn.commit() # 关闭连接

    cursor.close()
    conn.close()
    print("Data inserted successfully.")

if __name__ == "__main__":
    new_line = "TCP Student 192.168.189.100:32806 Teacher 137.78.5.128:65100, idle 0:00:00, bytes 512, flags UIO"
    insert_new_asa_log_line(new_line)