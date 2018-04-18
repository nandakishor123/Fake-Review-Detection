import sys
import glob
import csv

folder = sys.argv[1]
output_file = sys.argv[2]

files = glob.glob('./' + folder + '*.txt')

contents = []

for file in files:
    contents += open(file).readlines()

f = open(output_file,'a')
with f:
    writer = csv.writer(f, delimiter=',')
    for text in contents:
        writer.writerow([text])
