invoer = ('')
som = 0

while(not invoer == 'stop'):
    invoer = input('Geef een getal in of stop ')
    if(invoer == 'stop'):
        break
    else:
        try:
            invoer = int(invoer)
            som = som + invoer
        except ValueError:
            print("gelieve een geheel getal in the geven ")

print("De som is: ",som)

