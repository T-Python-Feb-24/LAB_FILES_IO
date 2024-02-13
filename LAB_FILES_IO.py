from typing import NoReturn


def add_note() -> NoReturn:

    note: str = input("Write your to-do item:\n")
    print(file_proccess(note, "w"))


def read_note() -> str:
    print("your to-do items is: ")
    print("".join(file_proccess()))


def file_proccess(note: str = "", rw="r") -> list[str] | str:
    try:
        with open("to_do.txt", "+a", encoding="utf-8") as todofile:
            todofile.seek(0)
            readlist: list[str] = todofile.readlines()
            match rw:
                case "w":
                    todofile.write(f"{len(readlist)+1}- {note}\n")
                    return "the note was written successfully"
                case "r":
                    return readlist

    except Exception as e:
        print(e)


def main() -> NoReturn:
    print("Welcome to to the to-do app\n\
==============================")

    while True:
        try:
            choice: str = input("Do you want to add a new To-Do item: ")
            match choice:
                case "y" | "Y":
                    add_note()
                case "n" | "N":
                    read_note()
                case _:
                    raise Exception(
                        "Please answer by \"y\" for yes and \"n\" for no")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
