import psycopg2

def conexion():
    return psycopg2.connect(
        dbname="examenRecuFastApi", user="postgres", password="admin", host="localhost", port="5432"
    )
