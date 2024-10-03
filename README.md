# AI_hangman
A game of hangman, made with assistance from ChatGPT.

  The program randomly selects a 'WORD' from a list, and displays a "_" for each character in the 'WORD'.
  The player is given 10 'ATTEMPTS' to guess the 'WORD'.
  If 'ATTEMPTS' decreases to 0, the game ends in a loss.
  
The user/player is asked for an input;
  - the player guesses a single 'LETTER':
    + the guess is correct -> every instance of the 'LETTER' in the 'WORD' is revealed ("_" is replaced with the 'Letter').
    + the guess is incorrect -> no 'LETTERs' are revealed, 'ATTEMPTS' decreases by 1.
  - the player attempts to guess the 'WORD':
    + the guess is correct -> 'WORD' is revealed, player wins.
    + the guess is incorrect -> no 'LETTERs' are revealed, 'ATTEMPTS' decreases by 1.

Once the game has ended (in either a win or a loss) the player is asked if they want to play again.
  - if the player chooses "yes": the program randomly chooses a new 'WORD' and the game begins again.
  - if the player chooses "no": the program closes*
      * NOTE: the program actually crashes *






Done:
  + Integrate tKinter
  + Increase size of GUI --- (GUI)
  + Allow 'Enter'-key to submit guess (bypass clicking button) --- (KEYPRESS)
  + Allow player to guess the entire word --- (GUESS-WORD)
  + Remove online dependency for full functionality --- (DICTIONARY)
  + Replay option -> On game end, ask player to play again, 'yes' to continue, 'no' to quit. --- (REPLAY)

Ready to merge:

To Do:
  + Optional:
      - Further tweak GUI --- (GUI-TWEAK)
      - Show the word definition when the game ends; --- (DEFINITION)
        + (link to online dictionary?)
