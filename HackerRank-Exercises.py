# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n=int(input())
    d={}
    for i in range(n):
        k,v=input().split()
        d[k]=v
    
    for i in range(n):
        try:
            query=input()
        except EOFError:
            break
        try:
            print(f'{query}={d[query]}')
        except KeyError:
            print("Not found")
        