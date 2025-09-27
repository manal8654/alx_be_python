def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations between two numbers.

    Args:
        num1: First number
        num2: Second number
        operation: Operation type ('add', 'subtract', 'multiply', 'divide')

    Returns:
        float or str: Result of the arithmetic operation, or error message
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
