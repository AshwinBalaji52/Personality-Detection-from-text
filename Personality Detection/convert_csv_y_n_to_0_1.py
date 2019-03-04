import csv
r = csv.reader(open('essays1.csv')) # Here your csv file
lines = list(r)
for line in lines:
    print(line)
    if line[7]=='y':
        line[7]=1
    else:
        line[7]=0
    if line[8]=='y':
        line[8]=1
    else:
        line[8]=0
    if line[9]=='y':
        line[9]=1
    else:
        line[9]=0
    if line[10]=='y':
        line[10]=1
    else:
        line[10]=0
    if line[11]=='y':
        line[11]=1
    else:
        line[11]=0
    print(line)

writer = csv.writer(open('essays2.csv', 'w'))
writer.writerows(lines)
