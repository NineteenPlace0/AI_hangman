# AI_hangman
A game of hangman, generated py ChatGPT, with minor tweaks by human hand.

Done:
  + Integrate tKinter
  + Increase size of GUI

Ready to merge:
  + Allow 'Enter'-key to submit guess (bypass clicking button) --- (KEYPRESS)
  + Allow player to guess the entire word --- (GUESS-WORD);
      - Otherwise only allow players to enter a single letter -> player not able to enter more than 1 character(letter) at a time.
  + Remove online dependency for full functionality (https://randomwordgenerator.com/json/words.json) --- (DICTIONARY)

To Do:
  Optional:
    - Further tweak GUI
    - Replay option -> On game end, ask player to play again, 'yes' to continue, 'no' to quit;
      + possibly buttons, maybe keypresses (y/n)
