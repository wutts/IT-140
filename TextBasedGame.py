#Alexey Gorenkov

#Sample function showing the goal of the game and move commands
from ast import parse


def show_instructions(player_name):  
   #print a main menu and the commands
   print(f'Welcome to \'Against the System Text Game\', {player_name}')
   print("Your goal is to collect all 6 core items before facing the final mirror.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print('_' * 30)

#Show status function
def show_status(current_room, inventory, rooms, collected_rooms):
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    item_in_room = rooms[current_room].get('item')
    if item_in_room and current_room not in collected_rooms:
        print(f'You see a {item_in_room}')
    print('_' * 30)

#Parsing command, either go or get
def parse_command(raw_input):
    stripped_input = raw_input.strip()
    if stripped_input.startswith('go '):
        direction = stripped_input[3:]
        return ('MOVE', direction)
    elif stripped_input.startswith('get '):
        name = stripped_input[4:]
        return ('GET', name)
    else:
        return('INVALID', None)

#Checking if direction is valid
def check_direction(direction):
    if direction in ('North', 'South', 'East', 'West'):
        return True
    else:
        print('Invalid direction, please try North, South, East, West or exit')
        return False

#Checking if player has collected all core items
def check_core_items(inventory, core_items):
    for core_item in core_items:
        if core_item not in inventory:
            return False
    return True

# Main function
def main():
    player_name = input('Enter your name: ')
    show_instructions(player_name)
    current_room = 'Room in Russia'
    villain_room = 'Mirror Room'
    rehab_unlocked = False 
    collected_rooms = []
    answered_quizzes = []
    correct_answers = 0
    inventory = []
    #For clarity in your win check:
    core_items = {
        'Pocket Dictionary',
        'Barcode Scanner',
        'Secondhand Laptop',
        'Spare Car Key',
        'Game Controller',
        'Amazon Badge',
    }
    total_items = 6
    rooms = {
        'Room in Russia': {
            'North': 'Tokyo Dorm'
            },
        'Tokyo Dorm': {
            'South': 'Room in Russia', 
            'East': 'Convenience Store Job', 
            'item': 'Pocket Dictionary', #CORE ITEM
            'quiz': {
                'prompt': 'What lessons did you learn in Tokyo Dorm?',
                'choices': [
                    'I made a new life out of unfamiliar signs.',
                    'I should\'ve stayed where I understood everything.',
                    'Real growth is only possible in your comfort zone.'
                ],
                'correct': 1 #Index of correct answer in choices list
            }
        },
        'Convenience Store Job': {
            'West': 'Tokyo Dorm', 
            'East': 'Tiny Apartment', 
            'item': 'Barcode Scanner', #CORE ITEM
            'quiz': {
                'prompt': 'What was the real gain from your first job?',
                'choices': [
                    'These kinds of jobs mean I failed.',
                    'If I\'m not admired, I\'m not progressing.',
                    'I started from zero and still made it work.'
                ],
                'correct': 3 #Index of correct answer in choices list
            }
        },
        'Tiny Apartment': {
            'West': 'Convenience Store Job', 
            'North': 'Used Car Dealership', 
            'item': 'Secondhand Laptop', #CORE ITEM
            'quiz': {
                'prompt': 'What did you gain from the lonely apartment?',
                'choices': [
                    'It\'s not worth trying if it\'s not official.',
                    'I taught myself what the system didn\'t.',
                    'Only degrees matter.'
                ],
                'correct': 2 # Index of correct answer in choices list
            }
        },
        'Used Car Dealership': {
            'South': 'Tiny Apartment', 
            'East': 'Console Room',
            'item': 'Spare Car Key', #CORE ITEM
            'quiz': {
                'prompt': 'What did you gain from the used car dealership?',
                'choices': [
                    'Letting go means failure.',
                    'I bought, fixed, and let go — and learned to move on.',
                    'The more I own, the better I am.'
                ],
                'correct': 2 #Index of correct answer in choices list
            }
        },
        'Console Room': {
            'West': 'Used Car Dealership',
            'North': 'Amazon Office',
            'item': 'Game Controller', #CORE ITEM
            'quiz': {
                'prompt': 'What did video games teach you?',
                'choices': [
                    'It\'s wrong to want things and still feel empty.',
                    'The things I once dreamed of didn\'t fill the void - but they helped me understand it.',
                    'If I\'m not fulfilled, I\'m broken.'
                ],
                'correct': 2 #Index of correct answer in choices list
            }
        },
        'Amazon Office': {
            'South': 'Console Room',
            'East': 'Rehab Room',
            'item': 'Amazon Badge', #CORE ITEM
            'quiz': {
                'prompt': 'What did your job at Amazon prove?',
                'choices': [
                    'I showed up. I carried region. I endured. Even when I wasn\'t rewarded.',
                    'If I\'m not promoted, it means I\'m not good enough.',
                    'People should always recognize your effort.'
                ],
                'correct': 1 #Index of correct answer in choices list
            }
        },
        'Rehab Room': {
            'West': 'Amazon Office',
            'North': 'Mirror Room',
            'item': 'Rehabilitation Cane', #OPTIONAL ITEM (not part of 6 core items)
            #No quiz here
        },
        'Mirror Room': {
            'South': 'Rehab Room',
            'villian': True #Entering here ends the game
            #No item, no quiz
        }
    }

    while True:
        if current_room == villain_room:
            if check_core_items(inventory, core_items) is True:
                print('You have collected all core items, faced the demon of Mirror room and defeated it!')
                print('Now the real game begins')
            else:
                print('You have not collected all core items, you were defeated by the demon of Mirror room')
                print('Now the real struggle begins')
            break
        show_status(current_room, inventory, rooms, collected_rooms)

        #One-time quizk if present
        if 'quiz' in rooms[current_room] and current_room not in answered_quizzes:
            print(rooms[current_room]['quiz']['prompt']['choices'])
            user_answer = input('Enter your answer: ')
            if user_answer == quiz['correct']:
                corrent_answers += 1
            else:
                rehab_unlocked = True
            answered_quizzes.append(current_room)
        
        #Command
        raw_input = input('Enter your move: ')
        if raw_input.strip().lower() == 'exit':
            print('Thanks for playing!')
            break
        parse_command(raw_input)



