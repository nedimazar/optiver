import numpy as np
import random
from tqdm import tqdm
import matplotlib.pyplot as plt


# Randomly moves the ant in one of the four directions
def move_ant(position):
    direction = random.choice(["north", "south", "east", "west"])
    if direction == "north":
        return (position[0], position[1] + 10)
    elif direction == "south":
        return (position[0], position[1] - 10)
    elif direction == "east":
        return (position[0] + 10, position[1])
    else:
        return (position[0] - 10, position[1])


def is_food(position):
    return position[1] == 10 - position[0]


def simulate_ant():
    position = (0, 0)
    steps = 0
    while not is_food(position):
        position = move_ant(position)
        steps += 1
    return steps


num_simulations = 10000
total_steps = 0
average_times = []
for i in tqdm(range(num_simulations)):
    total_steps += simulate_ant()
    if (i + 1) % 100 == 0:
        average_steps = total_steps / (i + 1)
        average_time = average_steps
        average_times.append(average_time)

plt.plot(range(100, num_simulations + 1, 100), average_times, color="blue", linewidth=2)
plt.xlabel("Number of simulations", fontsize=14)
plt.ylabel("Average time to reach food (seconds)", fontsize=14)
plt.title("Monte Carlo Simulation of the Ant Problem (Q1)", fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True)
plt.show()
