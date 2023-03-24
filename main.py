# returns a number guessed by the computer in the provided range
def guess_number(maximum_n: int, minimum_n: int) -> int:
    return int((max_ - min_) / 2) + min_


# takes the input of the user and validates it
def get_user_input() -> str:
    correct_answers = ["too small", "too big", "you win"]  # possible user input
    while True:
        user_in = input().lower()
        if user_in in correct_answers:
            return user_in
        print("Provide a correct input: 'too small', 'too big' or 'you win'")


print("Think of a number between 0 and 1000 and I'll guess it.")
print("Guide me by typing 'too small', 'too big' or 'you win' in the console.")

min_ = 0
max_ = 1000

while True:
    guess = guess_number(min_, max_)
    print(f"I'm guessing: " + str(guess))
    user_input = get_user_input()
    if (max_ == min_) and (user_input != "you win"):
        print("Do not cheat.")
    elif user_input == "too small":
        min_ = guess
    elif user_input == "too big":
        max_ = guess
    elif user_input == "you win":
        print("Yay, I've won!")
        break


