#!/bin/python3
if __name__ == '__main__':

    arr = []
    maximum = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(6):
        for j in range(6):
            if i < 4 and j < 4:    
                out = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                if j == 0:
                    maximum=out
                if out > maximum:
                    maximum=out
    print(maximum)
        