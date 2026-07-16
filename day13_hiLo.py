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

        print(f"Choice A: {choice_A.get('name')}, a {choice_A.get('description')} from {choice_A.get('country')}")
        print(vs)
        choice_B = get_data()
        if choice_B.get('name') == choice_A.get('name'):
            choice_B = get_data()
        print(f"Choice B: {choice_B.get('name')}, a {choice_B.get('description')} from {choice_B.get('country')}")

        try:
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        except ValueError:
            print("Invalid input.")
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if choice_A.get('follower_count') > choice_B.get('follower_count'):
            if user_choice == 'A':
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                break
        elif choice_A.get('follower_count') < choice_B.get('follower_count'):
            if user_choice == 'B':
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                break





if __name__ == "__main__":
    main()
