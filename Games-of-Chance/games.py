import random

money = 100

#Write your game of chance functions here

def flipCoin(bet, choice):
  result = random.randint(1, 2)
  if choice == 'Heads' or choice == 'Tails':
    if (choice == 'Heads' and result == 1) or (choice == 'Tails' and result == 2):
      print('Your choice was {choice}. You won ${bet}'.format(choice=choice, bet=bet))
      return bet
    else:
      print('Your choice was {choice}. You lost ${bet}'.format(choice=choice,bet=bet))
      return -bet
  else:
    print('Wrong Choice')
  return

def Chohan(bet, choice):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  modular = result % 2
  if choice == 'Even' or choice == 'Odd':
    if (choice == 'Even' and modular == 0) or (choice == 'Odd' and modular == 1):
      print('Your choice was {choice}. You won ${bet}'.format(choice=choice, bet=bet))
      return bet
    else:
      print('Your choice was {choice}. You lost ${bet}'.format(choice=choice,bet=bet))
      return -bet
  else:
    print('Wrong Choice')
  return

def pickACard(bet):
  person1 = random.randint(1, 13)
  person2 = random.randint(1, 13)
  if person1 == person2:
    print('It\'s a Tie!')
    return 0
  elif person1 > person2:
    print('You got {person1} and your opponent got {person2}. You won ${bet}.'.format(person1=person1, person2=person2, bet=bet))
    return bet
  else:
    print('You got {person1} and your opponent got {person2}. You lost ${bet}.'.format(person1=person1, person2=person2, bet=bet))
    return -bet
  
def Roulette (bet, guess):
  options = ['Even', 'Odd', 'Black', 'Red']
  result = random.randint(0,37)
  if result == 37:
    result = '00'
  if guess not in options:
    try:
      guess1 = int(guess)
    except:
        print('Wrong Choice')
        return 0
    if guess1 < 0 or guess1 > 36:
      print('Wrong Guess')
      return 0
    result = str(result)
    guess = str(guess)
    if guess == result:
      prize = bet*35
      print('The ball fell in number {result} and you picked {guess}. You won ${prize}'
      .format(result=result, guess=guess, prize=prize))
      return prize
    else:
      print('The ball fell in number {result} and you picked {guess}. You lost ${bet}'
      .format(result=result, guess=guess, bet=bet))
      return -bet
  else:
    if result == 0 or result == '00':
      print('The ball fell in number {result} and your choice was {guess}. You lost ${bet}'
      .format(result=result, guess=guess, bet=bet))
      return -bet
    modular = result % 2
    if (guess == 'Even' and modular == 0) or (guess == 'Odd' and modular == 1):
      print('The ball fell in number {result} and your choice was {guess}. You won ${bet}'.format(result=result, guess=guess, bet=bet))
      return bet
    elif (guess == 'Black' and modular == 0) or guess == 'Red' and modular == 1:
      print('The ball fell in number {result} and your choice was {guess}. You won ${bet}'.format(result=result, guess=guess, bet=bet))
      return bet
    else:
      print('The ball fell in number {result} and your choice was {guess}. You lost ${bet}'.format(result=result, guess=guess, bet=bet))
      return -bet
def check_money (bet):
  global money
  if bet > money:
    print('You don\'t have enough money.')
    return 0

def play (game, bet, guess=None):
  global money
  if check_money(bet) == 0:
    return 0
  if game == pickACard:
    end = game(bet)
  else:
    end= game(bet, guess)
  
  money += end
  print('Now you have $'+ str(money))
  return money

#Call your game of chance functions here 

play(Roulette, 200, 'Even')
play(pickACard, 40)