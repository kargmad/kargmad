def main():
 N=int(input("Enter the number of Ingredients"))

 quantity_req=[]

 quantity_total=[]

 quan_used_total=[]

 quantity_req=list(map(int, input("Enter the quantity values: ").split())) 
 quantity_total=list(map(int, input("Enter the total values: ").split()))
 for i in range(N):

    quan_used_total.append(int(quantity_total[i]/quantity_req[i]))
 print("Total number of PowerPuff girls which can be created:", min(quan_used_total))
main()