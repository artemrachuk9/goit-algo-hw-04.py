def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, salary_str = line.split(',')
                    salary = float(salary_str)
                    salaries.append(salary)
                except ValueError:
                    print(f"Некоректний запис у файлі: {line}")
                    continue
            if not salaries:
                return (0, 0)
            total = sum(salaries)
            average = total / len(salaries)
            return (total, average)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)
total, average = total_salary("salary_inline.txt")
print(f"Загальна сума: {total}, Середня зарплата: {average}")


# second hometsk
def get_cats_info(path):
    cats = []
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats.append(cat_dict)
        return cats
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f" Сталася помилка при обробці файлу: {e}")
        return []

# 👇 Виклик функції та виведення результату
cats_info = get_cats_info("cats.txt")
print(cats_info)



# third hometak 
def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please use format: add username phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please use format: change username phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Please use format: phone username"
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = ["Contacts list:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("👋 Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
