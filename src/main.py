import argparse

import settings
from settings import setup, cleanup, get_umk_connection, get_auth_connection


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delete", dest="delete", action="store_true", required=False,
                        help="удалить индекс в mapping")
    parser.add_argument("-uh", "--update-head", dest="update_head", action="store_true", required=False,
                        help="обновить индекс в mapping с начала")
    parser.add_argument("-u", "--update", dest="update", action="store_true", required=False,
                        help="обновить индекс в mapping с последнего добавленного элемента")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    setup()

    try:

        conn = get_umk_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, content, rv FROM ftst LIMIT 10")
        records = cursor.fetchall()
        print(records)

        cursor.close()
    except:
        cleanup()
        raise


if __name__ == "__main__":
    main()
