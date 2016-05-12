from MainController import MainController
from sympy.simplify.cse_main import cse


__author__ = 'Milena'

def main():



    main_controller = MainController()
    while True:
        if not main_controller.start():
            break

    #[['x1', 'x2', 'x3'],['x4', 'x5', 'x6', 'x7']]

    #from sympy.abc import a, b, c, d, e, f, g ,h ,i, j, k, l, m, n
    #cse([(f & g | a & b | d & e),(a & b & c | f & e | f & g | d & e)], optimizations='basic')
    #cse([(y & x ),(x & y | z)])[0][0][1]


    #((a & b | f | g & e).has(a & b | l & e))  !!!!
    #simplify_logic(f & g | l & e | d & e |a & b & c | f & e | l & e, True) !!!!


if __name__ == "__main__":
    main()
