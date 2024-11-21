from division import division
from mutiplication import multiplication
from addition import add_two_numbers
from subtraction import sub_two_numbers


def main():
    x = division(10,2)
    print(x)
    y = multiplication(5,2)
    print(y)
    add_two_numbers(4,7)
    sub_two_numbers(9,7)

if __name__ == "__main__":
    main()
