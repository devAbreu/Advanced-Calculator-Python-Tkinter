from functools import reduce

def sum_list(numbers):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - numbers: List of numbers to sum.

    Returns:
    - int or float: The sum of all the numbers in the list.
    """
    return reduce(lambda x, y: x + y, numbers)

def product_list(numbers):
    """
    Calculate the product of a list of numbers.

    Parameters:
    - numbers: List of numbers to multiply.

    Returns:
    - int or float: The product of all the numbers in the list.
    """
    return reduce(lambda x, y: x * y, numbers)

def average_list(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
    - numbers: List of numbers to average.

    Returns:
    - float: The average of all the numbers in the list, or 0 if the list is empty.
    """
    total = sum_list(numbers)
    return total / len(numbers) if len(numbers) > 0 else 0

