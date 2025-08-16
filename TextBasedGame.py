# Alexey Gorenkov
inventory = []

#Sample function showing the goal of the game and move commands
def show_instructions(player_name):  
   #print a main menu and the commands
   print(f'Welcome to \'Against the System Text Game\', {player_name}')
   print("Your goal is to collect all 6 core items before facing the final mirror.")
   print("Move commands: go South, go North, go East, go West")
   print("Add to Inventory: get 'item name'")
   print('_' * 30)

# Show status function
def show_status(current_room, inventory):
    print(f'You are in the {current_room}')
    print(f'Your inventory is {inventory}')
    # If rooms[current_room] has an "item" AND it’s not already in inventory, print: “You see a <Item>.” - fix

def parse_command(raw_input):
    raw_input.strip()
    # If input starts with "go " → return ("MOVE", Direction)
    # Else if input starts with "get " → return ("GET", ItemName)
    # Else → return ("INVALID", None)

def main():
    show_instructions()
    current_room = 'Room in Russia'
    correct_answers = 0
    rehab_unlocked = False 
    total_items = 6
    villian_room = 'Mirror Room'
    rooms = {
        'Room in Russia': {
            'North': 'Tokyo Dorm'
            },
        'Tokyo Dorm': {
            'South': 'Room in Russia', 
            'East': 'Convenience Store Job', 
            'item': 'Pocket Dictionary', # CORE ITEM
            'quiz': {
                'prompt': 'What lessons did you learn in Tokyo Dorm?',
                'choices': [
                    'I made a new life out of unfamiliar signs.',
                    'I should\'ve stayed where I understood everything.',
                    'Real growth is only possible in your comfort zone.'
                ],
                'correct': 1 # Index of correct answer in choices list
            }
        },
        'Convenience Store Job': {
            'West': 'Tokyo Dorm', 
            'East': 'Tiny Apartment', 
            'item': 'Barcode Scanner', # CORE ITEM
            'quiz': {
                'prompt': 'What was the real gain from your first job?',
                'choices': [
                    'These kinds of jobs mean I failed.',
                    'If I\'m not admired, I\'m not progressing.',
                    'I started from zero and still made it work.'
                ],
                'correct': 3 # Index of correct answer in choices list
            }
        },
        'Tiny Apartment': {
            'West': 'Convenience Store Job', 
            'North': 'Used Car Dealership', 
            'item': 'Secondhand Laptop', # CORE ITEM
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
            'item': 'Spare Car Key', # CORE ITEM
            'quiz': {
                'prompt': 'What did you gain from the used car dealership?',
                'choices': [
                    'Letting go means failure.',
                    'I bought, fixed, and let go — and learned to move on.',
                    'The more I own, the better I am.'
                ],
                'correct': 2 # Index of correct answer in choices list
            }
        },
        'Console Room': {
            'West': 'Used Car Dealership',
            'North': 'Amazon Office',
            'item': 'Game Controller', # CORE ITEM
            'quiz': {
                'prompt': 'What did video games teach you?',
                'choices': [
                    'It\'s wrong to want things and still feel empty.',
                    'The things I once dreamed of didn\'t fill the void - but they helped me understand it.',
                    'If I\'m not fulfilled, I\'m broken.'
                ],
                'correct': 2 # Index of correct answer in choices list
            }
        },
        'Amazon Office': {
            'South': 'Console Room',
            'East': 'Rehab Room',
            'item': 'Amazon Badge', # CORE ITEM
            'quiz': {
                'prompt': 'What did your job at Amazon prove?',
                'choices': [
                    'I showed up. I carried region. I endured. Even when I wasn\'t rewarded.',
                    'If I\'m not promoted, it means I\'m not good enough.',
                    'People should always recognize your effort.'
                ],
                'correct': 1 # Index of correct answer in choices list
            }
        },
        'Rehab Room': {
            'West': 'Amazon Office',
            'North': 'Mirror Room',
            'item': 'Rehabilitation Cane', # OPTIONAL ITEM (not part of 6 core items)
            # No quiz here
        },
        'Mirror Room': {
            'South': 'Rehab Room',
            'villian': True # entering here ends the game
            # No item, no quiz
        }
    }
    # For clarity in your win check:
    core_items = {
        'Pocket Dictionary',
        'Barcode Scanner',
        'Secondhand Laptop',
        'Spare Car Key',
        'Game Controller',
        'Amazon Badge',
    }
    
