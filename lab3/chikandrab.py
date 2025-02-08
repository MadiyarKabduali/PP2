def animals(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens*2+rabbits*4) == numlegs:
            return chickens, rabbits
print(animals(35,94))