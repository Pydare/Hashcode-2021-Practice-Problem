from time import time

start = time()
def extract_variables():
    # reading in the input file, a_example
    with open("e_many_teams.in") as infile:
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

    return M, T2, T3, T4, I, L

a, b, c, d, e, f = extract_variables()
print(d[:10])

print("Program took " + str(time() - start) + " seconds")