#Author Jin He
def UpComingBD():
    import datetime
    
    today=datetime.datetime.now()
    one_day = datetime.timedelta(days=1)
    one_month_earlier = today + one_day
    while one_month_earlier.month == today.month or one_month_earlier.day < today.day:
        one_month_earlier += one_day
    lastmonth=one_month_earlier
    format = "%b"
    lastmonth = lastmonth.strftime(format).upper()
    #print 'strftimelastmonth:', lastmonth
   
    lastday=one_month_earlier.day
    
   # print'lastday:', lastday
    format = "%b"
    thismonth = today.strftime(format).upper()
    
   # print 'strftimethismonth:', thismonth
    todayday=today.day
   # print 'todayday:', todayday
    
    next3=[]       
    
    
    
    f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r") 
    myList = []
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
       # print(save)
        
        if save[0] in ['1'] and save[1] in ['NAME']:
            StringName=i[6:]
            NewName=StringName.replace("/", " ")
            print ' '
            print 'Name is : ' +NewName
            
            
        if save[1] in ['BIRT\r\n'] :
            
            next=myList[index + 1]
            listday=next[7:9]
            
                
            after = next.split(" ")
            for elements in after:
                if elements == lastmonth and int(listday)<=int(todayday) :
                    print "birthday is " + lastmonth + "/" +listday
                    print" birthdays will coming soon"
                elif elements ==thismonth and int(listday)>=int(todayday):
                    print "birthday is " + thismonth + "/" +listday
                    print" birthdays will coming soon"    
                
UpComingBD()
