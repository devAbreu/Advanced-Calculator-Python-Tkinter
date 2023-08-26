from abc import ABC, abstractmethod
from decorators import log_operation

# IOperation serves as an interface for operations that can be performed
# by a calculator.
class IOperation(ABC):

    @abstractmethod
    def perform_operation(self):
        """Perform the operation."""
        pass

    @abstractmethod
    def display_result(self):
        """Display the result of the operation."""
        pass

# Calculator serves as a base class for arithmetic operations.
class Calculator(IOperation):

    def __init__(self, operand1, operand2):
        """
        Initialize Calculator with two operands.

        Parameters:
        - operand1: The first operand for the operation.
        - operand2: The second operand for the operation.
        """
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = None

    def perform_operation(self):
        """Perform the operation (to be implemented by subclass)."""
        pass

    def display_result(self):
        """
        Display the result of the operation.

        Returns:
        - str: A formatted string showing the result.
        """
        print(self.result)
        if self.result.is_integer():
            return f"Result: {int(self.result)}"
        else:
            return f"Result: {self.result}"


# Add performs addition of two operands.
class Add(Calculator):

    @log_operation
    def perform_operation(self):
        """Perform addition and return the result."""
        self.result = round(self.operand1 + self.operand2, 2)
        return self.result


# Subtract performs subtraction of two operands.
class Subtract(Calculator):

    @log_operation
    def perform_operation(self):
        """Perform subtraction and return the result."""
        self.result = round(self.operand1 - self.operand2, 2)
        return self.result


# Multiply performs multiplication of two operands.
class Multiply(Calculator):

    @log_operation
    def perform_operation(self):
        """Perform multiplication and return the result."""
        self.result = round(self.operand1 * self.operand2, 2)
        return self.result


# Divide performs division of two operands.
class Divide(Calculator):

    @log_operation
    def perform_operation(self):
        """
        Perform division and return the result.

        Returns:
        - float or str: The result of the division or an error message.
        """
        try:
            self.result = round(self.operand1 / self.operand2, 2)
            return self.result
        except ZeroDivisionError:
            return "Cannot divide by zero"
