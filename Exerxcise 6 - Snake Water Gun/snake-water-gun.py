import random

print('Snake🐍 Water🌊 Gun🔫 | Developed by Codifier Akash\n\nS - 🐍\nW - 🌊\nG - 🔫')

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
    print("Computer's Choice - Snake 🐍\n[Developer] - Two snakes meet peacefully\n[Round] - Tied 🎈\n")
    chances = chances + 1
  elif player_decision == 'W' and comp_decision == 'Snake':
    print("Computer's Choice - Snake 🐍\n[Developer] - The snake poisoned the water\n[Round] - You loose 💔\n")
    chances = chances + 1
    comp_score = comp_score - 1
  elif player_decision == 'G' and comp_decision == 'Snake':
    print("Computer's Choice - Snake 🐍\n[Developer] - The gun shot the snake\n[Round] - You won 🎉\n")
    chances = chances + 1
    score = score + 1
  
  elif player_decision == 'S' and comp_decision == 'Water':
    print("Computer's Choice - Water 🌊\n[Developer] - The snake poisoned the water\n[Round] - You won 🎉\n")
    chances = chances + 1
    score = score + 1
  elif player_decision == 'W' and comp_decision == 'Water':
    print("Computer's Choice - Water 🌊\n[Developer] - Two waters got mixed\n[Round] - Tied 🎈\n")
    chances = chances + 1
  elif player_decision == 'G' and comp_decision == 'Water':
    print("Computer's Choice - Water 🌊\n[Developer] - The water ruins the gun\n[Round] - You loose 💔\n")
    chances = chances + 1
    comp_score = comp_score + 1

  elif player_decision == 'S' and comp_decision == 'Gun':
    print("Computer's Choice - Gun 🔫\n[Developer] - The gun shot the snake\n[Round] - You loose 💔\n")
    chances = chances + 1
    comp_score = comp_score + 1
  elif player_decision == 'W' and comp_decision == 'Gun':
    print("Computer's Choice - Gun 🔫\n[Developer] - The water ruins the gun\n[Round] - You won 🎉\n")
    chances = chances + 1
    score = score + 1
  elif player_decision == 'G' and comp_decision == 'Gun':
    print("Computer's Choice - Gun 🔫\n[Developer] - Two guns became friends\n[Round] - Tied 🎈\n")
    chances = chances + 1

if chances > 10:
  if score > comp_score:
    print('Congratulations 🎊! You won the game 🎯')
  elif score < comp_score:
    print('You loose 🙅! Computer won the game. Better luck next time ⏳')
  elif score == comp_score:
    print("It's a tie 🎰")