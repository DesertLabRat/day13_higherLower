from art import logo, vs
from game_data import data
import random

def get_data():
    return random.choice(data)

def main():
    score = 0
    print(logo)
    while True:
        if score == 0:
            choice_A = get_data()
        else:
            choice_A = choice_B

        print(f"Choice A: {choice_A['name']}, a {choice_A['description']} from {choice_A['country']}")
        print(vs)
        choice_B = get_data()
        if choice_B.['name'] == choice_A['name']:
            choice_B = get_data()
        print(f"Choice B: {choice_B['name']}, a {choice_B.get('description')} from {choice_B['country']}")

        try:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        except ValueError:
            print("Invalid input.")
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        correct_answer = "A" if choice_z['follower_count'] > choice_B['follower_count'] else "B"

        if user_choice == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


if __name__ == "__main__":
    main()
