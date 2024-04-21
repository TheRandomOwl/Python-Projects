from sympy import pprint, diff, solve, parse_expr, im

def second_derivative_test(points,fxx,fyy,fxy,f):
    if len(points) == 0:
        print("There are no critical points.")
        return
    for ans in points:
        fxx_val = fxx.subs(ans)
        fyy_val = fyy.subs(ans)
        fxy_val = fxy.subs(ans)

        determinant = fxx_val * fyy_val - fxy_val ** 2
        # check if the answer complex and skip if it is
        if im(determinant).evalf() != 0 or fxx_val.is_real == False or fyy_val.is_real == False or fxy_val.is_real == False:
            continue

        if determinant > 0 and fxx_val > 0 and fyy_val > 0:
            print(f"Local minimum with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":f.subs(ans)})
        elif determinant > 0 and fxx_val < 0 and fyy_val < 0:
            print(f"Local maximum with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":f.subs(ans)})
        elif determinant < 0:
            print(f"Saddle point with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":f.subs(ans)})
        elif determinant == 0:
            print(f"Indeterminate with determinant {determinant}:")
            pprint(ans)
            pprint({"f(x,y)":f.subs(ans)})

def print_partial_derivatives(fx,fy,fxx,fyy,fxy):
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

def main():
    while True:
        try:
            ## Ask user if input is correct and check if the input is valid
            while True:
                function = parse_expr(input('Enter a function: '), transformations='all')
                if function != None:
                    print("Is this the function you want to use?:")
                    pprint(function)
                    ans = input("Enter 'y' or 'n': ").lower()
                    if ans == 'y':
                        break
            break
        except KeyboardInterrupt:
            print("Quit")
            return
        except:
            print("Invalid input. Please try again.")

    # calculate the first and second partial derivatives
    fx = diff(function, "x")
    fxx = diff(function, "x", "x")
    fy = diff(function, "y")
    fyy = diff(function, "y", "y")
    fxy = diff(function, "x", "y")
    print_partial_derivatives(fx,fy,fxx,fyy,fxy)

    try:
        # calculate the critical points
        critical_points = solve([fx, fy], ["x", "y"], dict=True)
    except:
        print("Could not solve for critical points.")
        return
    
    second_derivative_test(critical_points,fxx,fyy,fxy,function)

if __name__ == '__main__':
    main()