from sympy import *

x, y = symbols('x,y')
while True:
    try:
        function = parse_expr(input('Enter a function: '), transformations='all')
        pprint(function)

        # calculate the first and second partial derivatives
        fx = diff(function, x)
        fxx = diff(function, x, x)
        fy = diff(function, y)
        fyy = diff(function, y, y)
        fxy = diff(function, x, y)
        break
    except:
        print("Invalid input. Please try again.")

def second_derivative_test(points):
    if len(points) == 0:
        print("There are no critical points.")
        return
    for ans in points:
        fxx_val = fxx.subs(ans)
        fyy_val = fyy.subs(ans)
        fxy_val = fxy.subs(ans)

        determinant = fxx_val * fyy_val - fxy_val ** 2
        # check if the determinant is not complex
        if im(determinant).evalf() != 0:
            continue

        if determinant > 0 and fxx_val > 0 and fyy_val > 0:
            print(f"Local minimum with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":function.subs(ans)})
        elif determinant > 0 and fxx_val < 0 and fyy_val < 0:
            print(f"Local maximum with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":function.subs(ans)})
        elif determinant < 0:
            print(f"Saddle point with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":function.subs(ans)})
        elif determinant == 0:
            print(f"Indeterminate with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":function.subs(ans)})

def print_partial_derivatives():
    # print the first and second partial derivatives
    print("First partial derivative with respect to x:")
    pprint(fx)

    print("First partial derivative with respect to y:")
    pprint(fy)

    print("Second partial derivative with respect to x:")
    pprint(fxx)

    print("Second partial derivative with respect to y:")
    pprint(fyy)

    print("Mixed partial derivative with respect to x and y:")
    pprint(fxy)

print_partial_derivatives()

critical_points = solve([fx, fy], [x, y], dict=True)

second_derivative_test(critical_points)