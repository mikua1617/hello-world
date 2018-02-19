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

  
#problem 5 -   Playing a Hand
  
def playHand(hand, wordList, n):
    

    # Keep track of the total score
    score=0
    # As long as there are still letters left in the hand:
    while len(hand)>0:


        # Display the hand
        displayHand(hand)
        # Ask user for input
        word=input("enter word or a" + " '.' " + "to indicate that you're finished: ")
        # If the input is a single period:
        if word==".":

            break
            # End the game (break out of the loop)

        else:


        # Otherwise (the input is not a single period):

            # If the word is not valid:
            if isValidWord(word, hand, wordList)==False:

                # Reject invalid word (print a message followed by a blank line)
                print("invalid word! please try again.")

            # Otherwise (the word is valid):
            else:
                score+=getWordScore(word, n)
                print(word, "earned", getWordScore(word, n), "points,", "Total:", score, "points")
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                # Update the hand 
                hand=updateHand(hand, word)

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print("Game Over. Total score=", score)
    print(" ")
    
    
    
# Problem 6 - playing a game




def playGame(wordList):
    """

    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    gamechoose="a"

    while gamechoose!="e":


        gamechoose=input("enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if gamechoose == "n":
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif gamechoose == "r":
            playHand(hand, wordList, HAND_SIZE)
        elif gamechoose == "e":
            print("thank you for playing!")
        else:
            print("invalid entry, please try again")
            


  #problem 7 - You and your computer
  
  
  
  def playGame(wordList):
    
    gamechoose = "a"
    player="a"

    while gamechoose != "e":

        gamechoose = input("enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if gamechoose == "n":
            hand = dealHand(HAND_SIZE)


        elif gamechoose == "e":
            print("thank you for playing!")
            break
        else:
            print("invalid entry, please try again")

        while player!="u" and player!="c":
            if gamechoose=="e":
                break

            player=input("enter u to play yourself and c for the computer to play")
            if player!="u" and player!="c":
                print("invalid entry. Please try again")

        if player =="u":
            playHand(hand, wordList, HAND_SIZE)
        elif player =="c":
            compPlayHand(hand, wordList, HAND_SIZE)




