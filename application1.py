# from app1_functions import read_work, write_work
import time

import app1_functions

now = time.strftime("%b %d %Y, %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add or show or edit or complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        work = user_action[4:]

        task = app1_functions.read_work()

        task.append(work + '\n')

        app1_functions.write_work(task)

    elif user_action.startswith('show'):

        task = app1_functions.read_work()

        for index, pending in enumerate(task):
            pending = pending.strip('\n')
            row = f"{index + 1}-{pending}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            task = app1_functions.read_work()

            new_work = input("Enter the new task: ")
            task[number] = new_work + '\n'

            app1_functions.write_work(task)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            task = app1_functions.read_work()

            index = number - 1
            task_to_remove = task[index].strip('\n')
            task.pop(index)

            message = f"task {task_to_remove} was removed from the file"
            print(message)
        except IndexError:
            print("There is no task with that number.")
            continue

        app1_functions.write_work(task)

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid")

print("closed!")
print("Bye!")
