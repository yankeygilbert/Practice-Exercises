class clockType:
    def settime(hour,min,sec):
        thour=hour
        tmin=min
        tsec=sec
    def timer(hour, mins,sec):
        for hour in range(hour,0,-1):
            for mins in range(mins,0,-1):
                for sec in range(0,60):
                    print (hour,":",mins,":",sec)
   


#main code 
clockType.timer(0,2,0)

