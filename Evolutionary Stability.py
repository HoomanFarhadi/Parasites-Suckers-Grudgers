import random
import matplotlib.pyplot as plt

"""1. Parasites kill off suckers, then grudgers kill off parasites scenirio:
counter = 1
population_count = 150
iterations = 5100
survival_rate = 0.75
generations = 25
c_benefit = 3
d_benefit = 1
p_count = 35
c_count = 135
g_count = 10
t_count = 0"""

counter = 1
population_count = 150
iterations = 1000
survival_rate = 0.75
generations = 25
c_benefit = 3
d_benefit = 1
p_count = 35
c_count = 135
g_count = 10
t_count = 0

#The above was an attempt to figure out the 1. Parasites kill cooperators 2. Grudgers Kill Parasites scenirio, as described in the Selfish Gene, figure it out (this might be a limitation of the program).
#Read the selfish gene to extend the knowledge of evolutionary stability. Particularly nice guys finish first chapter might have the main discussions of the topic.
#For example in the nice guys finish first chapter it is outlined how the point system must be, so must read and understands reasons behind that chapter's facts. For example need to understand this: Strictly speaking, there is one further condition for the game to qualify as a true Prisoner's Dilemma: the average of the Temptation and the Sucker payoffs must not exceed the Reward. The reason for this additional condition will emerge later.
#Note that the phenomena described where parasites take over than grudgers take over only happens for specifc intitial conditions (important factors are iterations, frequency of each strategy, population limit, etc). Can the initial conditions for which this phenomena will happen be mathematically determined?

def display_frequencies(population,display=True):
    p = 0
    c = 0
    g = 0
    t = 0
    for i in population:
        if i.strategy == "parasite":
            p += 1
        elif i.strategy == "cooperator":
            c += 1
        elif i.strategy == "grudger":
            g += 1
        elif i.strategy == "titfortat":
            t += 1
    if display == True:
        print("Parasites: " + str(p))
        print("Cooperators: " + str(c))
        print("Grudgers: " + str(g))
        print("Tit for tats: " + str(t))
    else:
        return [p,c,g,t]
            
def initialize_population():
    global counter
    population = []
    for i in range(p_count):
        organism = parasite("o"+str(counter),"parasite")
        population.append(organism)
        counter += 1
    for i in range(c_count):
        organism = cooperator("o"+str(counter),"cooperator")
        population.append(organism)
        counter += 1
    for i in range(g_count):
        organism = grudger("o"+str(counter),"grudger")
        population.append(organism)
        counter += 1
    for i in range(t_count):
        organism = titfortat("o"+str(counter),"titfortat")
        population.append(organism)
        counter += 1
    return population

#Too slow for larger population sizes
#Try standard sorting like merge,bubble,quick, among others
#Figure time complexity of different searches that are used

#sortbypoints has time complexity O(nlogn)
def sortbypoints(population):
    population.sort(key=return_points)
    return population

