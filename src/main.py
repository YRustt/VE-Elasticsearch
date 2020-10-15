import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delete", dest="delete", action="store_true", required=False,
                        help="удалить индекс в elasticsearch")
    parser.add_argument("-uh", "--update-head", dest="update_head", action="store_true", required=False,
                        help="обновить индекс в elasticsearch с начала")
    parser.add_argument("-u", "--update", dest="update", action="store_true", required=False,
                        help="обновить индекс в elasticsearch с последнего добавленного элемента")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()


if __name__ == "__main__":
    main()
