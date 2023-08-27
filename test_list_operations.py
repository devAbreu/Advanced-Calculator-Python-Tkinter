from list_operations import sum_list, product_list, average_list

def test_sum_list():
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    assert result == 15

def test_product_list():
    numbers = [2, 3, 4]
    result = product_list(numbers)
    assert result == 24

def test_average_list():
    numbers = [10, 20, 30]
    result = average_list(numbers)
    assert result == 20
