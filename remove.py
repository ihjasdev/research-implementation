import csv
fname =("test.csv")
with open( fname , "rU") as infile, open("repaired_file.csv", "wb") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = '"/(){}_[]'
    for row in reader:
        newrow = [''.join('' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)

File_name = 'repaired_file.csv'
df=File_name
print(df)