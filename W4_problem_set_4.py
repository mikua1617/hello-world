#Problem 1 - Word Scores

def getWordScore(word):
  score=0
  for counter in word:
    score+=SCRABBLE_LETTER_VALUES[counter]
  
  score=score*len(word)
    
  if len(word)==HAND_SIZE:
    score+=50
  
  return score

#Problem 2 - Dealing with Hands

def updateHand(hand, word):
  remhand=hand.copy()
  for keys in word:
    if hand.get(keys, 0)!=0:
      remhand[keys]-=1
      
  return remhand      
  
    
