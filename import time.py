#TIME_COUNTER
''' LETS USE A TIME COUNTER '''

import time

count_time=int(input("ENTER TIME IN SECONDS: "))
NAME=input("ENTER YOUR NAME: ")
for x in range(count_time,0,-1):
  seconds=x%60
  minutes=int(x/60)%60
  hours=int(x/3600)
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)

print(f"TIME'S UP,'{NAME}'")