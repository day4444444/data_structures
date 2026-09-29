#Scrip description: Roll dice
#function whithout return (funcion sin retorno)}
from random import randint, uniform
import os
def rollDice():
    die1=randint(1,6)
    die2=randint(1,6)
    print(f"Die1 :{die1}")
    print(f"Die2 :{die2}")
rollDice()
