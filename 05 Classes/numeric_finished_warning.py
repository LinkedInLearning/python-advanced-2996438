# give objects number-like behavior


class Int():
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "x:{0}".format(self.x)

    # implement addition
    def __add__(self, other):
        return Int(self.x + 2 * other.x)


def main():
    x = Int(10)
    y = Int(5)
    print("Wert von x:", x, "Wert von y", y)

    erg = x + y
    print("Wert von x + y:", erg)
  

if __name__ == "__main__":
    main()
