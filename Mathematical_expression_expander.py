from __future__ import division
#import sympy
from sympy import expand as expand
from sympy import symbols as symbols

def set_constants():
    x, y, z, t = symbols('x y z t')
    k, m, n = symbols('k m n', integer=True)
    f, g, h = symbols('f g h')
    
def get_expr():
    expr = ['(x+y)**2','(x-y)**2','(x**2)- (y**2)','(x-y)**3','(x-y)**5']
    return expr

def execute_expr():
    exp = get_expr()
    if len(exp) > 1:
        for a in exp:
            print (expand(a))
    else:
        print('Empty list of expressions')
        
if __name__ == '__main__':
    try:
        set_constants()
        execute_expr()
    except:
        print('Error in Execution')
        
        
'''
x**2 + 2*x*y + y**2
x**2 - 2*x*y + y**2
x**2 - y**2
x**3 - 3*x**2*y + 3*x*y**2 - y**3
x**5 - 5*x**4*y + 10*x**3*y**2 - 10*x**2*y**3 + 5*x*y**4 - y**5        
'''
