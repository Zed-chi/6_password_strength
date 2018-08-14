import re
import string
import getpass


def get_points_of_chars(password):
    return len(password)*3


def get_points_of_uppercase_letters(password):
    letters = len(re.findall(r'[A-Z]', password))
    if letters > 0:
        return (len(password)-letters)*2
    else:
        return 0


def get_points_of_lowercase_letters(password):
    letters = len(re.findall(r'[a-z]', password))
    if letters > 0:
        return (len(password)-letters)*2
    else:
        return 0


def get_numbers_points(password):
    return len(re.findall(r'\d', password))*3


def get_middle_numbers_or_symbols_points(password):
    return len(re.findall(r'[a-zA-Z](\d|\W)[a-zA-Z]', password))*2


def get_symbols_points(password):
    return len(re.findall(r'\W', password))*6


def get_requirements_points(password):
    points = 0
    for i in [
        get_points_of_uppercase_letters(password),
        get_points_of_lowercase_letters(password),
        get_symbols_points(password),
        get_numbers_points(password),
            ]:
        if i > 0:
            points += 1
    if points >= 3 and len(password) >= 8:
        return (points+1*2)
    return 0


def get_letters_only_penalty(password):
    if get_numbers_points(password) == 0:
        return len(password)*-1
    return 0


def get_numbers_only_penalty(password):
    if len(re.findall(r'\w', password)) == 0:
        return len(password)*-3
    return 0


def get_repeats_penalty(password):
    penalty = 0
    sym = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
           "abcdefghijklmnopqrstuvwxyz0123456789")
    for char in sym:
        penalty += len(re.findall(char, password))
    return penalty * -1


def get_sequental_chars_penalty(password):
    penalty = 1
    for index in range(len(password)):
        if index < len(password)-1:
            if ord(password[index]) == ord(password[index+1])-1:
                penalty += 1
    return penalty * -3


def get_consecutive_chars_penalty(password):
    penalty = 0
    for index in range(len(password)):
        if index < len(password)-1:
            if ord(password[index]) == ord(password[index+1]):
                penalty += 2
    return (penalty * -3) if penalty >= 3 else 0


def get_password_strength(password):
    score = sum([
        get_points_of_chars(password),
        get_points_of_uppercase_letters(password),
        get_points_of_lowercase_letters(password),
        get_numbers_points(password),
        get_middle_numbers_or_symbols_points(password),
        get_symbols_points(password),
        get_requirements_points(password),
        get_letters_only_penalty(password),
        get_numbers_only_penalty(password),
        get_repeats_penalty(password),
        get_consecutive_chars_penalty(password),
        get_sequental_chars_penalty(password)
        ])
    if score >= 90:
        return 10
    elif score <= 1:
        return 1
    else:
        return (score/10)+1


def main():
    password = getpass.getpass("Please type pass to check: ")
    if len(password) == 0:
        exit("password is empty")
    print("You got", get_password_strength(password), "point(s) of security")


if __name__ == "__main__":
    main()
