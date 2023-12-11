# AI_hangman
A game of hangman, generated py ChatGPT, with minor tweaks by human hand.

Done:
  + Integrate tKinter
  + Increase size of GUI --- (GUI)
  + Allow 'Enter'-key to submit guess (bypass clicking button) --- (KEYPRESS)

Ready to merge:
  + Allow player to guess the entire word --- (GUESS-WORD);
      - Otherwise only allow players to enter a single letter -> player not able to enter more than 1 character(letter) at a time.
  + Remove online dependency for full functionality (https://randomwordgenerator.com/json/words.json) --- (DICTIONARY)

To Do:
  + Optional:
      - Further tweak GUI --- (GUI-TWEAK)
      - Replay option -> On game end, ask player to play again, 'yes' to continue, 'no' to quit; --- (REPLAY)
        + possibly buttons, maybe keypresses (y/n)
      - Show the word definition when the game ends; --- (DEFINITION)
        + (link to online dictionary?)
