from collections import namedtuple


class QuerysetMock:
    def __init__(self, object_list: list):
        self.object_list = list

    def all(self):
        return self.object_list


def dict_fetch_all(cursor) -> list:
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dict_fetch_one(cursor) -> dict:
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, cursor.fetchone()))


def named_tuple_fetchall(cursor) -> list:
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def tuple_fetchall(cursor) -> list:
    """Return all rows from a cursor as a namedtuple"""
    return list(cursor.fetchall())


def named_tuple_fetchone(cursor, custom=None) -> namedtuple:
    """Return one row from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    row = cursor.fetchone()
    return nt_result(*row) if row else None


def named_tuple_fetchuser(cursor, custom=None) -> namedtuple:
    """Return one row from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc] + ["is_authenticated"])
    row = cursor.fetchone()
    return nt_result(*row, True) if row else None


def get_update_set_command(validated_data: dict) -> str:
    params = [" = ".join([k, v]) for k, v in validated_data.items()]
    return ", ".join(params)
