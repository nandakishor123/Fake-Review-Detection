import csv
token = []
i=0
with open('reviews.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
	i= i+1
	if i==5:
		exit(10)
        token += list(row)
	print row
	#print row
	#print "Ho!!"
    
f.close()
