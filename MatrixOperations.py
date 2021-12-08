#Printing Finallist function
def printing(f):
    for x in f:
        print(x)
        
#Variables & List
main = "j"
finsum=0
#Inputing of Size of Matrix
row1=int(input("Enter number of rows on matrix: "))
column1=int(input("Enter number of columns on matrix: "))
row2=int(input("Enter number of rows on matrix: "))
column2=int(input("Enter number of columns on matrix: "))
#Inputing of Matrix & 0's of Final List
list1=[]
list2=[]
for x in range(row1):
        list1.append([])
        for y in range(column1):
            list1[x].append(int(input("Input Numbers of Matrix 1: ")))
for x in range(row2):
        list2.append([])
        for y in range(column2):
            list2[x].append(int(input("Input Numbers of Matrix 2: ")))

while main=="J" or main=="j":
    finallist=[]
    finallist1=[]

#Finallist
    for x in range(row1):
                finallist.append([])
                for y in range(column2):
                    finallist[x].append(0)
#Finallist1
    for x in range(row1):
                finallist1.append([])
                for y in range(column1):
                    finallist1[x].append(0) 

#Add & Sub
    choice=input("Select your operation:\n[A]Addition\n[B]Subtraction\n[C]Multiplication\n[D]Inverse\n[E]Transpose\n[F]Joint of Zero\n[G]Meet of Zero\n[H]Boolean Multiplication\nInput : ")
    if choice=="A" or choice=="a":
        if row1==row2 and column1==column2:
            for x in range(row1):
                for y in range(column1):
                    finallist[x][y]+=list1[x][y]+list2[x][y]
            printing(finallist)
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")
                   
    elif choice=="B" or choice=="b":
        if row1==row2 and column1==column2:
           for x in range(row1):
                for y in range(column1):
                    finallist[x][y]+=list1[x][y]-list2[x][y]
           printing(finallist)
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")

#Multiplication
    elif choice=="C" or choice=="c":
        if column1==row2:
            for x in range(len(list1)):
                for y in range(len(list2[0])):
                    for z in range(len(list2)):
                        finallist[x][y]+=list1[x][z]*list2[z][y]
            printing(finallist)
   
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")


#Inverse
    elif choice=="D" or choice=="d":
        if row1==2 and column1==2:
            sol=1/(list1[0][0]*list1[1][1]-list1[0][1]*list1[1][0])
            finallist1[0][0]+=list1[1][1]
            finallist1[1][1]+=list1[0][0]
            finallist1[0][1]+=-1*list1[0][1]
            finallist1[1][0]+=-1*list1[1][0]
            for x in range(row1):
                for y in range(column1):
                    finallist[x][y]+=round(sol*finallist1[x][y],1)
            printing(finallist)
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")

#Transpose
    elif choice=="E" or choice=="e":
        if row1==column1:
            for x in range(row1):
                for y in range(column1):
                    finallist[x][y]+=list1[y][x]
            printing(finallist)
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")

#Join
    elif choice=="F" or choice=="f":
        if row1==row2 and column2==column1:
            for x in range(row1):
                    for y in range(column1):
                        if list1[x][y]==1 or list2[x][y]==1:
                            finallist[x][y]+=1
                        else:
                            finallist[x][y]+=0
            printing(finallist)
                 
        else:
                print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")
#Meet
    elif choice=="G" or choice=="g":
        if row1==row2 and column1==column2:
            for x in range(row1):
                    for y in range(column1):
                        if list1[x][y]==1 and list2[x][y]==1:
                             finallist[x][y]+=1
                        else:
                            finallist[x][y]+=0
            printing(finallist)
                       
        else:
             print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")
     
#Boolean
    elif choice=="H" or choice=="h":
        if column1==row2:
            for x in range(len(list1)):
                    for y in range(len(list2[0])):
                        for z in range(len(list2)):
                            finallist[x][y]+=list1[x][z]*list2[z][y]
            for x in range(row1):
                for y in range(column2):
                    if finallist[x][y]>=1:
                            finallist[x][y]=1
            printing(finallist)
            
        else:
            print("INCOMPATIBLE MATRIX SIZE!\nPlease Select Again.")

#Printing of Matrix and Final Output
    main=input("Enter J to continue or Enter Anything else to stop:  ")
    

