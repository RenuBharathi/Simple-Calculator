print("Hello! This is BMI Calculator. Know your Body Mass Index.")
while True:
    Weight=float(input('Enter your weight_Kilograms: '))
    Height=float(input('Enter your Height_centiMeters: '))
    BMI = Weight/(Height**2)*10000   #Multiply by 10000 to convert centimeters into meters
    print("Your BMI is", BMI)
    if BMI<18.5:
        print('You are underweight.\nEat more nutritious food. I would love to see you in a bit more weight.')
    elif BMI>18.5 and BMI<24.9:
        print('You have normal BMI.\nYou are Healthy. Maintain your diet. Always be Young')
    elif BMI>25 and BMI<29.9:
        print('You are overweight.\nEat, but try some physical exercises to keep you charming')
    else:
        print('You are obese.\nI know you love food but I want to see you in a lean physique')


    user=input('Do you want to calculate again?')
    if user!='yes' and user!='y':
        print('Thankyou. Have a nice day.')
        break


