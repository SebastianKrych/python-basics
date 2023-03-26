choice = -1
# file = open("todos.txt", "r")


def read_todo_file():
    file = open("todos.txt", "r")
    return file.readlines()


def show_todo():
    file = open("todos.txt", "r")
    todo_index = 0
    print("TODO list:")
    for todo in file.readlines():
        print("[" + str(todo_index) + "]" + todo.strip())
        todo_index += 1
    file.close()


def add_todo():
    lines = read_todo_file()
    file = open("todos.txt", "w+")

    for line in lines:
        file.write(line)
        file.write("\n")

    file.flush()
    todo = input("Add todo: ")
    file.write(todo)
    file.flush()
    file.close()


def remove_todo_by_index():
    todos = []
    file = open("todos.txt", "r")
    for todo in file.readlines():
        todos.append(todo)
    file.close()

    index = input("Provide index of todo to be removed: ")
    line_index = 0

    file = open("todos.txt", "w+")
    for todo in file.readlines():
        if index == line_index:
            continue
        file.write(todo)


while choice != 4:
    print("1 show TODOs")
    print("2 add TODO")
    print("3 remove TODO")
    print("4 exit")
    print()
    choice = int(input("Perform action: "))
    print()

    if choice == 1:
        show_todo()
        print()

    if choice == 2:
        add_todo()

    if choice == 3:
        remove_todo_by_index()