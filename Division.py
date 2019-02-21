# Thomas maioli
# coded in Python
# date 2019-02-08
# Project name: Division
# Issues and concerns: Problem domain "division"


def divide(num, den):
    i = num // den
    r = num % den
    print(num, "Divided by",den, "equals", i, "with a remainder of", r)


def main():
    numerator = float(input("Enter the numerator "))
    denominator = float(input("Enter the Denominator  "))
    divide(numerator,denominator)

main()
