from django.db import connection
from django.shortcuts import redirect
from main.sql_utils import named_tuple_fetchall, tuple_fetchall
post_table = 'main_comment'


def delete_this_post(id, user_id):
    with connection.cursor as cursor:
        cursor.execute('select user_id  from {post_table} where id = {id}')
        post = named_tuple_fetchall(cursor)

    print(post)
    # if post.author.id == request.user.id:
    #     post.delete()
    #     return redirect("home")
    # else:
    #     return redirect("home")