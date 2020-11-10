import os
import atexit
import psycopg2
from functools import partial


UMK_DB = os.environ["UMK_DB"]
AUTH_DB = os.environ["AUTH_DB"]
ES_URI = os.environ["ES_URI"]

UMK_NAME_CONNECTION = "umk_connection"
AUTH_NAME_CONNECTION = "auth_connection"


def remove_connection(name):
    """
    Удаление коннекшена по имени.

    :param name: имя коннекшена.
    :return: None.
    """

    conn = globals().get(name, None)
    if conn is not None:
        conn.close()


@atexit.register
def cleanup():
    """
    Удаление всех коннекшенов. Выполняется перед завершением работы интерпретатора.

    :return: None.
    """

    remove_connection(UMK_NAME_CONNECTION)
    remove_connection(AUTH_NAME_CONNECTION)


def set_global_connection(name, db_variable):
    """
    Создание коннекшена и сохранение его в глобальное окружение.

    :param name: имя коннекшена.
    :param db_variable: данные для коннекшена в виде строки из .env файла.
    :return: None.
    """

    tokens = (token.split("=") for token in db_variable.split(";"))
    tokens = {name: value for name, value in tokens}
    connection = psycopg2.connect(**tokens)
    globals()[name] = connection


def setup():
    """
    Создание всех коннекшенов и сохранение их в глобальное окружение.

    :return: None.
    """

    try:
        set_global_connection(UMK_NAME_CONNECTION, UMK_DB)
        set_global_connection(AUTH_NAME_CONNECTION, AUTH_DB)
    except:
        cleanup()
        raise


def get_connection(name):
    """
    Получение коннекчшена из глобального окружения.

    :param name: название коннекшена.
    :return: None.
    """

    conn = globals().get(name, None)
    if conn is None:
        setup()

    return globals()[name]


get_umk_connection = partial(get_connection, UMK_NAME_CONNECTION)
get_auth_connection = partial(get_connection, AUTH_NAME_CONNECTION)
