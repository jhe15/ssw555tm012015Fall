#Author Jin He
def AgeLessThan150():
    import datetime
    today=datetime.datetime.now()
    year=today.year
    next3=[]
    f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r") 
    myList = []
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
        
        if save[0] in ['1'] and save[1] in ['NAME']:
            StringName=i[6:]
            NewName=StringName.replace("/", " ")
            print ' '
            print 'Name is : ' +NewName
        
        if save[1] in ['BIRT\r\n'] :
            next=myList[index + 1]
            listyear=next[13:]
            convert= int( listyear)
            convertcurrentyear=int(year)
            Result=convertcurrentyear-convert
            next3=myList[index + 3]
        
            if  Result <150:
                print 'Birth after 1865, age less than 150'
        
            elif Result >150 and next3.startswith('2 DATE'):
                print'Birth before 1867'
                listDeath=next3[13:]
                Actualage=int(listDeath)-convert
                print ' Actual age is: ' 
                print (Actualage)
                if Actualage< 150:
                    print 'age is less than 150'
                else:
                    print'age is more than 150, it is invalid'
                
           
            else :
                print'Information is not clear'
            
AgeLessThan150()
