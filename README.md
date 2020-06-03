# Quantum_Games-Damage-based-multiplayer-games-
Quantum calculation for multiplayer damage based games



In this program we deal with computing the in-game calculations using quantum compute.

Lets go through the Quantum algorithm for multiplayer game as its where the real algorithm comes in and the single player will be done in the end.


MULTIPLAYER System 

Lets see the generalised player base "n" number of players.

To deal with the "n" player system we see some basic rules in the game, such as a player can deal dammage to anybody in the game including himself. To deal with this system I took the damage as a general factor not connected to a player, for example a bullet fired by a player wont be conncted to him anyhow and the algorithm should take an input that a bullet was fired , these were the  people affected and the algorithm will give us the damage caused by that bullet to every one in the game if the player was not affected by the bullet it will deal no damage to that player by this way we wont be needng waste infomation like who fired the bullet.

I call this Event based damage evolution algorithm. Event such as bullet fired , greaned exploded etc.

Now lets go through how the algorithm acts on its base level. And we will try to go it usig Backtracking.

What do we need the program to give output as? We want it to give the damage delt to each of the player 
