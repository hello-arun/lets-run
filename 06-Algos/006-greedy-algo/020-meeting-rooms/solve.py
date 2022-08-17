def calc_max_room(A):
    data = []
    for s,e in A:
        data.append((s,+1))
        data.append((e,-1))
    data.sort()


    curr = 0
    max_ = 0

    for _,v in data:
        curr+=v
        max_=max(max_,curr)
    return max_

if __name__ == "__main__":
    meetings=[[5,10],[15,20],[1,24]]
    print(calc_max_room(meetings))
