from random import randint
answerList = open('answerlist.txt', mode='r').read().split('\n')
allowedList = open('allowedlist.txt', mode='r').read().split('\n')

randomWordIndex = randint(0, len(answerList))
randomWord = answerList[randomWordIndex]

over = False
tries = 0

while not over:
    guess = input("Enter your guess: ")
    
    if not(guess in allowedList or guess in answerList):
        print('Not a valid word please try again')
    else:
        for i in range(0,len(randomWord)): 
            if guess[i] in randomWord:
                if randomWord[i] == guess[i]:
                    print("🟩", end=' ')
                else:
                    print("🟨", end=' ')
            else:
                print("⬛", end=' ')

        print('')
        
        if guess == randomWord:
            print('You win')
            over = True 
        
        if tries == 5:
            print('You lose. The word was', randomWord)
            over = True
        
        tries+=1
