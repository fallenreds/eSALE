from django.db import connection
from django.shortcuts import redirect
from main.sql_utils import named_tuple_fetchall, tuple_fetchall, dict_fetch_one
post_table = 'main_post'

def delete_this_post(id, user_id):
    with connection.cursor() as cursor:
        cursor.execute(f'select author_id, id  from {post_table} where id = {id}')
        post = dict_fetch_one(cursor)
    if post['author_id'] == user_id:
        with connection.cursor() as cursor:
            cursor.execute(f'delete from {post_table} where id = {id}')
        return True
