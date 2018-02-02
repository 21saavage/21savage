import random
count=0
while (count<=100):
    roll=input('enter r to roll a dice')
    if(roll=='r'):
        r=random.randint(1,6)
        count=count+r
        print("random number",r)
        print(' in position',count)
        if  count==8:
            count=37
            print(' take the ladder my friend',count)
        elif count==11:
            count=2
            print(' die and come down',count)
        elif count==13:
            count=34
            print('take the ladder my friend',count)
        elif count==25:
            count=4
            print('die and come down',count)
        elif count==38:
            count=9
            print('die and come down',count)
        elif count==40:
            count=68
            print('take the ladder my friend',count)
        elif count==52:
            count=81
            print('take the ladder my friend',count)
        elif count==65:
            count=46
            print('die and come down',count)
        elif count==76:
            count=97
            print('take the ladder my friend',count)
        elif count==89:
            count=70
            print('die and come down',count)
        elif count==93:
            count=64
            print('die and come down',count)
        elif count>100:
            print("try again")
            count=count-r
        elif count==100:
            print("won")
            break
            
    
           
            
        
