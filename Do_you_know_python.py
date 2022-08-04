global score 
score = 0
print('do you know python? well lets find out')

number1 = input('Q1. how do you print somthing on the screen ')

if number1 == 'print()':
    print('Correct')
    score = score + 1
else: print('Worng the answer is print()')
    
number2 = input('how do you get user input ')

if number2 == 'input()':
    print('Correct')
    score = score + 1
       
else: print('Worng the answer is input()')




print(str(score))
