'''
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Exercise 8 (and Solution)

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import random

moves = ['rock', 'scissors', 'paper']
flag =0
print("Welcome to 'Rock-Paper-Scissor' game...\n")

selector = int(input("Select the game mode [1-singleplayer/2-multiplayer] "))
print("\n")

if (selector == 1):
	while(flag == 0):
		playerA = str(input("Player A inset your move: "))
		pc = str(random.choice(moves))
		print("The computer selected " + str(pc) + "\n")
		if (playerA == pc):
			print("Same move...")
		elif(playerA=="rock" and pc=="scissors"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		elif(playerA=="scissors" and pc=="paper"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		elif(playerA=="paper" and pc=="rock"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		else:
			print("Computer wins with "+ str(pc)+" ...\n")
		value=input("\nDo you want to continue playing?[yes/no]: ")
		print("\n")
		if (value == "no"):
			flag=1
			break

if(selector == 2):
	while(flag == 0):
		playerA = str(input("Player A inset your move: "))
		playerB = str(input("Player B inset your move: "))
		if (playerA == playerB):
			print("Same move...")
		elif(playerA=="rock" and playerB=="scissors"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		elif(playerA=="scissors" and playerB=="paper"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		elif(playerA=="paper" and playerB=="rock"):
			print("PlayerA wins with "+ str(playerA)+" ...")
		else:
			print("PlayerB wins with "+ str(playerB)+" ...")
		value=input("\nDo you want to continue playing?[yes/no]: ")
		print("\n")
		if (value == "no"):
			flag=1
			break
else:
	print("Incorrect value.. good bye!\n")




