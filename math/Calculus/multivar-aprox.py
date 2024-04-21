from sympy import pprint, diff, symbols, Matrix, parse_expr

def main():
    x, y, z, dx, dy, dz = symbols('x y z dx dy dz')
    function = parse_expr(input('Enter a function: '), transformations='all')
    pprint(function)
    
     # ask user for points to evaluate the function
    x_val = float(input("Enter the value of x: "))
    y_val = float(input("Enter the value of y: "))
    z_val = float(input("Enter the value of z: "))

    m1 = Matrix([[diff(function, x), diff(function, y), diff(function, z)]])
    m2 = Matrix([[dx, dy, dz]])

    # ask user for the values of dx, dy, dz
    dx_val = float(input("Enter the value of dx: "))
    dy_val = float(input("Enter the value of dy: "))
    dz_val = float(input("Enter the value of dz: "))

    m1 = m1.subs({x:x_val, y:y_val, z:z_val})
    m2 = m2.subs({dx:dx_val, dy:dy_val, dz:dz_val})
    ans = m1*m2.T
    pprint(ans)

if __name__ == "__main__":
    main()

