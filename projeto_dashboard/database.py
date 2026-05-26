import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Abn@rum12", # Sua senha atualizada
        database="dashboard"
    )