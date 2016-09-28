#declareer de vaiablen
monthlyPayment=0
loanAmount= 0
interestRate=0
numberPayments=0
loanduration=0

#vraag voor input
strloanAmount = input("Wat wordt je totale lening? ")
strinterestRate = input("Wat is het rente percentage? ")
strloanduration = input("Wat is de looptijd van de lening? ")

#omzetten naar floats
loanAmount= float(strloanAmount)
interestRate=float(strinterestRate)
loanduration=float(strloanduration)

#De looptijd maal 12 maanden
numberPayments = loanduration*12

monthlyPayment = loanAmount * interestRate * (1+interestRate) * numberPayments \
    / ((1+interestRate)* numberPayments -1)

print("De maandelijkse betaling wordt " + str(monthlyPayment))



