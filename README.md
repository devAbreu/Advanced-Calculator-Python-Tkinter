# Advanced Calculator

## Overview
The Advanced Calculator is a desktop application built using Python and Tkinter for the GUI. It allows users to perform various calculations including basic arithmetic operations, list-based operations like sum, product, and average, and it also has a feature to run parallel computations. The application also includes features like operation logging and history display.

## Features

### Arithmetic Operations
- Addition
- Subtraction
- Multiplication
- Division

### List Operations
- Sum
- Product
- Average

### Parallel Computations
- Execute multiple operations concurrently

### Logging and History
- Logs each operation
- Displays a history of all executed operations

## Installation
To run this project, clone the repository and run `main.py`:
```bash
git clone https://github.com/devAbreu/Advanced-Calculator-Python-Tkinter
cd advanced-calculator
python main.py
```

## How to Use
### Basic Arithmetic Operations
1. Open the app.
2. Enter the two operands in the operand input fields.
3. Click on the button corresponding to the operation you wish to perform (Add, Subtract, Multiply, Divide).

### Example
- Input Operand 1: `5`
- Input Operand 2: `10`
- Click on "Add" to get `15`

### List Operations
1. Open the app.
2. Navigate to the list operations section.
3. Enter the numbers separated by commas.
4. Click the "List Operations" button.

### Example
- Input List: `5,10,15`
- Click on "List Operations" to get:
  - Sum: `30`
  - Product: `750`
  - Average: `10`

### Parallel Computations
1. Open the app.
2. Enter the two operands in the operand input fields.
3. Click on the "Run Parallel" button to perform all basic arithmetic operations at once.

### Example
- Input Operand 1: `12`
- Input Operand 2: `4`
- Click "Run Parallel" to get:
  - Add: `16`
  - Subtract: `8`
  - Multiply: `48`
  - Divide: `3`

### History
To view the operation history, click the "Show History" button.

## Technologies Used
- Python
- Tkinter for GUI
- Threading for parallel computations
- Decorators for logging

## Future Enhancements

### Scientific Calculator Functions
Extend the calculator to support scientific calculations like trigonometric functions (sine, cosine, tangent), exponential and logarithmic functions.

### User Profiles
Implement user profiles where each user can save their own calculation history and preferences.

### Real-Time Collaboration
Allow multiple users to collaborate in real-time, enabling them to share calculations and results instantly.

### Keyboard Shortcuts
Add keyboard shortcuts for frequent operations to speed up usage.

### Expression Parsing
Allow the user to input a full mathematical expression, which the calculator would parse and evaluate.

### Dark Mode
Implement a dark mode to reduce eye strain during prolonged use.

### Offline Support
Enable the calculator to work offline, saving any logs or history locally to be synced once back online.

### Mobile Application
Create a mobile version of the application for Android and iOS to reach a wider audience.

### Advanced Graphing Capabilities
Introduce functionalities to graph equations and visualize data.

### Cloud Syncing
Allow users to sync their calculation history and preferences to the cloud, making it accessible from any device.

## Contributors
- [devAbreu](https://github.com/devAbreu)

## License
This project is licensed under the MIT License.

---