from data import data

mainChoice = 0

def warmup():
    ex1name = data.warmups.excercise1.get('name')
    ex2name = data.warmups.excercise2.get('name')
    ex3name = data.warmups.excercise3.get('name')
    ex4name = data.warmups.excercise4.get('name')
    ex5name = data.warmups.excercise5.get('name')
    ex6name = data.warmups.excercise6.get('name')
    ex7name = data.warmups.excercise7.get('name')
    print(f'\n0. Back \n1. {ex1name} \n2. {ex2name} \n3. {ex3name} \n4. {ex4name} \n5. {ex5name} \n6. {ex6name} \n7. {ex7name} \n')
    try:
        warmChoice = (int)(input(''))
    except:
        print('Only digits(0-7) allowed!')
    while warmChoice != 0:
        if warmChoice == 1:
            for key, val in data.warmups.excercise1.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 2:
            for key, val in data.warmups.excercise2.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 3:
            for key, val in data.warmups.excercise3.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 4:
            for key, val in data.warmups.excercise4.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 5:
            for key, val in data.warmups.excercise5.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 6:
            for key, val in data.warmups.excercise6.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        elif warmChoice == 7:
            for key, val in data.warmups.excercise7.items():
                print(f'{key}  --> {val} \n')
            print('Press \'Enter\' to go back to warm up menu\n')
            input('')
            pass
        else:
            print('Okay. I get it... Your forarms are pumped. But you must press the right key bud!\n')
        
        print(f'\n0. Back \n1. {ex1name} \n2. {ex2name} \n3. {ex3name} \n4. {ex4name} \n5. {ex5name} \n6. {ex6name} \n7. {ex7name} \n')
        try:
            warmChoice = (int)(input(''))
        except:
            print('Okay. I get it... Your forarms are pumped. But you must press the right key bud!\n')


def workout():
    progChoice = -1
    print('\n0. Back \n1. First pair \n2. Second Pair \n3. Third pair \n4. Triplet \n5. Instructions \n')
    try:
        workoutChoice = (int)(input(''))
    except:
        print('Only digits(0-7) allowed!')
    
    while workoutChoice != 0:
        
        if workoutChoice == 1:
            print(f'\n0. Back \n1. ' + data.workouts.pair1[0].get('name') + '\n2. '+ data.workouts.pair1[1].get('name') +' \n')
            progChoice = (int)(input(''))
            while progChoice != 0:
                if progChoice == 1:
                    progressionPair1(0)
                    pass
                elif progChoice == 2:
                    progressionPair1(1)
                    pass
                print(f'\n0. Back \n1. ' + data.workouts.pair1[0].get('name') + '\n2. '+ data.workouts.pair1[1].get('name') +' \n')
                progChoice = (int)(input(''))
        elif workoutChoice == 2:
            print(f'\n0. Back \n1. ' + data.workouts.pair2[0].get('name') + '\n2. '+ data.workouts.pair2[1].get('name') +' \n')
            progChoice = (int)(input(''))
            while progChoice != 0:
                if progChoice == 1:
                    progressionPair2(0)
                    pass
                elif progChoice == 2:
                    progressionPair2(1)
                    pass
                print(f'\n0. Back \n1. ' + data.workouts.pair2[0].get('name') + '\n2. '+ data.workouts.pair2[1].get('name') +' \n')
                progChoice = (int)(input(''))
        elif workoutChoice == 3:
            print(f'\n0. Back \n1. ' + data.workouts.pair3[0].get('name') + '\n2. '+ data.workouts.pair3[1].get('name') +' \n')
            progChoice = (int)(input(''))
            while progChoice != 0:
                if progChoice == 1:
                    progressionPair3(0)
                    pass
                elif progChoice == 2:
                    progressionPair3(1)
                    pass
                print(f'\n0. Back \n1. ' + data.workouts.pair3[0].get('name') + '\n2. '+ data.workouts.pair3[1].get('name') +' \n')
                progChoice = (int)(input(''))
        elif workoutChoice == 4:
            print(f'\n0. Back \n1. ' + data.workouts.pair4[0].get('name') + '\n2. '+ data.workouts.pair4[1].get('name') +' \n3. '+ data.workouts.pair4[2].get('name') +' \n')
            progChoice = (int)(input(''))
            while progChoice != 0:
                if progChoice == 1:
                    progressionPair4(0)
                    pass
                elif progChoice == 2:
                    progressionPair4(1)
                    pass
                elif progChoice == 3:
                    progressionPair4(2)
                    pass
                print(f'\n0. Back \n1. ' + data.workouts.pair1[0].get('name') + '\n2. '+ data.workouts.pair1[1].get('name') +' \n3. '+ data.workouts.pair4[2].get('name') +' \n')
                progChoice = (int)(input(''))
        elif workoutChoice == 5:
            print(data.workouts.workout.get('instructions') + '\n\n' +
                data.workouts.workout.get('rest_time') + '\n\n' +
                    data.workouts.workout.get('tempo') + '\n' )
            pass
        else:
            pass
        
        print('\n0. Back \n1. First pair \n2. Second Pair \n3. Third pair \n4. Triplet \n5. Instructions \n')
        try:
            workoutChoice = (int)(input(''))
        except:
            pass

def progressionPair1(x):
    for key, _ in data.workouts.pair1[x].get('progressions',{}).items():
        for key1, val1 in data.workouts.pair1[x].get('progressions',{}).get(key,{}).items():
            print(key1 + ' >> ' + val1)
        print('\n')

def progressionPair2(x):
    for key, _ in data.workouts.pair2[x].get('progressions',{}).items():
        for key1, val1 in data.workouts.pair2[x].get('progressions',{}).get(key,{}).items():
            print(key1 + ' >> ' + val1)
        print('\n')

def progressionPair3(x):
    for key, _ in data.workouts.pair3[x].get('progressions',{}).items():
        for key1, val1 in data.workouts.pair3[x].get('progressions',{}).get(key,{}).items():
            print(key1 + ' >> ' + val1)
        print('\n')

def progressionPair4(x):
    for key, _ in data.workouts.pair4[x].get('progressions',{}).items():
        for key1, val1 in data.workouts.pair4[x].get('progressions',{}).get(key,{}).items():
            print(key1 + ' >> ' + val1)
        print('\n')



while mainChoice != 3:
    print('\nSelect from the following list...\n')
    print('1. Warmup excercises \n2. Workouts \n3. Exit\n')
    try:
        mainChoice = (int)(input(''))
    except:
        print('Only digits(1-3) allowed!')
    if mainChoice == 1:
        warmup()
    elif mainChoice == 2:
        workout()
    elif mainChoice == 3:
        print('That\'s it! You\'re done! It\'s over! You did it!')
    else:
        print('Wrong choice...')