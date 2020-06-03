# Quantum_Games-Damage-based-multiplayer-games-
Quantum calculation for multiplayer damage based games



In this program, we deal with computing the in-game calculations using quantum computing.

Let's go through the Quantum algorithm for a multiplayer game as its where the real algorithm comes in and the single player will be done in the end.


MULTIPLAYER System 

Let's see the generalized player base "n" number of players.

To deal with the "n" player system we see some basic rules in the game, such as a player can deal damage to anybody in the game including himself. To deal with this system I took the damage as a general factor not connected to a player, for example, a bullet fired by a player won't be connected to him anyhow and the algorithm should take an input that a bullet was fired, these were the people affected and the algorithm will give us the damage caused by that bullet to everyone in the game if the player was not affected by the bullet it will deal no damage to that player by this way we won't be needing waste information like who fired the bullet.

I call this Event based damage evolution algorithm. An event such as bullet fired, a grenade exploded, etc.

Now let's go through how the algorithm acts on its base level. And we will try to do it using Backtracking.

What do we need the program to give output as? Damage dealt to each of the players because of the event just happened. So I mapped the output qubit's probability of being in down state to be equal to damage taken by the corresponding player, mapping 0 to 0 and 1 to 100. For each player, there is an output qubit defined at the end of the circuit.

Now let's see how we calculate damage.

To make this algorithm generalized i too the number of sources for damage to be "m". So there is m number of damage source in this circuit. What more do we need to generalize it? Each damage source has its constraint such as it the grenade exploded was on land or water and many more, taking this into account this algorithm takes l_1,1_2,...,l_m constraint for 1st,2nd,..., mth source respectively. If you see in the figure you can see the qubit q[2n] to q[2n+m-1] qubit to be damage source, and for each damage source qubit q[2n+m] to q[2n+m+l1-1] to constrain of 1st damage source. I took the total number of constraint added to L(l_1+l_2+...+l_m = L)
so the mth source constraint are q[2n+m+l-l_m] to q[2n+m+L-1]. Now we know what the qubit represents let's go through their inputs and how they show damage to the players' output qubit.


If you see apart from the player for a specific event the damage dealt by the event is irrespective of the player. It has its source input their constraints with no connection to the player. Let's call this the "base damage" of the event and if all the players are in the same position and condition it will reflect the same amount of damage to all of them. Finding the base damage we just need an MCT(Multiple-Control Toffoli) Gate to the qubit q[2n+m+L+1] which stores that base damage for further use. Let's see how this works.

Each source qubit starts with an X gate making it in a down state then a U3 gate which takes the input. Each U3 has its predefined rotation in X. The input comes as bullion for each qubit. If the event was due to 1st source only first qubit's U3 will receive an input of 1 which will be multiplied by the predefined theta in U3  rotating it by - theta along the x-direction and will change the down state to a superposition of up and down. And the constraint also acts similarly as the damage each constrain qubit has an X gate in the starting taking it to down state and it too has a predefined theta in its U3 which rotated the state with - theta in the x-direction and take bullion to activate it (U3(-theta x bullion,0,0)).  Now assume that the event corresponds to the kth damage source(k<m) the only that qubit will receive bullion as 1 and will rotate its state vector to a superposition lets assume that the probability of down state to be "p" so the damage because of that source will be p x 100 if there is no constrain to the damage the MCT will act on all the qubits finding all the qubits in down state making the base damage qubit in the same state as the source. Well doing great unlit now, let's add some constraint. Remember each event will have only 1 source active and if no source is active means no damage has to be calculated and the program won't be needed for that. After adding some constraint we see that the state of the base damage storage qubit (on which the MCT is acting) will have a probability of down state to be equal to that of the multiplication of each constraint qubit probability of being in down state with that of the source making the base damage weaker than the source. When there was no constraint, multiplication was done by 1 inflicting no change in the base damage. Now we know how the damage is calculated.

Let's move to the part where we inflect the damage to each of the players.

Each player has its qubit assigned and has an additional constraint qubit that defined the relationship between the event and player.
The player qubit starts with a U3 gate consisting of theta = pi with bullion multiplied to it. Whenever the player is involved, corresponding U3 receives bullion as 1 making its state change to down if the player is not involved it will receive the input of bullion 0 making U3 collapse to an identity gate hence the qubit remains in up state.

Let's say "c" number of players were affected by the event, players involved has index p_1th, p_2th,...,p_cth. Only these qubit's U3 will receive a 1 and rest 0 as an input. Starting with p_1th player. It received a 1 in its input and got hanged to a down state. Now its corresponding constraint qubit receives a theta between [0, pi] depending upon the relation with the damage source. If the player was meant to be least affected, he will receive a greater theta value. Let's see how this sets things up. We used a CCX gate to combine the player input and the constraint. Our p_1st player CCX will transform the up state of q[2n+m+L] into a superposition where the prob of being in down state will be equal to multiplication of the two control qubits. If we see the player qubit is in down state so the state of q[2n+m+L] will be exactly as the constraint qubit of that player. Now we use another CCX gate to connect the base damage storage qubit and the player constrains qubit. Using this set the player's qubit to a state where the probability of being in down state will be equal to the multiplication of probability of base damage storage qubit down state to the q[2n+m+l] state means the player constraint state's probability being in down state. So as the constraint changes the Base damage effect on players also changes. A player with greater constraint means greater theta will have less damage as the base damage will get multiplied with a lesser probability of down state. Noe when the calculation for one of the player is down the q[2n+m+L] is returned to up state for another player's calculation to be performed. If a player is not affected by the event he will receive bullion of 0 keeping the qubit into up state which will in turn make the q[2n+m+L] be in up state and eventually the player's output qubit in an up state resulting in zero damage inflected on that player.



