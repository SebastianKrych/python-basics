choice = -1


def add_todo():
    file = open("todos.txt", "a+")
    todo = input("Add todo: ")

    for line in file.readlines():
        file.write("\n")
        break

    file.write(todo)
    file.write("\n")
    file.flush()
    file.close()


def print_todos():
    index = 0
    file = open("todos.txt", "r")
    for line in file.readlines():
        print("[" + str(index) + "] " + line.strip())
        index += 1
    file.close()


def delete_todo_by_index(index_to_remove):
    index = 0
    todo_list = []
    file = open("todos.txt", "r")
    for line in file.readlines():
        if index != index_to_remove:
            todo_list.append(line.strip())
            print("[" + str(index) + "] " + line.strip())
        index += 1
    file.close()
    print("list:")

    for line in todo_list:
        print(line)

    print("end")

    file = open("todos.txt", "w+")
    for line in todo_list:
        file.write(line)
        file.write("\n")
    file.flush()
    file.close()


while choice != 4:
    print("1 show TODOs")
    print("2 add TODO")
    print("3 remove TODO")
    print("4 exit")
    print("==================")
    print()
    choice = int(input("Perform action: "))
    print()

    if choice == 1:
        print("TODO list:")
        print_todos()
        print("==================")
        print()

    if choice == 2:
        add_todo()

    if choice == 3:
        print(choice)
        idx = int(input("Remove todo with index "))
        delete_todo_by_index(idx)
        print()
