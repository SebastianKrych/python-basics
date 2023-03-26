choice = -1
todos = []


def show_todo():
    todo_index = 0
    print("TODO list:")
    for todo in todos:
        print("[" + str(todo_index) + "]" + todo)
        todo_index += 1


def add_todo():
    todo = input("Add todo: ")
    todos.append(todo)


def remove_todo_by_index():
    index = input("Provide index of todo to be removed: ")
    todos.pop(int(index))


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
