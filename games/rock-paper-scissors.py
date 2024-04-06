# Rock Paper Scissors
from random import sample
moves = ['rock', 'paper', 'scissors']
user = ''
while user.lower() not in moves:
    user = input("Enter rock paper or scissors: ")
cpu = sample(moves,1)[0]

print(f"You: {user}\nComputer: {cpu}")

if cpu == user:
    print("Tie")
elif (cpu == moves[0] and user == moves[2]) or (cpu == moves[1] and user == moves[0]) or (cpu == moves[2] and user == moves[1]):
    print("You lose!")
else:
    print("You win")