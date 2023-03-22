import random


def dinner_date():
    guest_count = input("Enter the number of friends joining (including you): ")
    guest_dictionary = {}

    if guest_count.isnumeric() and int(guest_count) > 0:
        print("\nEnter the name of every friend (including you), each on a new line:")

        for _ in range(0, int(guest_count)):
            guest_dictionary[input()] = 0

        bill = input("\nEnter the total bill value: ")

        lucky_mode = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky_person = random.choice(list(guest_dictionary.keys()))

        for guest in guest_dictionary.keys():
            if lucky_mode == 'Yes':
                if guest != lucky_person:
                    guest_dictionary[guest] = round(int(bill) / (int(guest_count) - 1), 2)
            else:
                guest_dictionary[guest] = round(int(bill) / int(guest_count), 2)

        if lucky_mode == 'Yes':
            print(f"\n{lucky_person} is the lucky one!")
        else:
            print("\nNo one is going to be lucky")

    else:
        print("\nNo one is joining for the party")

        quit()


if __name__ == '__main__':
    dinner_date()
