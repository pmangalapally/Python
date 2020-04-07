import random

for sample in range(10000):

    previous_flip_type = None
    flip_counter = 0
    number_of_streaks = 0

    for flip_number in range(100):
        flip = random.randint(0,1)
        #flip = 0
        if flip == 0:
            flip_type = 'T'
        else:
            flip_type = 'H'
        
        if previous_flip_type == flip_type:
            flip_counter = flip_counter + 1
        else:
            flip_counter = 0

        if flip_counter == 6:
            flip_counter = 0
            number_of_streaks = number_of_streaks + 1
        print(flip_type, end = '')
        previous_flip_type = flip_type

    print("\n", number_of_streaks, "\n")
    print('Chance of streak: {}%'.format(float((number_of_streaks/100))))
