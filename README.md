# Quantum_Games-Damage-based-multiplayer-games-
Quantum calculation for multiplayer damage based games



In this program we deal with computing the in-game calculations using quantum compute.

Lets go through the Quantum algorithm for multiplayer game as its where the real algorithm comes in and the single player will be done in the end.


MULTIPLAYER System 

Lets see the generalised player base "n" number of players.

To deal with the "n" player system we see some basic rules in the game, such as a player can deal dammage to anybody in the game including himself. To deal with this system I took the damage as a general factor not connected to a player, for example a bullet fired by a player wont be conncted to him anyhow and the algorithm should take an input that a bullet was fired , these were the  people affected and the algorithm will give us the damage caused by that bullet to every one in the game if the player was not affected by the bullet it will deal no damage to that player by this way we wont be needng waste infomation like who fired the bullet.

I call this Event based damage evolution algorithm. Event such as bullet fired , greaned exploded etc.

Now lets go through how the algorithm acts on its base level. And we will try to do it using Backtracking.

What do we need the program to give output as? Damage delt to each of the player because of the event just happned. So I mapped the output qubit's probability of being in down state to be equal to damage taken by the corrosponding player, mapping 0 to 0 and 1 to 100. For each player there is a output qubit defined at the end of the circuit.

Now lets see how we calacuate damage.

To make this algorithm generalised i too the number of source for damage to be "m". So there are m number of damage source in this circuit. What more do we need to generalse it? Each damage sourse has its own constraint such as it the greanade exploded was on land or water and many more, taking this into account this algorithm takes l_1,1_2,...,l_m constraint for 1st,2nd,...,mth source respectively. If you see in the figure you can see the qubit q[2n] to q[2n+m-1] qubit to be dammage source, and for each damage source qubit q[2n+m] to q[2n+m+l1-1] to be constrain of 1st ddamage source. I took the took the total number of constraint added to L(l_1+l_2+...+l_m = L)
so the mth source constraint are q[2n+m+l-l_m] to q[2n+m+L-1]

