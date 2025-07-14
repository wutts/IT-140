from datetime import datetime

'''
We didn't cover modules, but I had experience working with them
Googled "How to grab current year in Python
Found datetime and it's attributes 
.now() - grabs currect date and time
.year() - extracts year
'''

current_year = datetime.now().year
name = input('What is your name? ')
age = int(input('How old are you? '))
birth_year = current_year - age
print(f'Hello {name}! You were born in {birth_year}')