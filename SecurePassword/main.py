# logic is to simply replace some character of your password
# like if my password is manish then i can set it as m@n1$h
# i.e. i have simply replace character a with @, i with 1, and s with $

SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'))


def securePassword(password):
    for a, b in SECURE:
        password = password.replace(a, b)
    return password


if __name__ == '__main__':
    password = input("enter your password: ")
    print(f'your password should be {securePassword(password)}')
