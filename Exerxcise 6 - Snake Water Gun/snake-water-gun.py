import random

print('Snakeπ Waterπ Gunπ« | Developed by Codifier Akash\n\nS - π\nW - π\nG - π«')

chances = 1
score = 0
comp_score = 0

while chances <= 10:
  comp_decision_options = [
      'Snake',
      'Water',
      'Gun'
  ]

  print(f'Round - {chances}/10\nScore - {score}')
  player_decision = str(input('Your choice - ').capitalize())
  comp_decision = random.choice(comp_decision_options)
  
  if player_decision == 'S' and comp_decision == 'Snake':
    print("Computer's Choice - Snake π\n[Developer] - Two snakes meet peacefully\n[Round] - Tied π\n")
    chances = chances + 1
  elif player_decision == 'W' and comp_decision == 'Snake':
    print("Computer's Choice - Snake π\n[Developer] - The snake poisoned the water\n[Round] - You loose π\n")
    chances = chances + 1
    comp_score = comp_score - 1
  elif player_decision == 'G' and comp_decision == 'Snake':
    print("Computer's Choice - Snake π\n[Developer] - The gun shot the snake\n[Round] - You won π\n")
    chances = chances + 1
    score = score + 1
  
  elif player_decision == 'S' and comp_decision == 'Water':
    print("Computer's Choice - Water π\n[Developer] - The snake poisoned the water\n[Round] - You won π\n")
    chances = chances + 1
    score = score + 1
  elif player_decision == 'W' and comp_decision == 'Water':
    print("Computer's Choice - Water π\n[Developer] - Two waters got mixed\n[Round] - Tied π\n")
    chances = chances + 1
  elif player_decision == 'G' and comp_decision == 'Water':
    print("Computer's Choice - Water π\n[Developer] - The water ruins the gun\n[Round] - You loose π\n")
    chances = chances + 1
    comp_score = comp_score + 1

  elif player_decision == 'S' and comp_decision == 'Gun':
    print("Computer's Choice - Gun π«\n[Developer] - The gun shot the snake\n[Round] - You loose π\n")
    chances = chances + 1
    comp_score = comp_score + 1
  elif player_decision == 'W' and comp_decision == 'Gun':
    print("Computer's Choice - Gun π«\n[Developer] - The water ruins the gun\n[Round] - You won π\n")
    chances = chances + 1
    score = score + 1
  elif player_decision == 'G' and comp_decision == 'Gun':
    print("Computer's Choice - Gun π«\n[Developer] - Two guns became friends\n[Round] - Tied π\n")
    chances = chances + 1

if chances > 10:
  if score > comp_score:
    print('Congratulations π! You won the game π―')
  elif score < comp_score:
    print('You loose π! Computer won the game. Better luck next time β³')
  elif score == comp_score:
    print("It's a tie π°")