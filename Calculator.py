print('Hello by Renu, Welcome to the basic Calculator')
while True:
    x= int(input('Enter First number ='))
    y = int(input('Enter Second number= '))
    print('Choose operator: 1.Add, 2.Sub, 3.Multiply, 4.Divide, 5.Power')
    op= int(input('Choose number between 1 to 5 : '))
    if op==1:
        Output=x+y
        print(Output)
    elif op==2:
        Output=x-y
        print(Output)
    elif op==3:
        Output=x*y
        print(Output)
    elif op==4:
        Output=x/y
        print(Output)
    elif op==5:
        Output=x**y
        print(Output)
    else:
        print('Invalid operator')
 
    choice = input('Do you want to calculate again? (yes/no):')
    if choice!= 'yes':
     print('Thankyou, See you again :)')
     break
     
    
