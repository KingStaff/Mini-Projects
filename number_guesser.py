import random


def get_valid_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Invalid input. Please enter a valid number.")


# difficulty level (optional)
print("Choose difficulty: Easy (1-10), Medium (1-50), Hard (1-100)")
difficulty = input("Enter E, M, or H: ").strip().upper()

if difficulty == "E":
    top_of_range = 10
elif difficulty == "M":
    top_of_range = 50
elif difficulty == "H":
    top_of_range = 100
else:
    top_of_range = get_valid_number("Type a number: ")

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = get_valid_number("Make a guess: ")

    if user_guess == random_number:
        print(
            f"🎉 You got it in {guesses} guesses! The number was {random_number}.")
        break
    elif user_guess > random_number:
        print("🔻 Too high! Try again.")
    else:
        print("🔺 Too low! Try again.")
