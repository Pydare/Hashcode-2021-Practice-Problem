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
    Bruteforce is to sort the pizza id and details,
    then priortize T4, then T3, then T2 to score max
    points.
    """
    M, T2, T3, T4, I, L = extract_variables(filepath)
    pizzas = list(zip(I, L))
    pizzas.sort(key=lambda x:len(x[1]), reverse=True) # sorted by highest pizzas
    print(pizzas[:3])

    team_results = defaultdict(list) # value is a list of lists (list of pizza ids)
    i, deliveries = 0, 0
    while i < len(pizzas):
        if i + 4 <= len(pizzas) and T4 > 0:
            ids = []
            for j in range(i, i+4):
                ids.append(str(j))
            team_results["T4"].append(ids)
            T4 -= 1
            i += 4
        elif i + 3 <= len(pizzas) and T3 > 0:
            ids = []
            for j in range(i, i+3):
                ids.append(str(j))
            team_results["T3"].append(ids)
            T3 -= 1
            i += 3
        elif i + 2 <= len(pizzas) and T2 > 0:
            ids = []
            for j in range(i, i+2):
                ids.append(str(j))
            team_results["T2"].append(ids)
            T2 -= 1
            i += 2
        else:
            break
        deliveries += 1

    
    return team_results, deliveries


def export_variables(infile, outfile):
    """
    The first line of the file is the no. of deliveries
    The rest of the lines are team number and id of pizzas
    {1:[3,4,6]}
    """
    team_results, deliveries = solve(infile)
    res = [str(deliveries)] # initializing the outfile content

    # looping through the results
    for key in team_results.keys():
        temp = ""
        temp += str(key[-1]) + " "

        for val in team_results[key]:
            temp += " ".join(val)
            #temp += "\n" # for the purpose of writelines (outfile)
            res.append(temp)
            temp = temp[:2]

    # writing to a submission.txt file
    with open(outfile, "w") as file:
        for item in res:
            file.write(item + "\n")

def export_variables_direct(infile, outfile):
    """
    The first line of the file is the no. of deliveries
    The rest of the lines are team number and id of pizzas
    {1:[3,4,6]}
    """
    team_results, deliveries = solve(infile)
    f = open(outfile, "w")
    f.write(str(deliveries) + "\n")

    # looping through the results and direct into the file
    for key in team_results.keys():
        temp = ""
        temp += str(key[-1]) + " "

        for val in team_results[key]:
            temp += " ".join(val)
            temp += "\n"
            f.write(temp)
            temp = temp[:2]

    f.close()


def run():
    infile = "input/e_many_teams.in"
    outfile = "output1/submission_e.txt"
    export_variables_direct(infile, outfile)

run()
print("Program took " + str(time() - start) + " seconds")