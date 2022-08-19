def find_earliest_gas_station(gas,cost):
    n = len(gas)
    curr = start = 0
    for i,(g,c) in enumerate(zip(gas*2,cost*2)):
        if i == start+n:
            return start
        curr += g-c
        # print(g,c,curr,start)
        if curr<0:
            start=i+1
            curr=0
    return -1

if __name__ == "__main__":
    gas_stations = [3,5,2,1,7]
    costs        = [4,2,1,9,1]
    print(find_earliest_gas_station(gas_stations,costs))