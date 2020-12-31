import random
import string

# class Account:
#     def __init__(self):
#         self.card_number = random.randint(400000000000, 40000099999)
#         self.pin = random.randint(0000, 9999)
#         self.balance = 0


def generate_credit_card_number():
    account_identifier = random.randint(100000000, 999999999)
    card_number = '400000' + str(account_identifier)
    fifteen_digit = list(card_number)
    fifteen_digit = [int(x) for x in fifteen_digit]
    # print(fifteen_digit)

    for digit in range(1, 16, 2):
        fifteen_digit[digit - 1] = fifteen_digit[digit - 1] * 2

    # print(fifteen_digit)

    for digit in range(0, len(fifteen_digit)):
        if fifteen_digit[digit] > 9:
            fifteen_digit[digit] = fifteen_digit[digit] - 9

    # print(fifteen_digit)
    # print(sum(fifteen_digit))

    if sum(fifteen_digit) % 10 == 0:
        checksum = 0
    else:
        checksum = 10 - (sum(fifteen_digit) % 10)
    # print(checksum)

    card_number = int(card_number + str(checksum))
    return card_number


accounts = []

print("1. Create an account")
print("2. Log into account")
print("0. Exit")

response = int(input())
while response != 0:
    if response == 1:
        card_number = generate_credit_card_number()
        # pin = int(format(random.randint(0000, 9999), '04d'))
        chars = string.digits
        pin = int(''.join(random.choice(chars) for _ in range(4)))
        balance = 0
        account = [card_number, pin, balance]
        print('Your card has been created')
        print('Your card number')
        print(card_number)
        print('Your card PIN')
        print(pin)
        accounts.append(account)
        # print(accounts)
    elif response == 2:
        card_number_input = int(input("Enter your card number:"))
        pin_input = int(input("Enter your PIN:"))

        current_account = None
        for a in accounts:
            if a[0] == card_number_input and a[1] == pin_input:
                current_account = a

        if current_account is not None:
            print('\n')
            print('You have successfully logged in!')

            response = None
            while response != 2:
                print('\n')
                print('1. Balance')
                print('2. Log out')
                print('0. Exit')
                response = int(input())

                if response == 0:
                    quit()
                elif response == 1:
                    print('\n')
                    print('Balance', current_account[2])
                elif response == 2:
                    print('\n')
                    print('You have successfully logged out!')
        else:
            print('\n')
            print("Wrong card number or PIN!")

    print('\n')
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    response = int(input())
