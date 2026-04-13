#MapPlot.py
#Name: Mariana Chavez
#Date: 04.12.2026
#Assignment: Lab 10

import matplotlib.pyplot as plt

myFile = open("reaction_time_data.csv", "r")

trials = []
reaction_times = []

firstLine = True

for line in myFile:
    if firstLine:
        firstLine = False
        continue

    information = line.strip().split(",")

    trial = int(information[0])
    reaction_time = float(information[1])

    if reaction_time > 0:
        trials.append(trial)
        reaction_times.append(reaction_time)

myFile.close()

print("Trials:", trials)
print("Reaction Times:", reaction_times)
print("Length:", len(trials))


plt.plot(trials, reaction_times, marker='o')

plt.xlabel("Trial Number")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Times Over Trials")

plt.savefig("reaction_graph.png")
