import random
import turtle
import math
import copy

def student_details():
    # add variables to store student ID and username to be returned
    student_id = 17035066
    student_username = "mb18acr"
    
    return student_id, student_username
 
def generate_map(x_range, y_range, locations):
    # add code to create a list then use a for loop to create a random population for this list
    generated_map = []
    
    for i in range(locations) : 
        x = random.randint (-x_range, x_range)
        y = random.randint(-y_range,y_range)
        generated_map.append([x,y])
        
    return generated_map

def print_map(speed, color, thickness, selected_map):
    print("printing map")
    # add code to use the turtle to draw the path between all destinations
    # the turtle should make use of the parameters provided: speed. color, etc...
    # you will need to use a loop in order to draw the path to all locations

    jerry = turtle.Turtle()
    jerry.speed(speed)
    jerry.pencolor(color)
    jerry.penup()
    jerry.pensize(thickness)
    jerry.setpos(selected_map[0][0], selected_map[0][1])
    
    print(selected_map[0][0], selected_map[0][1])    
        
    for i in range (len(selected_map)-1):
        jerry.pendown()
        jerry.goto(selected_map[i][0], selected_map[i][1])
        # jerry.pencolor("green") used to check where turtle was starting
             
def calculate_distance(starting_x, starting_y, destination_x, destination_y):
    distance = math.hypot(destination_x - starting_x, destination_y - starting_y)  # calculates Euclidean distance (straight-line) distance between two points
    return distance

def calculate_path(selected_map):
    # you will need to setup a variable to store the total path distance
    # you will need to use a loop in order to calculate the distance of the locations individually
    # it would be wise to use make use of the calculate_distance function as you can reuse this
    # remember your need to calculate the path of all locations returning to the original location
    
    distance = 0

    for i in range (len(selected_map)-1):
        distance += calculate_distance(selected_map[i][0], selected_map[i][1], selected_map[i+1][0], selected_map[i+1][1])

    distance += calculate_distance(selected_map[-1][0], selected_map[-1][1], selected_map[0][0], selected_map[0][1])

    return distance

#################################################################################################

def nearest_neighbour_algorithm(selected_map):

    temp_map = copy.deepcopy(selected_map)

    optermised_map = []
    optermised_map.append(temp_map.pop())

    # you need to create an empty list for your optimised map 
    for x in range(len(temp_map)):
        
        # you need to add some variables to store establish the closest location
        closest_coord = 100
        closest_i = 0
        
        
        for i in range(len(temp_map)):
            current_coord = calculate_distance(optermised_map[-1][0], optermised_map[-1][1], temp_map[i][0], temp_map[i][1])
            # you need to calculate the distance between the current path and the next potential location
            # it would be wise to use make use of the calculate_distance function

            #print("Distance" + distance)
                
            if current_coord < closest_coord :
                closest_coord = current_coord
                closest_i = i
               # print("Closest Coord" + closest_coord)
                
                # you will need to write an if statement to establish if the current distance is lower than the stored
                # best distance, and if so set the best distance to the current location
            
            
        optermised_map.append(temp_map[closest_i])

        del temp_map[closest_i]

        # the final step is to add the closest location to the optermised_map and remove from the temp_map
        
        
    return optermised_map

#################################################################################################

def genetic_algorithm(selected_map, population, iterations, mutation_rate, elite_threshold):

    # this is the main genetic algorithm function and should make use of the inputs and call the sub functions in order to run

    # you will need to call the create_population function and store this in a list
    create_population(population, selected_map)
    # you will then need to use the iterator function and store the returned solution to best_solution

    return best_solution

def create_population(population, selected_map):

    # you need to create an empty list called gene_pool for the population
    gene_pool = []
    # use a for loop and the provided inputs to create the population 
    for x in range (population) :
        gene_pool.append(copy.deepcopy(selected_map))
        random.shuffle(gene_pool[x])     
    # you will also need to randomise the individuals within the population
    return gene_pool

def fitness_function(gene_pool, best_solution):
    # you need to find a way to rank the fitness of your population. one way you may consider doing this is with a ranked list
    # you will need to have correctly implemented the calculate_path function in order to rank the fitness of the population
    # you may consider using a loop to achieve this
    # your function must return a sorted gene pool that is sorted by fittest (shortest path to longest path
    # your function should also return the fittest individual in best_solution
    
    sorted_gene_pool = null
    ranking = []

    for i, x in enumerate(gene_pool) :
        
        score = calculate_path(x)
        ranking.append(score)
        if score < best_solution :
            old_best = best_solution
            best_solution = score
    
        sorted_gene_pool = [x for _, x in sorted(zip(ranking,gene_pool))]
        
    return sorted_gene_pool, best_solution

def iterator(gene_pool, iterations, mutation_rate, elite_threshold):
    # you need to use the provided inputs to iterate (run) the algorithm for the specified iterations
    # you will need to use a for loop in order to achieve this
    # in order for this function to work all over parts of the algorithm must be complete
    # the function must return the best individual (best_solution) in the population

    
    return best_solution

def mating_function(gene_pool, best_solution, mutation_rate, elite_threshold):
    # you need to create a new list called new_gene_pool to store the newly created individuals from this function
    # you will need to use a loop in order to perform the genetic crossover and mutations for each individual
    # in order for this function to work correctly you need to select the parent genes based to create the child
    # one of the top individuals based on the elite_threshold should be selected as one of the parents
    # once both parents have been chosen the breed function should be called using both of these parents
    # this means the breed function must be working and returning a child
    # once the breed function has returned a new individual this individual needs to be mutated
    # this means you need to implement the mutate function and it must return the mutated child
    # the function must return a new generation of individuals in new_gene_pool

    return new_gene_pool

def breed(parent_1, parent_2):
    # you need to select random points in which to cut the genes of the parents and put them into the child
    # because the individual must contain all of the locations (this is a unique issue to the TSP) the gene selection is slightly more difficult
    # one suggested way is to selected portions of genetic data from one parent then fill in the remainder of locations from the other parent
    # the portion of genes selected should be random and you may want to use some for loops to achieve this
    # the function must return a child of the 2 parents containing all the locations in the original map
    a = len(parent_1)
    b = len(parent_2)
    cut = []
    dna1 = []
    dna2 = []
    cut.extend ([random.randint(0,a), random.randint(0,b)])
    cut.sort()

    for i in range(cut[0], cut[1]):
        dna1.append(parent_1[i])
    dna2 = [item for item in parent_2 if item not in dna_1]

    child = dna1 + dna2
    
    return child

def mutate(child, mutation_rate):
    # this function must mutate the genes of the child based on the mutation rate provided
    # to achieve this you may want to use a for loop to go through the child
    # then use a random number with an if statement according the mutation rate
    # selected genes will then need to be swapped
    # the function must return a child containing all the locations in the original map but not as it originally arrived
    for switch in range(len(child)) :
        if random.random < mutation_rate :
            switched = random.randint(0,len(child)-1)
            gene1 = child[switch]
            gene2 = child[switched]

            child[switch] = gene2
            child[switched] = gene1
            
    mutated_child = child
    
    return mutated_child
