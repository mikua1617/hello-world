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
  
    
#Problem 3 - Valid Words

def isValidWord(word, hand, wordList):
  flag=1
  handtemp=hand.copy()
  if word in wordList:
    for check in word:
      if handtemp.get(check, 0)<=0:
        flag=0
        break
      handtemp[check]-=1
    
  else:
    return False
  
  if flag==0:
    return False
  else:
    return True
  
  
  
#Problem 4 - Hand Length  

def calculateHandlen(hand):

    length=0
    for counter in hand:
        length += hand[counter]

    return length
