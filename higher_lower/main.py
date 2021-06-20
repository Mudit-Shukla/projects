import random
from higher_lower.data import data

count = 0
end_game = False

lst = [random.choice(data)]
lst.append(random.choice(data))

def game_over():
    global count, end_game, lst
    option1 = lst[0]
    option2 = lst[1]

    print(f"Compare A :{option1['name']} , {option1['description']} from {option1['country']}" )
    print(f"Compare B :{option2['name']} , {option2['description']} from {option2['country']}" )
    choice = input("Who has more followers Type 'A' or 'B")
    if choice == 'A' and option1['follower_count'] > option2['follower_count']:
        lst[1] = random.choice(data)
        count += 1

    elif choice == 'B' and option1['follower_count'] < option2['follower_count']:
        count += 1
        lst[0] = random.choice(data)

    else:
        print(f"{option1['name']} ,{option1['follower_count']} {option1['description']} from {option1['country']}")
        print(f"{option2['name']} ,{option2['follower_count']} {option2['description']} from {option2['country']}")
        print(f"Game over Your Score is {count}")
        end_game = True


while not end_game:
    game_over()