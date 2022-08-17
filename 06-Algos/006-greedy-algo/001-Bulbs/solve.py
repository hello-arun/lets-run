def calc_cost(A:list) -> int:
    """ 
    A : Binary List for bulb states
    """
    cost = 0 
    for b in A:
        if cost%2 != 0:
            b = not b 
        if b == 0:
            cost+=1
    return cost

if __name__ == "__main__":
    bulbs=[1,0,1,0,1]
    print("Cost:",calc_cost(bulbs))   