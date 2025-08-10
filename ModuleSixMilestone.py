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
def check_direction(direction):
    if direction == 'North' or direction == 'West' or direction == 'East' or direction == 'South' or direction == 'exit':
        print(f'Moving in direction {direction}')
    else:
        print('Invalid direction. Please try using: West, East, North, South or exit')


# Main loop
while current_room != 'exit':
    print(f'You are in the {current_room}')
    user_direction = input('Choose direction: ').strip().lower()
    if user_direction == 'exit':
        current_room = 'exit'
    user_direction = user_direction.capitalize()
    check_direction(user_direction)
    possible_directions = rooms[current_room]

    if user_direction in possible_directions:
        current_room = possible_directions[user_direction]
    else:
        pass


