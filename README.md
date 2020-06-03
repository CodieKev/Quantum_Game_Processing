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
so the mth source constraint are q[2n+m+l-l_m] to q[2n+m+L-1]. now we know what the qubit represent lets go through their inputs and how they show dammage to the players output qubit.


If you see appart from the player for a specific event the damage delt by the event is irrespective of the player. It has its own source input their own constraints with no connection to the player. Lets call this the "base damage" of the event and if all the players are in the same position and condition it will reflect the same ammount of damage to all of them. Finding the base damage we just need a MCT(Multiple-Control Toffoli) Gate to the qubit q[2n+m+L] which stores that base damage for further use . Lets see how this works.

Each source qubit starts with a X gate makig it in a down state then a U3 gate which takes the input. Each U3 has its predefined rotation in X. The input comes as bullion for each qubit. If the event was due to 1st source only first qubit's U3 will recive an input of 1 which will be multiplied by the predefined theta in U3  rotating it by - thera along x direction and will cange the down state to a suprposition if up and down. And the constraint also act in the similar manner as the damage each constrain qubit has a X gate in the strting taking it to down state and it too have a predefined theta in its U3 which rotated the state with - theta in x direction and taked a bullion to activate it (U3(-theta x bullion,0,0)).  Now assume that the event corrosponds to the kth damage source(k<m) the only that qubit will recive a bullion as 1 and will rotate its state vector to a superposition lets assume that the probability of down state to be "p" so the damagge because of that source will be p x 100, if there is no constrain to the damage the MCT will act on all the qubits finding all the qubits in down state making the base damage qubiit in the same state as the source. Well doing great unlit now, lets add some constraint. Remember each event will have only 1 source active and if no source is active means no damage has to be calculated and program wont be needed for that. After adding some constraiint we see that the state of the base damage storage qubit (on which the MCT is acting) will havve a probability of doen state to be equal to that of the multiplication of each constraint qubit probability of being in doen state with that of the sourse making the base damage weeker then the source. When there were no constraint constraint multiplication was done by 1 inflicting no change in the base damage.



