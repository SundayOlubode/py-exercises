hours=float(input('Enter the hour(s): '))
rate=float(input('Enter the rate: '))
pay = 0
def computepay(hours, rate):
    try:
        if (hours <= 40):
            pay = (hours * rate)
        else:
            pay = ((hours * rate) + ((hours - 40) * rate * 1.5 ))
        return pay
    except:
        print('Should be an integer value!')
print('Your wage is: ', computepay(hours, rate))
