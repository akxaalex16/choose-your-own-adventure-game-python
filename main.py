name = input('Type your name: ')
print('Welcome', name, 'to this adventure!')

answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    q2 = input('You have come to a river, You can walk around it or swim across? Type walk to walk around and swim to swim across: ')

    if q2 == 'swim':
        print('You swam across and were eaten by an alligator')
    elif q2 == 'walk':
        print('You walked for many miles, ran out of water and lost the game.')
    else:
        print('Not a valid option. You lose.')
elif answer == 'right':
    q3 = input('You come to a bridge, it looks wobbly, do you want to cross it or head back? (Type: cross or back)')

    if q3 == 'back':
        print('You go back to the main road and you lose.')
    elif q3 == 'cross':
        q3 = input('You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ')

        if q3 == 'yes':
            print('You talk to the stranger and they gave you gold. You WIN!')
        elif q3 == 'no':
            print('You ignore the stranger and they are offended and you lose.')
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

print('Thank you for trying', name)