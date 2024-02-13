FILEPATH = "../task.txt"


def get_work(filepath=FILEPATH):
    """ Read a text file and return the list of task"""
    with open(filepath, 'r') as file_local:
        task_local = file_local.readlines()
        return task_local


def write_work(task_arg, filepath=FILEPATH):
    """Write the task list in the file"""
    with open(filepath, 'w') as file:
        file.writelines(task_arg)


if __name__ = "__main__":
    print("Hi")
    print(get_work())