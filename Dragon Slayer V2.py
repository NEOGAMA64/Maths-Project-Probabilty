import numpy as np
import sys, time, random, math

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00)

def points(heroP, dragonP):
	print_slow("\nYou have a total of " +str(heroP)+" points\n")
	print_slow("\nThe dragon has a total of "+str(dragonP)+" points\n")

def dmg(dragonP, heroP):

	dragDmg = np.random.randint(1,6)
	heroDmg = np.random.randint(1,6)

	print_slow("\nYou did "+ str(heroDmg)+" damage\n")
	print_slow("\nThe dragon did "+ str(dragDmg)+ " damage\n")

	if dragDmg == heroDmg:
		print_slow("\nSince you both did the same amount of damage,\n")
		print_slow("\nthe dragon gets the point as it weighs more and has greater overall force\n")
	
	"""if dragDmg == heroDmg:
		print_slow("\nYou and the dragon attacked with equal strength\n")
		print_slow("\nYou have an equal chance of getting the point\n")
		tiebreak = np.random.randint(1,3)
		if tiebreak == 1:
			heroP = heroP + 1
			print_slow("\nYou were lucky enough to get the point\n")
		elif tiebreak == 2:
			dragonP = dragonP + 1
			print_slow("\nThe dragon go the point\n")"""

	if dragDmg >= heroDmg:
		dragonP = dragonP + 1
	elif heroDmg > dragDmg:
		heroP = heroP + 1

	return heroP,dragonP

def dragon_slayer():
	dragonP = 0
	heroP = 0
	a = True

	print_slow("\nA dragon appears!!\n")
	print_slow("\nYou quickly draw your greatsword from your back\n")
	print_slow("\nYou wait for the dragon to make his move\n")
	print_slow("\nThe dragon has landed right in front of you and is ready for a showdown!!\n")
	
	while a == True:
			
		attack = raw_input("\nType 'hit' to strike the dragon with your sword!\n")
			
		if attack == "hit":
			heroP, dragonP = dmg(dragonP, heroP)

			points(heroP, dragonP)

		if heroP == 3:
			print_slow("\nYou won!!!\n\nNow go and claim your price\n")
			a = False
			#binomial()

		elif dragonP == 3:
			print_slow("\nIt's such as shame but you lost\n\nNow go rest in piece\n")
			a = False
			#binomial()

def binomial():
	n = 5
	x = 3
	p = 0.4

	y = math.pow(p,x)
	z = 1 - p 
	e = n - x
	d = math.pow(z,e)
	a = y * d

	print a

def main():
	slayer = True
	while slayer == True:
		gameStart = raw_input("\nDo you wish to start or exit Dragon Slayer? ")

		if gameStart == "start":
			dragon_slayer()
		elif gameStart == "exit":
			slayer = False

if __name__ == '__main__':
	main()