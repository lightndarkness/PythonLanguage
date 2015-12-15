#My first Python application
#Created by me!
#Print command displays a message on the screen
print("""Hello World
My name is Gianni""")

name = input("Come ti chiami? ")
cognome = input("Qual'e' il tuo cognome? ")
print("Ciao " + name.upper() + " " + cognome.lower())

message = "Hello World"
print(message.lower())
print(message.upper())
print(message.swapcase())

height = 12
width = 20

area = height * width
print("L'area e': %d" % area)
print("L'area e': %3d" % area)
print("L'area e': %f" % area)
print("L'area e': %.1f" % area)
print("L'area e': {0:f}".format(area))

salario = int(input("Inserire il salario "))
bonus = int(input("Inserire il bonus "))
stipendio = salario + bonus
print(stipendio)

loanAmount = float(input("Inserisci l'ammontare del mutuo: "))
interessi = float(input("Inserisci il tasso di interesse: "))
numeroAnni = int(input("Inserisci il numero di anni: "))

rataMensile = loanAmount + (loanAmount*interessi*numeroAnni)/(numeroAnni*12)
print("La rata mensile del mutuo e' di: {0:f}".format(rataMensile))