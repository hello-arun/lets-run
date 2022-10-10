from turtle import clear


def get_total_paths(n: int, m: int, path):
    if n == 1:
        answer = 1
        path += "R"*(m-1)
        paths.append(path)
    elif m == 1:
        answer = 1
        path += "D"*(n-1)
        paths.append(path)
    else:
        answer = get_total_paths(n, m-1, path+"R") +\
            get_total_paths(n-1, m, path+"D")
    return answer


N=6
M=3
print(f"Calculating for {N}x{M} matrix")
paths = []
print("Total Paths:",get_total_paths(N,M, ""))
print("Trejectories:")
for path in paths:
    print(" ",path)
