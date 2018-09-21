#!/usr/bin/python3.6

z = 1

while z == 1:

	def addition():
		a = input("Entrez le premier nombre = ")
		b = input("Entrez le deuxième nombre = ")
		a = float(a)
		b = float(b)
		c = 0
		c = a + b
		print("Le résultat de ", a, " + ", b, " est ", c)

	def soustraction():
		a = input("Entrez le premier nombre = ")
		b = input("Entrez le deuxième nombre = ")
		a = float(a)
		b = float(b)
		c = 0
		c = a - b
		print("Le résultat de ", a, " - ", b, " est ", c)

	def multiplication():
		a = input("Entrez le premier nombre = ")
		b = input("Entrez le deuxième nombre = ")
		a = float(a)
		b = float(b)
		c = 0
		c = a * b
		print("Le résultat de ", a, " x ", b, " est ", c)

	def division():
		a = input("Entrez le premier nombre = ")
		b = input("Entrez le deuxième nombre = ")
		a = float(a)
		b = float(b)
		c = 0
		c = a / b
		print("Le résultat de ", a, " / ", b, " est ", c)


	print("""----------------------------------Calculatrice----------------------------------
	1. Addition
	2. Soustraction
	3. Multiplication
	4. Division
	5. Quitter""")
	choix = input("Que souhaitez-vous faire ? ")
	if choix == "1":
		addition()
	elif choix == "2":
		soustraction()
	elif choix == "3":
		multiplication()
	elif choix == "4":
		division()
	elif choix == "5":
		break
	else:
		print("Entrez un chiffre correct.")
		continue
