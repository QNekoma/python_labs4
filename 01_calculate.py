def repeat(num_repeats):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(num_repeats):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)  # Указываем, что функцию нужно запустить 3 раза
def example_function(parameter):
    return parameter ** 2

result = example_function(5)
print(result)  # Выведет: [25, 25, 25]
