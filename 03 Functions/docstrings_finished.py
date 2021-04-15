# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything special.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: the second argument. Defaults to None. Whatever makes you happy.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
