from zxcvbn import zxcvbn


def get_password_strength(password):
    rank = zxcvbn(password)
    return (rank["score"]//0.4)+1


def main():
        password = input("Please type your  password: ")
        rank = get_password_strength(password)
        print("Your password got {} point of security".format(rank))


if __name__ == '__main__':
    main()
