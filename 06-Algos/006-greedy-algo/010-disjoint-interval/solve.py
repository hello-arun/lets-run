def count_maxdisjoints(A:list) -> int:
    """ 
    A : list of list of integers
    """
    A.sort(key=lambda x:x[1]) # Prioritzing sets which ends up early

    prev_s,prev_e = A[0]
    count = 1
    for s, e in A:
        if s>prev_e:
            prev_s,prev_e=s,e
            count+=1
    return count

if __name__ == "__main__":
    integers=[[1,4],[2,3],[4,6],[8,9]]
    print("Max Disjoints:",count_maxdisjoints(integers))   