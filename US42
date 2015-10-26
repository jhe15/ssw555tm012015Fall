#Author: Jin He
f = open("/Users/jinhe/Documents/workspace/P02/src/AlexanderGraham1.ged","r") 
def Rejectillegitimatedates():
    import datetime
    today=datetime.datetime.now()
    year=today.year

    
    myList = []
    for line in f:
        myList.append(line)
     
    for index, i in enumerate(myList):    
        save=i.split(" ")
        if save[0] in ['1'] and save[1] in ['DATE']:  
            if save[3] in ['JAN', 'MAR','MAY', 'JUL','AUG','OCT','DEC']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<32 and int(save[2])>0:
                    
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                 
            elif save[3] in ['APR', 'JUN','SEP', 'NOV']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<31 and int(save[2])>0:
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                    print ' '
                    
            elif save[3] in ['FEB']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<29 and int(save[2])>0:
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                    print ' '
            else:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                print' This is not correct date'
                print ' '
        
        
        if save[0] in ['2'] and save[1] in ['DATE']:  
            if save[3] in ['JAN', 'MAR','MAY', 'JUL','AUG','OCT','DEC']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<32 and int(save[2])>0:
                    
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                 
            elif save[3] in ['APR', 'JUN','SEP', 'NOV']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<31 and int(save[2])>0:
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                    print ' '
                    
            elif save[3] in ['FEB']:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                if  int(save[2])<29 and int(save[2])>0:
                    print 'The date is correct'
                    print ' '
                else:
                    print'The date is not correct'
                    print ' '
            else:
                print (save[2] + ' '+  save[3]+ ' ' + save[4])
                print' This is not correct date'
                print ' '
            
                
     
Rejectillegitimatedates()        
        
    
         
