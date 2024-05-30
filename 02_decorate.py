def make_calc():
    initial = float(input("Введите начальное значение: "))
    result = initial

    while True:
        operation = input("Введите операцию (+, -, *, /) или 'exit' для выхода: ")
        if operation == "exit":
            break

        num = float(input("Введите число: "))
        if operation == "+":
            result += num
        elif operation == "-":
            result -= num
        elif operation == "*":
            result *= num
        elif operation == "/":
            if num != 0:
                result /= num
            else:
                print("Error: division by zero")
        else:
            print("Error: unsupported operation")

        print(f"Результат: {result}")


make_calc()
