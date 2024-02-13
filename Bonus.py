from datetime import datetime
import json


def add_to_do_item(to_do_list):
    while True:
        todo_dict: dict = {
            "Title": input("Enter the title of the item: "),
            "date": str(datetime.today().strftime("%Y-%m-%d %H:%M:%S")),
            "Done": False,
        }

        is_done = input("is it done?[y if it done] default (not done): ")
        match is_done:
            case "Y" | "y":
                todo_dict["Done"] = True
                break
            case "":
                break
            case _:
                print(
                    "\033[31mPlease enter y if it is done or keep it blank to not done\033[m")
                continue

    if not isExist(to_do_list, todo_dict):
        to_do_list.append(todo_dict)
        print("Your new To-Do item has been added successfully.")


def isExist(to_do_list: list[dict], todo_dict) -> bool:
    for item in to_do_list:
        if todo_dict["Title"] == item["Title"]:
            item.update(todo_dict)
            print("Your To-Do item has been updated successfully.")
            return True
    return False


def list_to_do_items(to_do_list):
    for index, item in enumerate(to_do_list):
        print(f"{index + 1}- {item['Title']} \
- {item['date']} - {"Done" if item['Done'] else "Not Done"}")


def save_to_do_list(to_do_list):
    with open("to_do.json", "w") as file:
        json.dump(to_do_list, file, indent=4)


def load_to_do_list() -> list[dict]:
    try:
        with open("to_do.json", "r") as file:
            return list(json.load(file))
    except FileNotFoundError:
        return []


def main() -> None:
    print("Welcome to to the to-do app\n\
==============================")

    while True:
        try:
            to_do_list: list[dict] = load_to_do_list()
            print("your to-do list is:")
            for i, item in enumerate(to_do_list, 1):
                print(f"{i}- {item["Title"]}")
            choice: str = input(
                "Do you want to add a new To-Do or update item:(y|n) ")
            match choice:
                case "y" | "Y":
                    add_to_do_item(to_do_list)
                    save_to_do_list(to_do_list)

                case "n" | "N":
                    list_to_do_items(to_do_list)
                    break

                case _:
                    raise Exception(
                        "\033[31mPlease answer by \"y\" for yes and \"n\" for no\033[m")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
