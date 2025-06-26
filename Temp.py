def celsiustofahrenheit(C):
    return C*(9/5)+32
def fahrenheittocelsius(F):
    return(F-32)*(5/9)
def celsiustokelvin(cel):
    return cel+273.15
def fahrenheittokelvin(fah):
    return (fah-32)*(5/9)+273.15
while True:
    print("Temperaute converter")
    choice=int(input("Choose:\n1 for celsius to fahrenheit\n2 for fahrenheit to celsius\n3 for celsius to kelvin\n4 for fahrenheit to kelvin:\n"))
    if choice==1:
        C=float(input("Enter temperaute in celsius: "))
        Temperature=celsiustofahrenheit(C)
        print("Temperature in fahrenheit:",Temperature)
    elif choice==2:
        F=float(input("Enter temperature in fahrenheit: "))
        Temperature=fahrenheittocelsius(F)
        print("Temperature in celsius:",Temperature)
    elif choice==3:
        cel=float(input("Enter Temperature in Celsius: "))
        Temperature+celsiustokelvin(cel)
        print("Temperature in Kelvin:",Temperature)
    elif choice==4:
        fah=float(input("Enter temperature in fahrenheit:"))
        Temperature=fahrenheittokelvin(fah)
        print("Temperature in kelvin:",Temperature)
    else:
        print("Invalid operation")

    Respond=input("Do you want to continue? Yes or No\n")
    if Respond!="yes":
        print("Bye,Thankyou")
        break
        
