import math

def secant_main():
    # Get the function from the user
    f_of_x = input("Enter the function: ")

    # Notations for compatibility for both polynomial and transcendental functions
    f_of_x = f_of_x.replace(" ", "")    
    f_of_x = f_of_x.replace('^', '**')
    f_of_x = f_of_x.replace('e', 'math.e')
    f_of_x = f_of_x.replace('exp', 'math.exp')
    f_of_x = f_of_x.replace('sqrt', 'math.sqrt')
    f_of_x = f_of_x.replace('ln', 'math.log')
    f_of_x = f_of_x.replace('log', 'math.log10')
    f_of_x = f_of_x.replace('sin', 'math.sin')
    f_of_x = f_of_x.replace('cos', 'math.cos')
    f_of_x = f_of_x.replace('tan', 'math.tan')
    f_of_x = f_of_x.replace('csc', '1/math.sin')
    f_of_x = f_of_x.replace('sec', '1/math.cos')
    f_of_x = f_of_x.replace('cot', '1/math.tan')

    # Define the lambda function
    function = lambda x: eval(f_of_x, {'x': x, 'math': math, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'log': math.log, 'log10': math.log10, 'e': math.e, 'exp': math.exp, 'csc': lambda x: 1/math.sin(x), 'sec': lambda x: 1/math.cos(x), 'cot': lambda x: 1/math.tan(x)})

    # Get initial values, absolute error, and decimal places
    x0 = float(input("Enter the initial value x0: "))
    x1 = float(input("Enter the initial value x1: "))
    ea = float(input("Enter the absolute error: "))
    dp = int(input("Enter the number of decimal places for rounding: "))

    def secant_method(function, x0, x1, ea, dp, max_iterations=1000):
        print("\nTabulated Results:")
        print(f"{'Iter':<5} | {'x0':<10} | {'x1':<10} | {'x2':<10} | {'f(x0)':<13} | {'f(x1)':<13} | {'f(x2)':<13} | {'Ea':<10}")
        print("-" * 105)

        iterations = 1
        while iterations < max_iterations:
            fx0 = function(x0)
            fx1 = function(x1)

            x2 = x0 - (fx0 * ((x1 - x0) / (fx1 - fx0)))
            fx2 = function(x2)

            absolute_error = abs(x2 - x1)

            print("{:<5} | {:<10.{dp}f} | {:<10.{dp}f} | {:<10.{dp}f} | {:<13.{dp}f} | {:<13.{dp}f} | {:<13.{dp}f} | {:<10.{dp}f}".format(iterations, custom_round(x0, dp), custom_round(x1, dp), custom_round(x2, dp), custom_round(fx0, dp), custom_round(fx1, dp), custom_round(fx2, dp), custom_round(absolute_error, dp), dp=dp))

            if fx2 == 0 or absolute_error < ea:
                return x2, iterations

            x0, x1 = x1, x2
            iterations += 1

        print("Maximum iterations reached. The method may not have converged.")
        return None

    def custom_round(value, dp):
        # Rounding to the specified number of decimal places
        return round(value, dp)

    # Perform Secant Method
    result = secant_method(function, x0, x1, ea, dp)

    # Display the result
    if result:
        root, iterations = result
        print("\nRoot:", custom_round(root, dp))
        print("\nIterations:", iterations)
        print("\n")
    else:
        print("Unable to find the root within the given tolerance.")
          
if __name__ == "__main__":
    secant_main()
