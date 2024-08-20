print('Hello, welcome to trivia!')

ans = input('Are you ready to play!? (yes/no: ')
score = 0
total_q = 4

if ans.lower() == 'yes' :
    ans = input('1. What is the best programming language? ')
    if ans == 'Python' :
        score +=1
        print('correct!')
    if ans =='python' :
        score+=1
        print('correct!')
    else:
        print('Incorrect!')


    ans = input('2. What is 2 + 8 + 9 -1 ')
    if ans =='18':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. What is better, a m340i or a m3?')
    if ans =='m3':
        score += 1
        print('Correct!')
    else:
        print('Incorrect!')

    ans = input('1. Who won their second UFC fight against one another, Nate Diaz or Conner McGregor? ')
    if ans == 'Nate Diaz' :
        score +=1
        print('correct!')
    if ans == 'nate diaz' :
        score +=1
        print('correct!')
    else:
        print('Incorrect!')


    
                
