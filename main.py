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