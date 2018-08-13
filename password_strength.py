from zxcvbn import zxcvbn


def get_password_strength(password):
    strength_info = zxcvbn(password)
    return (strength_info["score"]//0.4)+1


def main():
        password = input("Please type your  password: ")
        score = get_password_strength(password)
        print("Your password got {} point(s) of security".format(score))


if __name__ == '__main__':
    main()
