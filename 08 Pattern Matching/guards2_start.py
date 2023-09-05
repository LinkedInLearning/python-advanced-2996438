# Using pattern guards to restrict how matches are made

# TODO: Pattern guards can get fairly sophisticated
dataset = ["UPPER", 5, "Mixed Case", True, None]
for d in dataset:
    match d:
        case _:
            print(f"{d}: Something else")
