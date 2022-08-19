def calc_max_time(mice:list,holes:list):
    mice.sort()
    holes.sort()
    max_time=0
    for a,b in zip(mice,holes):
        max_time = max(max_time,abs(a-b))
    return max_time


if __name__=="__main__":
    mice = [3,2,-4]
    holes = [0,-2,4]
    print(calc_max_time(mice,holes))
