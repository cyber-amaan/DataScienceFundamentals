def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
kwargsAcceptFun(name="Alice", age=30, city="New York")