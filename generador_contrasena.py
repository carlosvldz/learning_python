import random 


def generate_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symb = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayus + minus + symb + numbers

    password = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()