# Quantum_Games-Damage-based-multiplayer-games-
Quantum calculation for multiplayer damage based games


This script is a quantum version for the multiplayer based game after Qiskit Game Jam inspired me. 

To start with, let's assume we have an "N" number of players.

To deal with this, let's define some basic rules in the game; a player can inflict damage to any player in the game, including himself. Here, the damage is the independent factor. 
For example, a bullet fired by a player won't be connected to him anyhow. The script records the bullet shot, and people affected. The script would give us the damage caused by the bullet to people affected in the game. In case any player is not affected, it would assign zero damage to that player. In this way, we can save memory by not recording the information which is immaterial to our output - like who fired the bullet. 

This is an event-based damage evolution algorithm. An event can be a bullet fired, a grenade exploded or both. 

Here, I used backtracking to do this. 

What could be the output? 
Here, we take "Damage dealt" to the players after the event as our output. Qubit's probability {amplitude ^2} of downstate {|1>} is taken as damage dealt for the corresponding player, mapping [0,1] --> [0,100]. Each qubit represents one player. 

How to calculate damage?
Here, "M" is the number of sources of damage or the type of events. There are M number of damage sources in the quantum circuit of the given algorithm. 

What else to do to generalize it?
Each damage source has its constraints such as if the grenade explodes, is on land or water, and many more, taking this into account this algorithm takes l_1,l_2,...,l_m constraints for 1st,2nd,..., mth source respectively. The qubit q[2n] to q[2n+m-1] qubit is the damage source, and for each damage source, qubit q[2n+m] to q[2n+m+l1-1] is the constraint of that damage source. I take the total number of constraints added to L(l_1+l_2+...+l_m = L), so the mth source constraints are mapped to q[2n+m+l-l_m] to q[2n+m+L-1]. 
The damage dealt by the event is irrespective of the player. It has its source input and its constraints with no connection to the player. Damage dealt here is the "base damage" of the event, and if all the players are in the same position and condition, it will reflect the same amount of damage to each of the affected players. For finding the base damage, we need an MCT(Multiple-Control Toffoli) Gate to the target qubit q[2n+m+L+1], which stores that base damage.\

The Actual Game
Each source qubit starts with an X gate, making it in the downstate {|1>} and then a U3 gate, which takes the input. Each U3 has its predefined rotation in X. The input comes as a boolean for each qubit. If the event was due to 1st source only, first qubit's U3 would receive an input of 1, which will be multiplied by the predefined theta in U3, rotating it by - theta along the x-direction and it will change the downstate to a superposition of up and down. Each constraint qubit has an X gate in the starting taking it to downstate, and it too has a predefined theta in its U3, which rotates the state with - theta in the x-direction and takes boolean to activate it (U3(-theta x boolean,0,0)). For example, for the kth damage source for k<m, the only qubit will come out to be 1 which has U3(Boolean) applied to it. The U3 will rotate such a qubit's state vector to a superposition. Let us assume that the probability of down state is "p" and hence the damage because of that source will be p x 100. If there is no constraint to the damage, the MCT will act on all the qubits finding all the qubits in down state and converting the base damage qubit to the same state as that of the source. 
Remember, each event will have a single active source. With constraints, state of the base damage qubit (on which the MCT is acting) will have a probability of downstate to be equal to that of the multiplication of each constraint qubit probability of being in downstate with that of the source making the base damage weaker than the source. When there is no constraint, multiplication is done by 1, inflicting no change in the base damage. 

Damage to all players, 
Each player has one qubit assigned to them and has an additional constraint qubit that defines the relationship between the event and player. The player qubit starts with a U3 gate consisting of theta = pi with boolean multiplied to it. Whenever the player is involved, corresponding U3 receives boolean as 1 making its state change to down. If the player is not affected, it will receive the input boolean 0, resulting in the collapse of U3; hence the qubit remains in upstate{|0>}.
If "C" number of players are affected by the event, players involved have index p_1th, p_2th,...,p_cth, then, only these qubit's U3 will receive a 1 and rest 0 as an input boolean. We used a CCX gate to combine the player input and the constraint. For example, p_1st player's CCX will transform the upstate of q[2n+m+L] into a superposition where the probability of being in downstate will be equal to the multiplication of the two control qubits. If we see the player qubit is in downstate so the state of q[2n+m+L] will be exactly as the constraint qubit of that player. Now we use another CCX gate to connect the base damage storage qubit, and the player constrains the qubit. The player's qubit is now in a state where the probability of being in downstate will be equal to the multiplication of probability of base damage storage qubit's probability of being in downstate to the q[2n+m+l] state. So as the constraint changes, the Base damage effect on players also changes. A player with more constraint means bigger theta will have less damage as the base damage.




