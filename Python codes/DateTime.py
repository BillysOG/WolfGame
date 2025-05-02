import datetime as d

date = d.date(2008,3,1)
time =d.time(3,30,15)

current_time = d.datetime.now()
current_time2 = current_time.strftime("%H:%M:%S\n%d/%m/%Y")
target_time = d.datetime(2030, 4 , 5)

print(f"\n{current_time2}")

if current_time > target_time:
    print("The current time is greater than the target time\n")
else:
    print("The current time is NOT greater than the target time\n")