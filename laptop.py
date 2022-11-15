import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                    password="gamerzlife",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres_db")

    cursor = connection.cursor()
    sql_test_2 = """SELECT round(width / 5) * 5, round(depth / 5) * 5, round(height / 5) * 5, COUNT(id) 
            FROM notebooks_notebook 
            GROUP BY notebooks_notebook.width, notebooks_notebook.depth, notebooks_notebook.height 
            ORDER BY width, depth, height;"""
            
    sql_test_1 = """SELECT notebooks_brand.title, COUNT(notebooks_notebook.id) 
            FROM notebooks_notebook, notebooks_brand  WHERE notebooks_notebook.brand_id = notebooks_brand.id
            GROUP BY notebooks_brand.title, notebooks_notebook.brand_id
            ORDER BY -COUNT(notebooks_notebook.id)
            """
    cursor.execute(sql_test_1)
    test_1 = cursor.fetchall()
    for res in test_1:
        print(res)

    cursor.execute(sql_test_2)
    test_2 = cursor.fetchall()
    for i in test_2:
        print(res)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

