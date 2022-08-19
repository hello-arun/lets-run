def calc_min_move(A:str) -> int:
    seat_nos=[i for i,j in enumerate(A) if j=="x"]
    median_i = len(seat_nos)//2
    start_pos = seat_nos[median_i]-median_i
    moves=0
    for i,seat in enumerate(seat_nos):
        moves += abs(seat-i-start_pos)
    return moves


if __name__ == "__main__":
    A="xx..xx....xxx"
    print(calc_min_move(A))