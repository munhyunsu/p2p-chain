import os

FLAGS = _ = None
DEBUG = False


def main():
    if DEBUG:
        print(f'Parsed arguments {FLAGS}')
        print(f'Unparsed arguments {_}')


if __name__ == '__main__':
    root_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(root_path)
    os.chdir(root_dir)

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')
    parser.add_argument('--address', type=str, default='',
                        help='The server bind address')
    parser.add_argument('--port', type=int, default=6292,
                        help='The server service port')

    FLAGS, _ = parser.parse_known_args()
    DEBUG = FLAGS.debug

    main()

