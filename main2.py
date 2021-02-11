"""
M: no of pizzas available in the pizzeria
T2: no of 2-person teams
T3: no of 3-person teams
T4: no of 4-person teams

M lines
I: no of ingredients
L: list of the ingrdients

eg,
3 onion pepper olive

RETURN: maximize per team, the number of different ingredients used in all their 
pizzas
"""
from time import time
from collections import defaultdict

start = time()
def extract_variables(filepath):
    # reading in the input file, a_example
    with open(filepath) as infile:
        data = infile.read()
        data = data.split("\n")

    data_details = []

    for item in data:
        item = item.split()
        data_details.append(item)

    M, T2, T3, T4 = data_details[0] # no. of available pizza, no of people in teams of 2, 3 & 4
    I, L = [], [] # no. of ingredients w corresponding items

    piz_id = 0
    for pizza_deets in data_details[1:]:
        if pizza_deets:
            I.append(piz_id)
            L.append(pizza_deets[1:])
            piz_id += 1
    
    return M, int(T2), int(T3), int(T4), I, L


def solve(filepath):
    """
    Modelling this problem as a graph.
    Keep track of all the ingredients that appear in more than one pizza,
    ingredients with the highest occurence of pizzas would be priortized (testing)
    """

    """
    Sort the pizzas by size in a reverse style, for each of the pizzas,
    compare with others for pairs with least common pizzas
    """
    M, T2, T3, T4, I, L = extract_variables(filepath)
    pizzas = list(zip(I, L))