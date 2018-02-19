#Problem 1 - Word Scores

def getWordScore(word):
  score=0
  for counter in word:
    score+=SCRABBLE_LETTER_VALUES[counter]
  
  score=score*len(word)
    
  if len(word)==HAND_SIZE:
    score+=50
  
  return score
      
    
