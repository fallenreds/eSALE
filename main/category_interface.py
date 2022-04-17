from django.db import connection

from main.sql_utils import named_tuple_fetchall, tuple_fetchall

category_table_name = "main_category"


def retrieve_category(category_id: int):
    with connection.cursor() as cursor:
        cursor.execute(f"select id from {category_table_name} where id = %s", [category_id])

        category = named_tuple_fetchall(cursor)

    return category


def to_str(obj):
    return obj.title


def list_categories():
    with connection.cursor() as cursor:
        cursor.execute(f"select id, title from {category_table_name}")
        categories = tuple_fetchall(cursor)
    return categories
