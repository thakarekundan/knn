import csv
dict={'Algeria':1,'Angola':2,'Central African Republic':3,'Ivory Coast':4,'Egypt':5,'Kenya':6,'Mauritius':7,'Morocco':8,'Nigeria':9,'South Africa':10,'Tunisia':11,'Zambia':12,'Zimbabwe':13,'no_crisis':1,'crisis':0}
datalst=[]
with open('african_crises.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        print(row)      
        row[0] = dict[row[0]]
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = float(row[5])
        row[6] = float(row[6])
        row[7] = float(row[7])
        row[8] = float(row[8])
        row[9] = dict[row[9]]
        datalst.append(row)

print("Total dataset -: ",len(datalst))

hit=0
fail=0
trainlst=datalst[0:801]
test=datalst[801:1059]
for each in test:
    classlevel=0
    mindist=28589245823
    for train in trainlst:
        distx=abs(train[0]-each[0]) + abs(train[1]-each[1]) + abs(train[2]-each[2]) + abs(train[3]-each[3]) + abs(train[4]-each[4]) + abs(train[5]-each[5]) + abs(train[6]-each[6]) + abs(train[7]-each[7]) + abs(train[8]-each[8])
        if(mindist>=distx):
            mindist=distx
            classlevel=train[9]
    if classlevel == each[9]:
        hit += 1
    else:
        fail += 1

print("|| Total data -: ", len(datalst),"               ||")
print("|| Train data -: ", len(trainlst),"                ||")
print("|| Test data -: ", len(test),"                 ||")
print("|| Hit data -: ", hit ,"                  ||")
print("|| Failed data -: ", fail ,"                ||")
score=hit/len(test)*100
print("|| Manual Accuracy score -: "+"{:.2f}".format(score),"%   ||")



