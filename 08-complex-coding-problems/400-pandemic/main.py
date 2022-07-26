def infect_neighbors(home_no):
    # will infact the neareast neighbors and return
    # the infected neighbors
    neighbors = [None, None]
    # if target neighbors are not infected then infact
    if (homes[home_no-1] == 0): # 0 means neighbors is not infected
        neighbors[0] = home_no-1
        homes[home_no-1] = 1
    if (homes[home_no+1] == 0):
        neighbors[1] = home_no+1
        homes[home_no+1] = 1
    return neighbors


def get_infection_daywise(infected_homes, infected_day_by_day=[]):
    neighs = []
    for home_no in infected_homes:
        for n in infect_neighbors(home_no):
            if n is not None:
                neighs.append(n)
    if len(neighs) != 0:
        print(f"Homes(next wave) : {homes}")
        infected_day_by_day.append(neighs)
        get_infection_daywise(neighs)
    return infected_day_by_day


total_homes = 10
infected_homes = [3, 5]  # homes numbers start from 1 to N
print(f"     Total Homes : {total_homes}")
print(f"        infected : {infected_homes}")

# We add two additional (None)homes; one at the begining and
# one at the end so that we do not face array out of bound exception
# we initialise each home with 0 it means, at starting every home
# is not infected
homes = [0]*(total_homes+2)  # 0 means house in not infected
homes[0] = None
homes[-1] = None

# assign the infected house with 1
for infected_home in infected_homes:
    homes[infected_home] = 1
print(f"  Homes(initial) : {homes}")
# calculate infection prgression day by day
infected_daywise = get_infection_daywise(infected_homes)
print(f"Infected daywise : {infected_daywise}")
