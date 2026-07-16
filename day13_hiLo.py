from art import logo, vs
from game_data import data
import random

def get_data():
    return random.choice(data)

def display_choice(label, choice):
    print(
        f"Choice {label}: "
        f"{choice['name']}, "
        f"a {choice['description']} "
        f"from {choice['country']}"
    )

def main():
    score = 0
    print(logo)
    while True:
        if score == 0:
            choice_A = get_data()
        else:
            choice_A = choice_B

        choice_B = get_data()
        while choice_B == choice_A:
            choice_B = get_data()

        display("A", choice_A)
        print(vs)
        display("B", choice_B)

        while True:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
            if user_choice in ("A", "B"):
                break

            print("Please enter A or B."

        correct_answer = "A" if choice_z['follower_count'] > choice_B['follower_count'] else "B"

        if user_choice == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


if __name__ == "__main__":
    main()
