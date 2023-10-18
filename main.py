import math

# Історія обчислень
history = []

# Функція пам'яті
memory = None

# Кількість десяткових розрядів
decimal_places = 2

def get_user_input():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")

        return num1, num2, operator
    except ValueError:
        print("Помилка: Введено недійсне число.")
        return None, None, None

def check_operator(operator):
    valid_operators = ['+', '-', '*', '/', '^', '√', '%']
    if operator not in valid_operators:
        print("Помилка: Введено недійсний оператор.")
        return False
    return True

def calculate_result(num1, num2, operator):
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Помилка: Ділення на нуль.")
                return None
            result = num1 / num2
        elif operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = math.sqrt(num1)
        elif operator == '%':
            result = num1 % num2
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

    history.append((num1, num2, operator, result))
    return result

def set_decimal_places():
    global decimal_places
    try:
        decimal_places = int(input("Введіть кількість десяткових розрядів для відображення: "))
    except ValueError:
        print("Помилка: Введено недійсне число.")

def main():
    while True:
        num1, num2, operator = get_user_input()

        if num1 is not None and num2 is not None and operator is not None:
            if check_operator(operator):
                result = calculate_result(num1, num2, operator)
                if result is not None:
                    formatted_result = round(result, decimal_places)
                    print(f"Результат: {formatted_result}")

        another_calculation = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
        if another_calculation.lower() != 'так':
            break

    # Історія обчислень
    print("Історія обчислень:")
    for item in history:
        num1, num2, operator, result = item
        formatted_result = round(result, decimal_places)
        print(f"{num1} {operator} {num2} = {formatted_result}")

if __name__ == "__main__":
    while True:
        print("Меню налаштувань:")
        print("1. Змінити кількість десяткових розрядів")
        print("2. Завершити налаштування")
        choice = input("Виберіть опцію: ")

        if choice == '1':
            set_decimal_places()
        elif choice == '2':
            break

    main()
