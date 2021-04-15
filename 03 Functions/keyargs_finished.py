# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    # try to call the function without the keyword
    #myFunction(1, 2, True)
    myFunction(1, 2, suppressExceptions=True)
    myFunction(1, 2)

if __name__ == "__main__":
    main()
