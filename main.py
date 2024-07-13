def main():
    # Constants for ticket prices
    full_price = 18.40
    half_price = 8.40

    # Asking user for their age
    age = int(input("Please enter your age: "))

    # Determining ticket price based on age
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age >= 0 and age < 18:
        print("You qualify for a half-price ticket.")
        print(f"Price: ${half_price}")
    else:
        print("You need to pay full price for the ticket.")
        print(f"Price: ${full_price}")

if __name__ == "__main__":
    main()
