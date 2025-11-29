https://youtu.be/jJ5NKmwTbeo?si=XitBsOgsx3HO_Kae  - video on calculator creation
https://www.youtube.com/watch?v=ek47NMFW_mk - step by step guide video
https://www.youtube.com/watch?v=y8JRgQ0X1Lg&t=50s - mvc 




presentation
1. A technical approach explaining OOP terms like encapsulation
2. a practical scenario so pick a method in the controller and show how it relates and cuts across in the mvc

3.our model should contain the methods we used in there as a cycle and model sits in the middle
Model (CalculatorModel)
│
├── Data/State
│   ├── current_input : string/number
│   ├── previous_value : number
│   ├── selected_operator : string
│   ├── expression_history : list<string>
│   ├── 
│   ├── angle_mode : enum {DEG, RAD}
│   └── error_state : string/null
│
├── Expression Handling
│   ├── append_input(value)
│   ├── clear()
│   ├── backspace()
│   ├── handle_operator(op)
│   ├── evaluate_expression()
│   └── validate_expression()
│
├── Scientific Operations
│   ├── factorial(n)
│   ├── power(x, y)
│   ├── sqrt(x)
│   ├── trig_sin(x)
│   ├── trig_cos(x)
│   ├── trig_tan(x)
│   ├── log(x) / ln(x)
│   └── exp(x)
│
├── Mode Handling
│   ├── set_angle_mode()
│   ├── convert_angle_if_needed()
│
└── Memory Functions
    ├── memory_store(value)
    ├── memory_recall()
    ├── memory_clear()
    ├── memory_add(value)
    └── memory_subtract(value)
✅ 1. Number Handling
1. process_num(digit)

Handles typing numbers (0–9), appending digits, and starting new numbers.

✅ 2. Operators (+, −, ×, ÷)
2. process_operator(op)

Stores the current operator and prepares for the next number.

3. calculate()

Performs the math using last_op and updates the result.

✅ 3. Equal (=)
4. process_equal()

Completes the pending calculation and clears the last operator.

✅ 4. Clear Functions
5. clear()

Resets current value without wiping everything.

6. all_clear() (optional)

Resets the entire calculator:
current_value, total, last_op, and memory.

✅ 5. Memory Functions (M+, M-, MR, MC)
7. memory_add()

Adds the current value to memory (M+).

8. memory_subtract()

Subtracts current value from memory (M−).

9. memory_recall()

Displays memory value (MR).

10. memory_clear()

Clears memory (MC).

✅ 6. Scientific Functions
11. process_scientific(func)

Handles scientific keys such as:

"sin"

"cos"

"tan"

"sqrt"

"log"

"ln"

"exp"

"x^2"

"x^3"

"1/x"

"abs"

"pi"

"e"

(You’ll map the button name to the math function.)

✅ 7. Decimal Handling
12. process_decimal()

Adds a decimal point only if it doesn’t exist already.

✅ 8. Negation (+/− button)
13. toggle_sign()

Multiplies the number by −1.

✅ 9. Percentage
14. process_percent()

Converts current value into percentage (value / 100).

✅ 10. Parentheses (Optional)

If your calculator supports advanced expressions:

15. open_parenthesis()
16. close_parenthesis()

(These are optional and require expression parsing.)

✅ ✅ COMPLETE LIST (ALL METHODS TO IMPLEMENT)
Number Input

process_num(digit)

process_decimal()

Operators

process_operator(op)

calculate()

process_equal()

Scientific Functions

process_scientific(func)

toggle_sign()

process_percent()

Memory

memory_add()

memory_subtract()

memory_recall()

memory_clear()

Clear / Reset

clear()



all_clear() (optional)

Optional

open_parenthesis()

close_parenthesis()











































Title: Scientific Calculator README (MVC)
 

## Overview
This is a  Scientific Calculator implemented in Python, designed using the MVC (Model-View-Controller) architecture. It supports basic and advanced operations, including arithmetic, factorials, powers, roots, trigonometry, logarithms, and exponentials. The project separates concerns for maintainability and scalability.

---

## Features
- Basic arithmetic: `+`, `-`, `*`, `/`
- Scientific functions: factorial, power, square root, trigonometric functions (sin, cos, tan), logarithms (`log`, `ln`), exponentials
- Expression history tracking
- Error handling and validation
- Angle mode selection (Degrees / Radians)
- Clear and backspace functionality
- User-friendly GUI

---

 Project Structure

### Model (CalculatorModel)
Handles all **data, state, and calculations**.

#### Data/State
- `current_input` : string/number  
- `previous_value` : number  
- `selected_operator` : string  
- `expression_history` : list<string>  
- `angle_mode` : enum {DEG, RAD}  
- `error_state` : string/null  

#### Expression Handling
- `append_input(value)` : Add input to current expression  
- `clear()` : Clear current input and reset state  
- `backspace()` : Remove last character of current input  
- `handle_operator(op)` : Handle selected operator  
- `evaluate_expression()` : Compute result of expression  
- `validate_expression()` : Check expression for errors  

#### Scientific Operations
- `factorial(n)` : Compute factorial  
- `power(x, y)` : Compute x^y  
- `sqrt(x)` : Compute square root  
- `trig_sin(x)` : Compute sine (based on angle mode)  
- `trig_cos(x)` : Compute cosine  
- `trig_tan(x)` : Compute tangent  
- `log(x)` / `ln(x)` : Compute logarithms  
- `exp(x)` : Compute exponential  

---

### View (CalculatorView)
Handles **user interface** and **display**.

#### Components
- GUI window with numeric buttons, operators, and scientific function buttons  
- Display for current input and previous calculation  
- Mode selection for DEG/RAD  
- Buttons for clear, backspace, and history viewing  

#### Responsibilities
- Render calculator layout  
- Update display on input or result  
- Pass user interactions to Controller  

---

### Controller (CalculatorController)
Handles **logic and interaction** between View and Model.

#### Responsibilities
- Capture user input from View  
- Update Model state (append input, evaluate expression, handle operator)  
- Handle errors and validation  
- Update View with results or error messages  
- Manage expression history and angle mode changes  

---

## Installation
1. Ensure Python 3.x is installed.  
2. Clone the repository:
```bash
git clone <repository_url>
```
3. Navigate to the project folder:
```bash
cd scientific-calculator
```
4. Install any dependencies (Tkinter is usually included with Python).

---

## Usage
1. Run the calculator:
```bash
python main.py
```
2. Use buttons to input numbers, operators, and scientific functions.  
3. Press `=` to compute results.  
4. Use `C` to clear, and `←` to backspace.  
5. Switch between DEG and RAD for trigonometric functions as needed.

---

## Contributing
- Fork the repository.  
- Create a feature branch:
```bash
git checkout -b feature-branch
```
- Commit changes:
```bash
git commit -m "Add feature"
```
- Push branch:
```bash
git push origin feature-branch
```
- Open a pull request.

---

## License
[MIT License](LICENSE)

---

This README provides a clear MVC-based overview of your Scientific Calculator, explaining the roles of Model, View, and Controller along with usage instructions and scientific operations.
