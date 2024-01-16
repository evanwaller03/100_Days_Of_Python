import random
from userData import user_data

def getBIndex(a_index):
    continue_selecting = True
    while continue_selecting:
        rand_index = random.randint(0,9)
        if rand_index != a_index:
            selected_person = user_data[rand_index]
            continue_selecting = False
    return selected_person, rand_index

def select_person(this_index, userAorB):
    if userAorB == 'a':
        selected_person = user_data[this_index]
        return selected_person, this_index
    else:
        return getBIndex(this_index)
    

def get_starting_index():
    return random.randint(0,9)

def ask_question(userA, userB):
    print(f"Compare A: {userA['name']}, a {userA['description']}, from {userA['country']}")
    print(f"Compare B: {userB['name']}, a {userB['description']}, from {userB['country']}")
    return input("Who has more followers? Type 'A' or 'B': ").lower()

def calculate_answer(a_count, b_count):
    if a_count > b_count:
        return 'a'
    if b_count > a_count:
        return 'b'
    else:
        return ''

def run_game():
    print("Welcome to Higher or Lower.")
    user_score = 0
    userA, userAIndex = select_person(get_starting_index(), 'a')
    again = True
    while again:
        if user_score > 0:
            userA, userAIndex = select_person(userBIndex, 'a')
        userB, userBIndex = select_person(userAIndex, 'b')
        user_response = ask_question(userA, userB)
        answer = calculate_answer(userA['follower_count'], userB['follower_count'])
        if user_response == answer:
            user_score += 1
        else:
            again = False
    
    print(f"Your final score: {user_score}.")
    if input("Play again? Type 'yes' or 'no': ") == 'yes':
        run_game()
    else:
        print('Thank you for playing.')
    
run_game()
            
