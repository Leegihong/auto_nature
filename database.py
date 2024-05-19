import mysql.connector
from mysql.connector import Error

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully.")
    except Error as e:
        print(f"Failed to create database '{database_name}'. Error: {e}")

def create_table(cursor, table_sql):
    try:
        cursor.execute(table_sql)
        print("Table created successfully.")
    except Error as e:
        print(f"Failed to create table. Error: {e}")

def save_papers_to_db(papers):
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='filab1020')
        cursor = connection.cursor()
        
        database_name = 'nature'
        create_database(cursor, database_name)
        
        cursor.execute(f"USE {database_name}")
        
        # 'abstract' 컬럼을 추가합니다.
        table_sql = """CREATE TABLE IF NOT EXISTS papers (
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       title VARCHAR(255) NOT NULL,
                       link VARCHAR(255) NOT NULL,
                       abstract TEXT)"""  # TEXT 타입으로 abstract 컬럼 추가
        create_table(cursor, table_sql)
        
        for paper in papers:
            title = paper["title"]
            link = paper["link"]
            abstract = paper["abstract"]  # 초록 추출
            query = "INSERT INTO papers (title, link, abstract) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, link, abstract))
        connection.commit()
        print(f'{cursor.rowcount} papers were saved to the database.')
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MariaDB connection is closed.")
