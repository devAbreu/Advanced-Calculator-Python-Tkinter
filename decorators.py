from datetime import datetime
from functools import wraps

# List to keep track of operation history
operation_history = []

def log_operation(func):
    """
    Decorator to log the execution and result of an operation.

    Parameters:
    - func: The function being decorated.

    Returns:
    - Callable: A wrapped version of the original function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function to be executed when the decorated function is called.

        Returns:
        - Any: The result returned by the decorated function.
        """
        result = func(*args, **kwargs)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        operation_history.append(f"{timestamp} - {func.__name__} - Result: {result}")
        return result

    return wrapper
