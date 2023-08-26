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

### Installation
To use this Advanced Calculator, follow these steps:

1. Clone the repository to your local machine:
```bash
git clone https://github.com/devAbreu/Advanced-Calculator-Python-Tkinter.git
cd Advanced-Calculator-Python-Tkinter
```

## Setting Up a Virtual Environment (Optional but Recommended)

It's a good practice to work within a virtual environment to manage project dependencies. Here's how you can set up a virtual environment using Python's built-in `venv` module:

1. Open a terminal and navigate to the project directory.

2. Create a new virtual environment using the `venv` module. Replace `<env_name>` with the desired name for your virtual environment:
```bash
   python3.11 -m venv <env_name>
```
### Activate the virtual environment
On macOS and Linux:
```bash
source <env_name>/bin/activate
```
On Windows:
```bash
.\<env_name>\Scripts\activate
```
Once the virtual environment is activated, you can install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
To deactivate the virtual environment, simply run:
```bash
deactivate
```
Using a virtual environment helps isolate project-specific dependencies and prevents conflicts with other Python projects you might be working on. It's recommended but entirely optional.


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