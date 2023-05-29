import psycopg2
import sys
from dotenv import load_dotenv

load_dotenv()


def cursor(func):
    def wrapper(*args, **kwargs):
        conn = psycopg2.connect(
            host="yourhost",
            database="yourdatabase",
            user="yourusername",
            password="yourpassword"
        )
        cur = conn.cursor()
        result = func(cur, *args, **kwargs)
        conn.commit()
        cur.close()
        conn.close()
        return result

    return wrapper

# import psycopg2
#
#
# def connect(host: str = None, database: str = None, user: str = None, password: str = None):
#     conn = None
#     try:
#         conn = psycopg2.connect(
#             host=host,
#             database=database,
#             user=user,
#             password=password)
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')
