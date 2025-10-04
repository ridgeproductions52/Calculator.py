import math     # Imports math module found at -> https://docs.python.org/3/library/math.html

from sympy import solve 
from sympy.parsing.sympy_parser import parse_expr
from sympy.solvers import solve      # Imports Sympy Solver module found -> https://docs.sympy.org/latest/modules/solvers/solvers.html#sympy.solvers.solvers.solve
from sympy.abc import x, y, z, a, b, c
from sympy import *

import ast # Python Abstract Syntax Tree found at -> https://docs.python.org/3/library/ast.html

import physic # Imports physics.py, used to run the physics toolbox to avoid overcrowding and complicating calculator.py


# Complex Parser, solves and handles arithmetic, trigonometric, logarithms, exponentials, etc.
def mainParser():
    class MathExpressionEvaluator:  # Define a class for evaluating mathematical expressions
        def __init__(self):
            pass

        # Method to evaluate mathematical expressions
        def evaluate(self, expression):
            try:
                # Parse the expression into an Abstract Syntax Tree (AST)
                parsed_expression = ast.parse(expression, mode='eval')

                # Define the allowed names (functions and constants) for evaluation
                allowed_names = {
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                    'log': math.log,
                    'sqrt': math.sqrt,
                    **vars(math)  # Include all functions and constants from the math module
                }

                # Evaluate the AST using a custom namespace that includes the allowed names
                result = eval(compile(parsed_expression, filename='', mode='eval'), {}, allowed_names)
                return result
            except SyntaxError:
                print("Invalid expression syntax.")
                return None
            except Exception as e:
                print("Error:", e)
                return None
    # Take user input and parse out into print
    if __name__ == "__main__":
        evaluator = MathExpressionEvaluator()

        expr = input("What equation would you like to evaluate?")

        # Evaluate mathematical expressions
        print("Evaluation Results:")
        print(expr, evaluator.evaluate(expr))


# Factorial Tool, gives us factorial of a non-negative integer, n. Floats are no longer accepted(i.e. 5.0)
def factorialtool():
    while True:
        try:
            factnumber = int(input("What number would you like to find the factorials of?"))
            result = math.factorial(factnumber)
            print(result)
        except ValueError:
            print("Not an integer! Please provide a valid integer.")        # If input is not a valid integer then it will throw error and ask for new valid integer
            continue
        else:
            break


# Degree-Radian Tool, converts degrees to radians and same vice versa
def degreeradconvert():
    while True:
        try:
            conopt = ['1. Degree to Radian','2. Radian to Degree']
            print('\n'.join(conopt))
            convert = input("Which way would you like to convert? ")
            if convert == "1":
                degree = float(input("What degree would you like to convert to radians? "))
                result = math.radians(degree)
                print(result)

            if convert == "2":
                radian = float(input("What radian would you like to convert to degrees? Please only put value of radian"))
                result = math.degrees(radian)
                print(result)

        except ValueError: # Checks to verify that the integer provided is actually a valid integer and throws error if not
            print("Not a valid number! Please enter valid degree/radian")
            continue

        else:
            break


# System of Equations Solver, solves system of equations and returns each variable's value
def systemEquationsSolve():
    exprs = input("What expression(s) do you want to solve?  ")
    exprs = [parse_expr(e, evaluate=False) for e in exprs.split(",")]

    solve_for = input("What variables do you want to solve for?  ")
    solve_for = [parse_expr(e, evaluate=False) for e in solve_for.split(",")]

    result = solve(exprs, solve_for, dict=True)
    print("Solution:")
    print("\n".join([f"{var} = {value}" for var, value in result.items()]))


# Algebraic Equation Solver, solves equations algebraically 
def algeq_solve():
    equation_str = (input("What expression would you like to solve? Please enter one equation at a time.\n"))
    variable_str = (input("What variable would you like to solve for? Please select one.\n"))

    lhs_str, rhs_str = equation_str.split("=")

    lhs = parse_expr(lhs_str)
    rhs = parse_expr(rhs_str)

    expr = simplify(rhs - lhs)
    solved = solve(expr, variable_str, dict=False)
    print(solved[0])



# For each tool, provide its keystroke/number, then the details about each tool.
# Each tool needs a description and function to call.
tooloptions = {
    "1": {
        "description": "Basic Arithmetic Solver",
        "func": mainParser,
    },
    "2": {
        "description": "System of Equations Solver",
        "func": systemEquationsSolve,
    },
    "3": {
        "description": "Degree-Radian Converter",
        "func": degreeradconvert,
    },
    "4": {
        "description": "Factorial Tool",
        "func": factorialtool,
    },
    "5": {
        "description": "Algebraic Equation Solver",
        "func": algeq_solve,
    },
    "6": {
        "description": "Physics Toolset",
        "func": physic.main, 
    }
}

try:
    print("Hello! Welcome to Ridge Production's Calculator.\n")       # Welcome message

    # Grab code and description for each tool to print using list comprehension over dict items
    for key, item in tooloptions.items():
        print(f"{key}. {item['description']}")

    opentool = input("\nWhat tool would you like to use: ")

    # Check which tool user selected and run function associated with requested tool
    item = tooloptions.get(opentool)
    if item:
        item['func']()
    else:
        print("Invalid tool.  Try again.\n\n")
except KeyboardInterrupt:
    pass
