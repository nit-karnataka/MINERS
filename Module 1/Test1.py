import csv
with open ('DB1.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=",")
	line = 0
	list1 = list()
	idlst = set()
	for row in csv_reader:
		if line == 0:
			line+=1;
			continue
		idlst.add(row[1])
		list1.append(row)

with open ('DB2.csv') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=",")
	line = 0
	list2 = list()
	for row in csv_reader:
		if line == 0:
			line+=1;
			continue
		idlst.add(row[1])
		list2.append(row)


print(list1)
print(list2)
print(idlst)
db = dict()

for i in idlst:
    
    for l in list1:
        lt = list()
        if i in l:
            lt.append(l[0])
            lt.append(l[2])
            
            db[i] = lt
    for l in list2:
        lt = list()
        if i in l:
            lt.append(l[0])
            lt.append(l[2])
            db[i] = lt
            
for k,v in db.items():
       bg = v[1].split()
       try:           
           if bg[1] == "positive":
               bg[1] = "+"
           elif bg[1] == "negative":
               bg[1] = "-"
       except Exception as ex:
           continue

       v[1] = "".join(bg)
       db[k] = v

print(db)

with open('combined.csv',mode='w') as file:
    writer = csv.writer(file,delimiter=',')
    for k,v in db.items():
        lst = list();
        lst.append(k)
        lst.append(v[0])
        lst.append(v[1])
        
        
        writer.writerow(lst)
print("file written");
