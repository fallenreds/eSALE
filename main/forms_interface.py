from django.db import connection
from django.utils import timezone
post_table_name = "main_post"
comment_table_name = "main_comment"
field_conversion = {
    "category": "category_id"
}

def handle_uploaded_file(f,image):
    with open('media/'+image, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def create_post(validated_data, author_id):
    cleaned_data = {field_conversion.get(k, k): v for k, v in validated_data.items()}
    # print(cleaned_data)
    cleaned_data["image"] = 'main/'+str(cleaned_data["image"])
    cleaned_data["published_date"] = timezone.now()
    cleaned_data["author_id"] = author_id
    handle_uploaded_file(validated_data['image'],cleaned_data["image"])
    columns = ",".join(list(cleaned_data.keys()))
    values_prepare = ",".join(['%s' for _ in range(len(cleaned_data.keys()))])

    with connection.cursor() as cursor:
        cursor.execute(
            f"insert into {post_table_name} ({columns}) values ({values_prepare});",
            [v for v in cleaned_data.values()]
        )

def create_comment(validated_data, author_id,profile_id):
    cleaned_data = validated_data
    cleaned_data['author_id'] = author_id
    cleaned_data['profile_id'] = profile_id
    cleaned_data['created_date'] = timezone.now().date()

    columns = ",".join(list(cleaned_data.keys()))
    values_prepare = ",".join(['%s' for _ in range(len(cleaned_data.keys()))])

    with connection.cursor() as cursor:
        cursor.execute(
            f"insert into {comment_table_name} ({columns}) values ({values_prepare});",
            [v for v in cleaned_data.values()]
        )