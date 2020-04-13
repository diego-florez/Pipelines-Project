from send_email import *
import functions as f


def main():
    arg = f.get_arg()
    email_generator(arg.movie)
    pass


if __name__ == '__main__':
    main()