#Check to see if program is actually running as the coding intended
#another way to to the evolve function would be to just keep one population and kill the organisms that are accumulating low points and make the ones that are accumulating lots of points reproduce
#How to make evolve function as efficient and fast as possible
def evolve(initial_population,iterations,survival_rate,population_count):
    global counter
    for i in range(iterations):
        random.shuffle(initial_population)
        for j in range(0,len(initial_population)-1,2):
            first_organism = initial_population[j]
            second_organism = initial_population[j+1]
            first_action = first_organism.action(second_organism.name)
            second_action = second_organism.action(first_organism.name)
            first_organism.memorize(second_organism.name,second_action)
            second_organism.memorize(first_organism.name,first_action)
            first_organism.addpoints(first_action,second_action)
            second_organism.addpoints(second_action,first_action)
    sorted_population = sortbypoints(initial_population)
    intermediate_population = []
    for i in range(len(sorted_population)):
        if random.random() <= ((i+1)/(len(sorted_population)+1)+survival_rate-0.5):
            intermediate_population.append(sorted_population[i])
    final_population = []
    factor = (population_count // len(intermediate_population)) + 1
    for i in intermediate_population:
        for j in range(factor):
            child = eval(i.strategy)("o"+str(counter),i.strategy)
            counter += 1
            final_population.append(child)
    return final_population

def return_points(organism):
    return organism.points

class organism:
    def __init__(self,name,strategy):
        self.name = name
        self.strategy = strategy
        self.points = 0
        self.memory = []
    def action(self,opponent):
        pass
    def memorize(self,opponent,response):
        pass
    def addpoints(self,action,response):
        if action == "c" and response == "c":
            self.points += c_benefit
        elif action == "c" and response == "d":
            self.points += 0
        elif action == "d" and response == "c":
            self.points += (c_benefit + d_benefit + 1)
        elif action == "d" and response == "d":
            self.points += d_benefit
class parasite(organism):
    def action(self,opponent):
        return "d"
class cooperator(organism):
    def action(self,opponent):
        return "c"
class grudger(organism):
    def action(self,opponent):
        if opponent in self.memory:
            return "d"
        else:
            return "c"
    def memorize(self,opponent,response):
        if not opponent in self.memory and response == "d":
            self.memory.append(opponent)
class titfortat(organism):
    def action(self,opponent):
        if opponent in self.memory:
            return "d"
        else:
            return "c"
    def memorize(self,opponent,response):
        if not opponent in self.memory and response == "d":
            self.memory.append(opponent)
        elif opponent in self.memory and response == "c":
            self.memory.remove(opponent)

def user_mediated_simulation():
    initial_population = initialize_population()
    for i in range(generations):
        print("Generation: " + str(i+1))
        display_frequencies(initial_population)
        new_population = evolve(initial_population,iterations,survival_rate,population_count)
        initial_population = new_population
        x = input("Pause...")

def plot_simulation():
    p = []
    c = []
    g = []
    t = []
    x = [i+1 for i in range(generations)]
    initial_population = initialize_population()
    for i in range(generations):
        print("Generation: " + str(i+1))
        data = display_frequencies(initial_population,False)
        p.append(data[0])
        c.append(data[1])
        g.append(data[2])
        t.append(data[3])
        new_population = evolve(initial_population,iterations,survival_rate,population_count)
        initial_population = new_population
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("Generations since Initial Population")
    plt.xticks(range(1,x[-1]+1,1))
    ax.set_ylabel("Number of Organisms")
    plt.plot(x,p,label="Parasites")
    plt.plot(x,c,label="Suckers")
    plt.plot(x,g,label="Grudgers")
    #plt.plot(x,t,label="Tit for Tats")
    plt.legend()
    plt.show()

#user_mediated_simulation()
plot_simulation()


#some parts of the evoluition function process are heuristical (thus may need to be replaced with more rigorously justified processes)
#run evolution simulator function and graph the resutls to see how frequencies of each strategy change over time
#use mathematical probability or other wise to calculate the stability of each strategy (what the frequencies will stabilize at, infer ending frequencies based on initial, quantitively determine how much advantage (this refers to point earning potential most likely) a particular strategy has given the initial distribution of the population, and compare it to the advantage of other strategies (one way to do this is to look at the expected value for how many points that individual will acumulate over a certain number of rounds, need to figure out a solution for when the number of rounds is greater than 1 (recursion is a possible approach), such a solution seems hard, although the case for r approaches infinity is easy)) over time based on c and d benefit values
#for example answer the above question for a population comprised of tit for tats AND parasites, along with all other combinations of 2,3, or 4 strategies, along with considering other possible strategies
#For a given grudger, after how many iterations is he expected to run into a parasite? (given initial frequencies of each species)
#Add more strategies (because currently the lack of strategies means that there is no difference between tit for tat and grudger)
