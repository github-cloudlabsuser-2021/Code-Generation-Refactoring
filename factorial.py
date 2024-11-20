def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
    It is denoted by n! and defined as:
    - 0! = 1
    - n! = n * (n-1) * (n-2) * ... * 1 for n > 0

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.

    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

choice = int(input("Enter a number to calculate its factorial: "))
if choice < 0:
    print("Please enter a non-negative integer")
else:
    print(f"The factorial of {choice} is {factorial(choice)}")