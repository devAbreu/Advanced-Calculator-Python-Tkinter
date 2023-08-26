from concurrent.futures import ThreadPoolExecutor

def execute_operations(operations):
    """
    Execute a list of calculator operations concurrently.

    Parameters:
    - operations: A list of Calculator objects with operations to perform.

    Returns:
    - list: A list of results corresponding to each operation.
    """
    results = []
    # Using ThreadPoolExecutor to perform operations concurrently
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda op: op.perform_operation(), operations))
    return results
