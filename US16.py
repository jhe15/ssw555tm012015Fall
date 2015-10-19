#Author Jin He

import datetime
f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r")
def MaleWithSameLast():
    
    today=datetime.datetime.now()
    year=today.year
    next3=[]
    
    myList = []
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
        
        if save[0] in ['1'] and save[1] in ['NAME']:
            StringName=i[6:]
            NewName=StringName.replace("/", " ")
          #  print ' '
            print 'Name is : ' +NewName
        
        
        if save[0] in ['1'] and save[1] in ['NAME']: 
            next=myList[index + 4]
            listyear =next[6]
            print  ' The gender:'+listyear
            if listyear =='F' :
                 print ' This person is a female.'
            elif listyear =='M'and  save[3] in ['/Bell/\r\n']  : 
                 print ' This person is a male with the same last name with family.'
            else:
                 print ' This person is a male with the different last name with family.'
            

MaleWithSameLast()
