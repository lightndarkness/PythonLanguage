#The import statement gives us access to
#the functionality of the datetime class
import datetime
#today() is a function that returns today's date
print(datetime.date.today())

#store the value in a variable called currentDate
currentDate = datetime.date.today()
print(currentDate)

print(currentDate.year) # This prints the year property of the date
print(currentDate.month) # This prints the month property of the date
print(currentDate.day) #This prints the day property of the date

print(currentDate.strftime("%d %m %Y"))
print(currentDate.strftime("%A %d %B %Y"))

dataNascita = input("Inserisci la tua data di nascita: ")
dataNascita = datetime.datetime.strptime(dataNascita, "%d-%m-%Y").date()
print("Tu sei nato nel mese di " + dataNascita.strftime("%B"))

oraNascita = input("Inserisci l'ora in cui sei nato: ")
oraNascita = datetime.datetime.strptime(oraNascita, "%H:%M").time()
print("Tu sei nato alle " + oraNascita.strftime("%H:%M"))

expressDelivery = input("Vuoi la consegna express per la tua merce? ")
if expressDelivery.lower() == "yes":
    print("Ci sara' un extra costo di 10 euro")
print("Grazie e arrivederci")

saldoCorrente = 150
if saldoCorrente > 100:
    print("Complimenti hai diritto ad uno sconto sui costi di gestione")
print("Arrivederci")