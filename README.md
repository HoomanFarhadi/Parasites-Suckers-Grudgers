# Parasites-Suckers-Grudgers
A simulation of evolutionary stability phenomena as explored by Richard Dawkins in The Selfish Gene.

### Ideas and Implementation
This simulation was an attempt to recreate some of the ideas that were presented in The Selfish Gene | Chapter 12: Nice Guys Finish First. The main context of this chapter is that of an evolutionary stable strategy (ESS). A strategy is a specific policy that governs an organism’s behavior in a competitive evolutionary environment. An ESS is a strategy which once "widespread" is resistant to change, i.e. alternative strategies will not be successful in gaining an evolutionary advantage when competing with it. For example, in this case we have organisms which can either “cooperate” or “defect”. Each time two organism meet they have two choose one of these two actions, and get rewarded or punished based on their own as well as their opponent's choice. An example of the payoffs for each action pair is demonstrated in the following table (the top row indicates the action a certain organism chooses, the left column their opponent's action, and the numbers for each pair indicating that certain organism's payoff):

                Defect     Cooperate

    Defect        1            0            

    Cooperate     5            4

For example, these payoffs could represent apes grooming each other's backs (the example given in the Selfish Gene). The cost of grooming another's back is only 1 point (time and energy consumption), but the cost of remaining ungroomed is 4 points (because of the potential for parasites and disease to develop). As such, if two apes defect (reject to groom one another), they get a 1 point payoff from not having to spend time and energy. If one ape grooms the other but the other does not reciprocate, the ape that gets groomed gets both 4 points for being cleaned and 1 point for not having to spend any time and energy, while the other ape gets 0 points because they both spent time and energy grooming the other but remained infested themselves. If both cooperate they each get 4 points for being rid of a potential parasite infestation.

The payoffs could be thought of more rigorously. In the above example, the payoffs were chosen as to correspond to some biological reality, and thus their quantification depended very much on the context of scenario. More abstractly, we could set up a system of constraints that would determine the set of all payoffs which are theoretically plausible. These constraint could be anything and yield many interesting payoffs (perhaps not biologically plausible). Indeed, they would very much determine the optimal policy(ies), any ESS's, and the results of the simulations. It is interesting to think about and play around with different payoffs and constraints. However, for now, we just present a basic set of constraints to model biological reality:
* We start off with a constant number of points (in the above case 5)
* Defect from the opponent results in a certain number of points d > 0 being taken away from the base amount (in the above d = 4)
* Cooperation on our part results in a certain number of points c > 0 being taken away from the base amount (in the above c = 1)
* In most cases d > c because the penalty of being defected on by the opponent is often much higher than cooperating ourselves (for example in the above example retaining parasites could result in disease and death, while wasting time and energy grooming another is only a minor concern).

Once the payoffs are decided, we can create our organism classes. Each organism has a name (a id unique to that particular organism), a strategy (which can be thought of as its species), a memory, and a number indicating how many points it has accumulated. In the file Evolutionary Stability.py, the following four species of organisms were implemented:
* Sucker: Cooperates every time.
* Parasite: Defects every time.
* Grudger: Remembers the name of the organisms who have defected and defects in response to them every time it encounters them in the future. Otherwise cooperates.
* Tit for Tat: Responds with the action that the opponent played in their previous encounter if it has seen the opponent before, otherwise cooperates.

Each of these strategies is an inherited class of the general organism class, and has class methods like memorize() (for grudger and tit for tat), action() (for all organisms to determine their action) and addpoints() (for all organisms to add the payoffs).

initialize_population() initializes a starting population of organisms based on predefined frequencies, and returns a list of organism objects representing the population.

evolve() takes an initial population, a population capacity, and a survival rate and evolves that population to the next generation. The details of this are straightforward according to natural selection:
* On each iteration, organisms are paired randomly
* Each pair plays one set of actions against each other and the payoffs are added
* This is repeated for a set number of generations
* At the end of the iterations, the organisms are sorted by their points
* The lowest scoring organisms are then deleted according to the survival rate and a bit of randomness as to reflect the true evolutionary process
* The remaining organisms than "reproduce" to return the population back to its capacity
* The new population is returned

Finally, the function user_mediated_simulation() allows the user to step through a set number of generations of a population, with the population frequencies being printed for each generation. The function plot_simulation() does this automatically and displays the frequencies of each type of organism over time in a line graph.

### Figures
One particularly interesting phenomena occurs for populations of parasites, cooperators, and grudgers (this is mentioned in the book) for very sensitive initial conditions (it was very tedious to recreate these necessary frequencies, especially because the evolution function relies on randomness). Here is what occurs:
1. There is an initial population with large numbers of suckers, a reasonable number of parasites, and a small number of grudgers
2. The parasites start increasing in number due to their success over the suckers, whose numbers decrease. The grudgers remain few in number but do not die off.
3. The parasites kill off all the suckers and peak. The numbers of grudgers remain low but steady.
4. The numbers of grudgers start to increase, at the expense of the parasite population.
5. The grudgers reach an immense population, killing off all the parasites. The situation is stable from there on.

Figures 1 and 2 illustrate this.

This phenomena illustrates the notion of ESS and stable states particularly well. In the beginning, the state is unstable because parasites are superior to suckers. The grudgers have a harder time accumulating points than parasites, but they are able to reap the benefits of mutual cooperation with their own kind and the suckers, which makes up for their losses to the parasites and keeps them in the game. After the suckers have died off and parasites become dominant, the state is still unstable because now with no suckers, the grudgers are superior to the parasites. They reap the benefits of mutual cooperation in their own groups, while the parasites, constantly defecting, eventually receive no more cooperation from the grudgers and thus fall behind. The grudgers than overtake them and kill them off. This final state is stable. Also, grudger is the only ESS because it is the only one that cannot be beaten by the other two strategies.

However in the simulations this situation often did not occur; instead the grudgers were killed off early on and the parasites were the only ones to remain. This is illustrated in figure 3.

<!-- Explanation, how to use, observations, next steps -->
<!-- Incomplete -->
