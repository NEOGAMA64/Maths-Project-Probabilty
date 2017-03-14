import numpy as np

def drag_dmg(heroHP):
	print "The dragon shot a fireball at you"
	x = np.random.randint(2,4)
	heroHP = heroHP - x
	print "It dealt " + str(x) + " damage"
	print "You have " + srt(heroHP) + " HP left"
	return heroHP
		
def dragon_slayer():

	heroHP = 10
	dragonHP = 10
	sword = False
	bow = False
	decision = True

	print "A dragon appears!!\n" 
	print "Do you wish to attack it with your sword or your bow and arrows?"
	print "\nThink carefully: arrows do more damage but loading them on the bow will allow the dragon to attack first"
	print "You have 100 health points, or HP, the dragon also has 100 HP though"
	
	while decision == True:	
		
		swordOrBow = raw_input()

		if swordOrBow == "sword" or "Sword":
			print "You have choosen to draw your sword"
			sword = True
			decision = False
		elif swordOrBow == "bow" or "Bow": 
			print "You have choosen to shoot the dragon with your bow"
			bow = True
			decision = False
		else: 
			print "Sorry but you must type in 'sword' or 'bow'"

	if sword == True:
		print "The dragon has landed right in front of you and is ready for a showdown!!"
		while dragonHP > 0 and heroHP > 0:
			
			attack = raw_input("Type 'hit' to strike the dragon with your sword!")
			
			if attack == "hit":
				y = np.random.randint(2,3)
				print "You dealt " + str(y) + " damage"
				dragonHP = dragonHP - y
				print "The dragon has " + str(dragonHP) + " HP left"

			drag_dmg(heroHP)
		
		if dragonHP <= 0:
			print "You won!!! now you can rest in piece"
		elif heroHP <= 0:
			print "It's such as shame but you lost. Now go rest in pieces"

	if bow == True:
		print "The dragon has landed right in front of you and is ready for a showdown!!"
		while dragonHP > 0 and heroHP > 0:
			print "Since you choose to shoot arrows with you bow,\n" 
			print "you must wait a whole turn to load it, giving the dragon a chance to attack first"
			
			drag_dmg(heroHP)

			hit = raw_input("Type 'hit' to shoot the dragon with you bow")

			if hit == "hit":
				z = np.random.randint(3,5)
				print "You dealt " + str(z) + " damage"
				dragonHP = dragonHP - z
				print "The dragon has " + str(dragonHP) + " HP left"


		if dragonHP < heroHP:
			print "You won!!! now you can rest in piece"
		elif heroHP < dragonHP:
			print "It's such as shame but you lost. Now go rest in pieces"

def main():
	slayer = True
	while slayer == True:
		gameStart = raw_input("Do you wish to start?")

		if gameStart == "yes" or "Yes":
			dragon_slayer()
		

if __name__ == '__main__':
	main()