from random import randint

known_joke = ['Knock knock',
              'rock rock',
              'block block']
while True:
  input = raw_input()
  if input == 'Good morning':
    print 'Good morning. How are you?'
  elif input == 'I\'m not happy...':
    print 'Why?'
  elif input == 'Tell me a joke':
    print known_joke[randint(0, 2)]
  elif input[:7] == 'because':
    print 'why do you think ' + input[8:].replace('I\'m', 'you are').replace('I', 'you') 
  

    

