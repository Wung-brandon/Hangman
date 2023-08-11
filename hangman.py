
import random

name_list = ['boris','perez','brandon','perkins','wung','venia','herbert','salim',
             'sharihou','gina','steve','obi','emmanuel','george','santi','ojong',
             'lucas','bertrand','grace','ashley','besong','henry','courage','henry',
            'matilda','babila','jimmy','tita','wisdom','carlos','messi','ronaldo' ]

#randomly choose a word from name_list
chosen_word = random.choice(name_list)
print(chosen_word)
#creating an empty list called display and replacing it with an underscore _ using a for loop 
display = []
for _ in range(len(chosen_word)):     #for _ in chosen_word:
    display += "_"
#print(display)

lives = 6
end_of_game = False
while not end_of_game:
    #ask a user a guess a letter from the choosen word
    user_guess = input("Enter a letter that is in the chosen word:").lower()
    if user_guess in display:
        print(f'You have already guessed {user_guess}')

    #loop through each position in the chosen word;
    #if the letterat that position matches the 'user_guess' then reveal that the
    #letter in the display at that position

    #looping through the chosen word and checking if the letter the user guesses is
    #equal to the any of the letters in the chosen word 
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #print(letter)
        if letter == user_guess: 
            display[position] = letter
    #if user guess is not in the chosen word then reduce lives by 1.
    #if lives goes down to 0 then the game should stop andprint you lose     
    
    if user_guess not in chosen_word:
        print(f'You have a guessed {user_guess} that is not in the word. You lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
        

    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win!")