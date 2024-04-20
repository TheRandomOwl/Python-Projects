from sympy import *

x, y = symbols('x,y')
function = parse_expr(input('Enter a function: '), transformations='all')
pprint(function)

# calculate the first and second partial derivatives
fx = diff(function, x)
fxx = diff(function, x, x)
fy = diff(function, y)
fyy = diff(function, y, y)
fxy = diff(function, x, y)

def second_derivative_test(points):
    for ans in points:
        fxx_val = fxx.subs(ans)
        fyy_val = fyy.subs(ans)
        fxy_val = fxy.subs(ans)

        determinant = fxx_val * fyy_val - fxy_val ** 2

        if determinant > 0 and fxx_val > 0 and fyy_val > 0:
            print(f"Local minimum at {ans} with determinant {determinant}")
            pprint(ans)
            #print(f"f({point[0]},{point[1]}) = {function.subs(ans)}")
        elif determinant > 0 and fxx_val < 0 and fyy_val < 0:
            print(f"Local maximum at {ans} with determinant {determinant}")
            pprint(ans)
            #print(f"f({point[0]},{point[1]}) = {function.subs(ans)}")
        elif determinant < 0:
            print(f"Saddle point at {ans} with determinant {determinant}")
            pprint(ans)
            #print(f"f({point[0]},{point[1]}) = {function.subs(ans)}")
        elif determinant == 0:
            print(f"Indeterminate at {ans} with determinant {determinant}")
            pprint(ans)

def print_partial_derivatives(f):
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

print_partial_derivatives(function)

critical_points = solve([fx, fy], [x, y], dict=True)
print(type(critical_points))
print(critical_points)
if len(critical_points) > 0:
    second_derivative_test(critical_points)
else:
    print("There are no critical points")
