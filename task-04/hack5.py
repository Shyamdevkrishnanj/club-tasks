
s = input()
def timeconversion(s):

    l = list(s.strip(':'))

    hour = l[0] + l[1]
    minutes = l[3]+ l[4]
    seconds = l[6] + l[7]
    zone = l[8] + l[9] 
    if zone == 'PM' and hour != '12':
        time = int(hour) + 12
      
        
        print(f"{time}:{minutes}:{seconds}")
    elif zone == 'PM' and hour == '12':
        print(f"{hour}:{minutes}:{seconds}")
    
    elif zone == 'AM' and hour == '12':
        print(f"00:{minutes}:{seconds}")
    elif zone == 'AM':
        print(f"{hour}:{minutes}:{seconds}")

timeconversion(s)