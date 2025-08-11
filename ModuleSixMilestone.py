# Alexey Gorenkov

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# Setting current room to 'Great Hall'
current_room = 'Great Hall'
# Checking if direction is correct and printing message in case it is not
def check_direction(direction):
    if direction in ('North', 'South', 'East', 'West'):
        return True
    else:
        print('Invalid direction, please try North, South, East, West or exit')
        return False

# Main loop
while current_room != 'exit':
    print(f'You are in the {current_room}')
    user_direction = input('Choose direction: ').strip().lower()
    if user_direction == 'exit':
        current_room = 'exit'
        print('Thanks for playing!')
        continue

    possible_directions = rooms[current_room]
    if user_direction in possible_directions:
        current_room = possible_directions[user_direction]
    else:
        print('You can\'t go that way')


