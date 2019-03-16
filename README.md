# Parasites-Suckers-Grudgers
A simulation of evolutionary stability phenomena as explored by Richard Dawkins in The Selfish Gene.

### Ideas and Implementation
This simulation was an attempt to recreate some of the ideas that were presented mostly in The Selfish Gene | Chapter 12: Nice Guys Finish First. The main context of this chapter is that of an evolutionary stable strategy (ESS). A strategy is a specific policy that governs an orgasmim's behavior in a competitive evolutionary enviroment. An ESS is a strategy which once "widespread" is resistant to change, ie alternative strategies will not be successful in gaining an evolutionary advantage when competiting with it. For example, in this case we have organisms which can either "cooperate" or "defect. Each time two organism meet they have two choose one of these two actions, and get rewarded or punished based on their own as well as their opponent's choice. An example of the payoffs for each action pair is demonstrated in the following table (the top row indicates the action a certain organism chooses, the left column their opponent's action, and the numbers for each pair indicating that certain orgasmism's payoff):

                Defect     Cooperate

    Defect        1            0            

    Cooperate     5            4

For example, these payoffs could represent apes grooming each other's backs (the example given in the Selfish Gene). The cost of grooming another's back is only 1 point (time and energy consumption), but the cost of remaining ungroomed is 4 points (because of the potential for parasites and disease to develop). As such, if two apes defect (reject to groom one another), they get a 1 point payoff from not having to spend time and energy. If one ape grooms the other but the other does not reciprocate, the ape that gets groomed gets both 4 points for being cleaned and 1 point for not having to spend any time and energy, while the other ape gets 0 points because they both spent time and energy grooming the other but remained infested themselves. If both cooperate they each get 4 points for being rid of a potential parasite infestation.

The payoffs could be thought of more rigorously. In the above example, the payoffs were chosen as to corrospond to some biological reality, and thus their quantification depended very much on the context of scenerio. More abstractly, we could set up a system of constraints that would determine the set of all payoffs which are theoritically plausible. These constraint could be anything and yield many interesting payoffs (perhaps not biologically plausible). Indeed, they would very much affect the determinance of the optimal policy(ies), any ESS's, and the results of simulations. It is interesting to think about and play around with different payoffs and constraints. However, for now, we just present a basic set of constraints to model biological reality:
* We start off with a constant number of points (in the above case 5)
* Defect from the opponent results in a certain number of points d > 0 being taken away from the base amount (in the above d = 4)
* Cooperation on our part results in a certain number of points c > 0 being taken away from the base amound (in the above c = 1)
* In most cases d > c because the penalty of being defected on by the opponent is often much higher than cooperating ourselves (for example in the above example retaining parasites could result in disease and death, while wasting time and energy grooming another is only a minor concern).

Once the payoffs are decided, we can create our organism classes. Each organism has a name (the name of its species so to say, which would define its behavior), a strategy, a memory, and a number indicating how many points it has accumulated. In the module, the following four species of organisms were implemented:
*Sucker:

### Figures

<!-- Explanation, how to use, observations, next steps -->
<!-- Incomplete -->
