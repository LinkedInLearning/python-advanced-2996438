# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and German
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysGer = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # iterate using a function and a sentinel
    with open("testfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line)

    # use regular interation over the days
    for m in range(len(days)):
        print(m+1, days[m])

    # using enumerate reduces code and provides a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # use zip to combine sequences
    for m in zip(days, daysGer):
        print(m)

    for i, m in enumerate(zip(days, daysGer), start=1):
        print(i, m[0], "=", m[1], "in German")


if __name__ == "__main__":
    main()
