import datetime

timenow = datetime.datetime.now()

delta = datetime.timedelta(seconds=10)

timestop = timenow + delta

print(timenow)
print(timestop)

while datetime.datetime.now() < timestop:
    print('this')
    