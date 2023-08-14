
def input_choice():
    print('0. Exit')
    print('1. Add user')
    print('2. Remove user')
    print('3. List users')

    return input('Choose a choice: ')


def add_user(users):
    user = input('Enter user: ')
    users.append(user)
    print(f'Added {user}')

def remove_user(users):
    user = input('Enter user: ')
    if user in users:
        users.remove(user)
    else:
        print(f'{user} not found')

def list_users(users):
    if len(users) == 0:
        print('No users')
    else:
        list = (sorted(users))
        print('List of users: ')
        for user in list:
            print(' - ' + user)

def read_user_from_file():
    with open('users.txt', 'r') as file:
        usersFromFile = file.readlines()
        users = [user.rstrip('\n') for user in usersFromFile]

    return users

def write_user_to_file(users):
    with open('users.txt', 'w') as file:
        file.writelines([user + '\n' for user in users])



