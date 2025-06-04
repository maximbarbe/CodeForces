s = input().split(":")
t = input().split(":")
time_hours = int(s[0])
time_minute = int(s[1])
sleep_hours = int(t[0])
sleep_minute = int(t[1])
if sleep_minute > time_minute:
    time_hours -= 1
    time_minute += 60
if time_hours < sleep_hours:
    time_hours += 24

print(f'{str(time_hours - sleep_hours).rjust(2, "0")}:{str(time_minute - sleep_minute).rjust(2, "0")}')
    
