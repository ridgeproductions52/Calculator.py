# 🧮 Ridge Production's Calculator

Welcome to **Ridge Production's Calculator**, a versatile command-line tool designed to handle a wide range of mathematical and physics-related computations. Built with Python, this calculator leverages powerful libraries like `math`, `sympy`, and a custom `physic.py` module to provide an interactive experience for solving equations, converting units, and more.

---

## 🚀 Features

This calculator offers six core tools:

| Tool # | Description                     | Functionality                                                                 |
|--------|---------------------------------|--------------------------------------------------------------------------------|
| 1️⃣     | Basic Arithmetic Solver         | Parses and evaluates arithmetic, trigonometric, logarithmic, and exponential expressions. |
| 2️⃣     | System of Equations Solver     | Solves systems of equations using symbolic algebra.                           |
| 3️⃣     | Degree-Radian Converter        | Converts between degrees and radians.                                         |
| 4️⃣     | Factorial Tool                 | Computes factorials of non-negative integers.                                 |
| 5️⃣     | Algebraic Equation Solver      | Solves single-variable algebraic equations.                                   |
| 6️⃣     | ~~Physics Toolset~~            | Runs physics-related computations via `physic.py`. (Release Date: 11/01/2025  |

---

## 🧠 How It Works

Upon running the script, you'll be greeted with a menu of tools. Simply enter the number corresponding to the tool you'd like to use, and follow the prompts.

### Example: Basic Arithmetic Solver

What equation would you like to evaluate?  
> sin(0.5) + log(10)  
Evaluation Results:  
sin(0.5) + log(10) 1.479425538604203  

### Example: Factorial Tool

What number would you like to find the factorials of?  
> 5  
120  

---

## 🛠️ Dependencies

Make sure you have the following Python packages installed:

- `math` (standard library) — https://docs.python.org/3/library/math.html
- `sympy` — https://docs.sympy.org/latest/modules/solvers/solvers.html
- `ast` (standard library) — https://docs.python.org/3/library/ast.html
~~- `physic.py` — Custom module for physics computations~~

Install SymPy if needed:

pip install sympy

---

## 📦 File Structure

calculator.py       # Main script with all tools  
~~physic.py           # Physics toolbox (must be present in the same directory)~~

---

## 🧪 Usage

Run the script from the terminal:

python calculator.py

Follow the prompts to select a tool and input your expressions or values.

---

## 📄 License

This project is open-source and free to use. Attribution to Ridge Production is appreciated.

---

## 🙌 Credits

Developed by Ridge Production. Uses Python's built-in and third-party libraries to deliver a robust CLI calculator experience.
