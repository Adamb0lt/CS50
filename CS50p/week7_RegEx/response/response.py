from validator_collection import validators, checkers, errors


def main():
    ask = input("What's your email address? ")
    print(check(ask))

def check(e):
    try:
        validators.email(e)
        return "Valid"
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return "Invalid"

if __name__ == "__main__":
    main()