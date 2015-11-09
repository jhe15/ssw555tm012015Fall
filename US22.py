#Author Jin He
def UniqueID():
 
    f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r") 
    myList = []
    myList1 = []
    Duplicated=[]
    from collections import Counter
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
        #print(save)
        if save[0] in ['0']:
            if(save[1].find("@")==0):
                myList1.append(save[1])
              #  print(myList1)
    
    
    Duplicated=[k for k,v in Counter(myList1).items() if v>1]
   # print(Duplicated)  
    for j in (Duplicated):
        print "The ID " + j + " is not unique"
           
              
            
UniqueID()
