def max_3prod(A:list) -> int:
    """ 
    A : list of integers
    """
    A = sorted(A)

    hi3 = A[-1]*A[-2]*A[-3]
    lo2hi1 = A[0]*A[1]*A[-1]
    return max(hi3,lo2hi1)

if __name__ == "__main__":
    integers=[-5,1,0,6,-5,6]
    print("Max 3 Product:",max_3prod(integers))   