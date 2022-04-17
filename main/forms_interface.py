from django.db import connection

post_table_name = "main_post"

field_conversion = {
    "category": "category_id"
}


def create_post(validated_data, author_id):
    cleaned_data = {field_conversion.get(k, k): v for k, v in validated_data.items()}
    cleaned_data["author_id"] = author_id
    columns = ",".join(list(cleaned_data.keys()))
    values_prepare = ",".join(['%s' for _ in range(len(cleaned_data.keys()))])

    with connection.cursor() as cursor:
        cursor.execute(
            f"insert into {post_table_name} ({columns}) values ({values_prepare});",
            [v for v in cleaned_data.values()]
        )
