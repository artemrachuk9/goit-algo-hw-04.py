# first hometsk
def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            line = file.read().strip()
            parts = line.split(' ')
            salaries = []
            for pair in parts:
                try:
                    name, salary_str = pair.split(',')
                    salary = float(salary_str)
                    salaries.append(salary)
                except ValueError:
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

# 🧠 ВИКЛИКАЄМО ФУНКЦІЮ
total, average = total_salary("salary_inline.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


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