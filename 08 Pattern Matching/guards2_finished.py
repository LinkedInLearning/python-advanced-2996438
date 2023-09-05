# Using pattern guards to restrict how matches are made

# Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case str() as s if s.isupper():
            print(f"{d}: Upper case string")
        case str():
            print(f"{d}: Not an upper-case string")
        # order is important here - Python will treat bools as ints
        # so the check for bool has to come before int

        case bool():
            print(f"{d}: Boolean")
        case int():
            print(f"{d}: Integer")
        case _:
            print(f"{d}: Something else")
