import numpy as np
import sys, time, random

#print_slow function by user "Sebastian" in stack overflow forum "printing slowly (Simulate typing)" @ Apr 30 '12 at 21:32
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

def swrd_dmg(dragonHP):
	#a = np.random.randint(1,6)
	#b = np.random.randint(6,11)
	#c = np.random.randint(a,b)
	y = np.random.randint(2,5)
	print_slow("\nYou dealt " + str(y) + " damage\n")
	dragonHP = dragonHP - y
	print_slow("\nThe dragon has " + str(dragonHP) + " HP left\n")
	return dragonHP

def bow_dmg(dragonHP):
	#a = np.random.normal(10,2,1000)
	#b = random.choice(a)

	#c = np.random.rand(1000,1)
	#d = random.choice(c)
	y = np.random.randint(3,7)
	print_slow("\nYou dealt " + str(y) + " damage\n")
	dragonHP = dragonHP - y
	print_slow("\nThe dragon has " + str(dragonHP) + " HP left\n")
	return dragonHP

def drag_dmg(heroHP):

	print_slow("\nThe dragon shot a fireball at you\n")
	x = np.random.randint(3,6)
	heroHP = heroHP - x
	print_slow("\nIt dealt " + str(x) + " damage\n")
	print_slow("\nYou have " + str(heroHP) + " HP left\n")
	return heroHP
		
def dragon_slayer():

	heroHP = 10
	dragonHP = 10
	sword = False
	bow = False
	decision = True

	print_slow("\nA dragon appears!!\n")
	print_slow("\nDo you wish to attack it with your sword or your bow and arrows?\n")
	print_slow("\nThink carefully: arrows do more damage but loading them on the bow will allow the dragon to attack first\n")
	print_slow("\nYou have 10 health points, or HP, the dragon also has 10 HP though\n")
	
	while decision == True:	
		
		swordOrBow = raw_input("\nType in 'sword' or 'bow' to choose: ")

		if swordOrBow == "sword":
			print_slow("\nYou have choosen to draw your sword\n")
			sword = True
			decision = False
		elif swordOrBow == "bow": 
			print_slow("\nYou have choosen to shoot the dragon with your bow\n")
			bow = True
			decision = False
		else: 
			print_slow("\nSorry but you must type in 'sword' or 'bow'\n")

	if sword == True:
		print_slow("\nThe dragon has landed right in front of you and is ready for a showdown!!\n")
		while dragonHP > 0 and heroHP > 0:
			
			attack = raw_input("\nType 'hit' to strike the dragon with your sword!\n")
			
			if attack == "hit" and heroHP > 0:
				dragonHP = swrd_dmg(dragonHP)

				if dragonHP > 0:				
					heroHP = drag_dmg(heroHP)
		
		if 0 >= dragonHP and heroHP > dragonHP:
			print_slow("\nYou won!!!\n\nNow go and claim your price\n")
		elif 0 >= heroHP and dragonHP > heroHP:
			print_slow("\nIt's such as shame but you lost\n\nNow go rest in piece\n")

	if bow == True:
		print_slow("\nThe dragon has landed right in front of you and is ready for a showdown!!\n")
		print_slow("\nSince you chose to shoot arrows with your bow, ")
		print_slow("you must wait a whole turn to load it, giving the dragon a chance to attack first\n")
		
		while dragonHP > 0  and heroHP > 0:
			if dragonHP > 0:
				heroHP = drag_dmg(heroHP)

			if heroHP > 0:
				shoot = raw_input("\nType 'shoot' to shoot the dragon with an arrow\n")
				dragonHP = bow_dmg(dragonHP)

		if 0 >= dragonHP and heroHP > dragonHP:
			print_slow("\nYou won!!!\n\nNow go and claim your price\n")
		elif 0 >= heroHP and dragonHP > heroHP:
			print_slow("\nIt's such as shame but you lost\n\nNow go rest in piece\n")

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
