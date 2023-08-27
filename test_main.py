import tkinter as tk
from tkinter import ttk
from unittest.mock import patch
from main import perform_and_show, perform_list_operations, perform_parallel_operations

@patch('main.result_label')
def test_perform_and_show(mock_result_label):
    perform_and_show("dummy_op")
    mock_result_label.config.assert_called_once()

@patch('main.list_result_label')
@patch('main.list_entry')
def test_perform_list_operations(mock_list_entry, mock_list_result_label):
    mock_list_entry.get.return_value = "1, 2, 3"
    perform_list_operations()
    mock_list_result_label.config.assert_called_once()

@patch('main.parallel_result_label')
@patch('main.operand1_entry')
@patch('main.operand2_entry')
def test_perform_parallel_operations(mock_operand2_entry, mock_operand1_entry, mock_parallel_result_label):
    mock_operand1_entry.get.return_value = "5"
    mock_operand2_entry.get.return_value = "2"
    perform_parallel_operations()
    mock_parallel_result_label.config.assert_called_once()
