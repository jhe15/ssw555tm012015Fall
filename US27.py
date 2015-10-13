#Author: Jin He
def CurrentAge():
    import datetime
    today=datetime.datetime.now()
    year=today.year

    f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r") 
    myList = []
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
        
        if save[0] in ['1'] and save[1] in ['NAME']:
            StringName=i[6:]
            NewName=StringName.replace("/", " ")
            print 'Name is : ' +NewName
        
        if save[1] in ['BIRT\r\n'] :
            next=myList[index + 1]
            listyear=next[13:]
            convert= int( listyear)
            convertcurrentyear=int(year)
            Result=convertcurrentyear-convert
        
            print 'Age is :' 
            print(Result)
            print '  '
        
CurrentAge()        
        
    
         
