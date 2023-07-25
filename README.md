# Liars-Dice-Console-Game

  Created my own vision of Liar's Dice Console Game with up to 11 players and including wild ones mode. 
  
The rules of the games that I followed were:

— The game is played by two to 11 players. Five dice are used per player.  

— The game is round based. Each round, each player rolls a 'hand' of dice.  

— The first player begins his turn by bidding. A bid consists of announcing any face value and a number of dice. This bid is the player's claim as how many dice with that particular value there are on the whole table.  

— Each player has two choices during their turn: to make a higher bid or to challenge the previous bid, by calling the last bidder 'liar'.  

— Rising the bid means that the player may bid a higher quantity of the same face, or any particular quantity of a higher face.   

— If the current player challenges the previous bid, all dice are revealed.  

— If the bid is valid (there are at least as many of the face value as were bid), the bidder wins. Otherwise, the challenger wins.   

— The player who loses a round loses one of their dice.   

— The last player to retain a die is the winner.  

— The loser of the last round starts the bidding on the next round. If the loser of the last round was eliminated, the next player starts the new round.  


— Advanced mode: The 'ones' face of the dice is considered wild — it always counts as the face of the current bid.  

Each of the robots has their own temper and makes a decisions based on it. The game can be played over and over again with the same players with the same tempers as initiated at the beginning. That will improve bots profiling skills and will make them more accurate in predicting bets and accusing in a lie other players.

I used binomal distribution for calculating probability of outcome. 

I put comments in the code to clarify myself, hope to find it useful.

I dare you try to beat my bots! 

Also, try to play another game with the same players to check if their profile skills are good enough to beat you again.

If you have any comments or suggestions, please feel free to share.  

Special Thanks to my most dedicated testers - Simeon and Deyan!

Enjoy!

## Getting started

- Clone the repository

```
git clone https://github.com/bozhimirov/Liars_Dice_Console_Game_OOP
```

- Run the project

```
python main.py
```
## Description

#### **player_utils**
### **player.py**
In players.py are positioned the player class and the human class

### **player_helpers.py**
In player_helpers.py are positioned some functions that help to manage players. A list of all functions:

 - create list of players
 - rotate players
 - return active players
 - check who lose a die
 - choose player to start the game
 - get next player to bid
 - check if players are bluffing
 - actions if someone is called a liar
 - actions if player is human
 - actions if player is bot

#### **utils**

### **betting_helpers.py**
In betting_helpers.py are positioned some functions that help for managing betting proccess. A list of all functions:

- calculate new bet
- action if there is a bet
- place bet
- calculate bet according to temper
- dice modifier for wild mode
- bluff bet

### **helper_functions.py**
In helper functions there are some helper functions for the game. A list of all functions:

- pause
- roll dice
- choose language for the game
- return text

### **list_of_opponents.py**
In this file there is a list with 10 predefined names of opponents


### **output.py**
Here is positioned Output class with methods that prints text on the console. 


### **validators.py**
In this file there is a class Validators with the needed validations as methods. A list with all methods:

- validate action input
- validate username input
- validate answer input
- validate game mode input
- validate human bet 
- validate bet
- validate language

### **tests**
This folder contains test files.

### **test_validate_bet.py**
Here are tests for validator of bets. Here are covered most of the cases.

#### **probability_calculation.py**
Here is placed a function that calculates probability of win based on previous opponent's actions and using binomial distribution

#### **main.py**
Here is the main file of the game.



