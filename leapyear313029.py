while True:
 month=0 # to access globally
 yearint=0 # to access globally

 leapyear=False
 while True:
  year=str(input('enter year: '))
  if not len(year)==4: 
    print('Invalid Year length 4 digits yyyy only!')
    yearint=int(year) # casted from string to an integer
       
  else:
    # if yearint % 4==0 and yearint % 100!=0 and yearint % 400==0:
    
    if yearint%4==0:
        leapyear=True
        print('Leap Year: ',year)
    else:
        print('This is Not a Leap Year!')
    break

 while True: #error found not fixed by invalid month
  month=int(input('enter month: '))
  if month<1 or month >12:
    print('Invalid Month, Re-enter the month!')
  else:
   if month in (1,3,5,7,8,10,12):
    month31={1:'January',3:'March',5:'May',7:'July',
             8:'August',10:'October',12:'December'}
    print(month31[month])
    print('Days=31')
 
   elif month ==2:
     
     if leapyear:
      month29={2:'February\nDays=29'}
      print(month29[month])
     else:
      month28={2:'February\nDays=28'}   
      print(month28[month]) 
 
   elif month in(4,6,9,11):    
     month30={4:'April',6:'June',9:'September',11:'November'}
     print(month30[month])
     print('Days=30')
   break

    