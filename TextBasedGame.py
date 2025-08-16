#Alexey Gorenkov
#Sample function showing the goal of the game and move commands
def show_instructions(player_name):  
   #print a main menu and the commands
   print(f'Welcome to \'Against the System Text Game\', {player_name}')
   print("Your goal is to collect all 6 core items before facing the final demon.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print('_' * 30)

#Show status function
def show_status(current_room, inventory, rooms, collected_rooms):
    print(f'You are in: {current_room}')
    print(f'Inventory: {inventory if inventory else []}')
    item_in_room = rooms[current_room].get('item')
    if item_in_room and current_room not in collected_rooms:
        print(f'You see a {item_in_room}')
    print('_' * 30)

#Parsing command, either go or get
def parse_command(raw_input):
    stripped_input = raw_input.strip()
    if not stripped_input:
        return  ('INVALID', None)
    
    lower_stripped = stripped_input.lower()
    if lower_stripped.startswith('go '):
        direction = stripped_input[3:].strip().title()
        return ('GO', direction)
    if lower_stripped.startswith('get '):
        item_name = stripped_input[4:].strip()
        return ('GET', item_name) if item_name else ("INVALID", None)
    return ('INVALID', None)

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
    collected_rooms = [] #rooms where items was picked up
    answered_quizzes = [] #rooms where quizzes were answered
    correct_answers = 0
    inventory = []
    total_questions = 6

    #List of core items:
    core_items = [
        'Pocket Dictionary',
        'Barcode Scanner',
        'Secondhand Laptop',
        'Spare Car Key',
        'Game Controller',
        'Amazon Badge',
    ]

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
            'villain': True #Entering here ends the game
            #No item, no quiz
        }
    }

    while True:
        if current_room == villain_room:
            has_all_items = check_core_items(inventory, core_items)
            if has_all_items == True:
                print('You have collected all core items, faced the demon of Mirror room and defeated it!')
                print('Now the real game begins')
            elif rehab_unlocked and 'Rehabilitation Cane' in inventory:
                print('You have the Rehabilitation Cane, you already won, you can go back to life')
            else:
                print('You have not collected all core items, you were defeated by the demon of Mirror room')
                print('Now the real struggle begins')
            break
        show_status(current_room, inventory, rooms, collected_rooms)

        #One-time quiz if present
        quiz = rooms[current_room].get('quiz')
        if quiz and current_room not in answered_quizzes:
            print(quiz['prompt'])
            print(f"1) {quiz['choices'][0]}")
            print(f"2) {quiz['choices'][1]}")   
            print(f"3) {quiz['choices'][2]}")
            user_answer = input('Choose 1/2/3: ').strip()
            #Count correct quiz answers
            if user_answer == str(quiz['correct']):
                correct_answers += 1
            else:
                pass
            answered_quizzes.append(current_room)
            print("_" * 30)
        
        if len(answered_quizzes) == total_questions and correct_answers == total_questions:
            rehab_unlocked = True
            print('You\'ve aced every reflection. A hidden door unlocks somewhere...')
        print("_" * 30)

        #Command
        raw_input = input('Enter your action: ')
        if raw_input.strip().lower() == 'exit':
            print('Thanks for playing!')
            break
        action, payload = parse_command(raw_input)
        if action == 'INVALID':
            print('Invalid command. Try: \'go North\' or \'get Pocket Dictionary\'.')
            continue
        
        if action == 'GO':
            direction = payload #North/South/East/West
            # Rehab gate 
            if current_room == 'Amazon Office' and direction == 'East' and not rehab_unlocked:
                print('That path is closed to you for now.')
                continue
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print('You can\'t go that way')
        elif action == 'GET':
            requested = payload
            item_in_room = rooms[current_room].get('item')

            if not item_in_room:
                print("There's nothing to pick up here.")
            elif current_room in collected_rooms:
                print("You already picked that up.")
            elif requested.lower() == item_in_room.lower():
                inventory.append(item_in_room)
                collected_rooms.append(current_room)
                print(f"Picked up: {item_in_room}")
            else:
                print(f"That item isn't here. You see {item_in_room}.")

if __name__ == '__main__':
    main()




