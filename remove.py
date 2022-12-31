import csv

with open("test.csv", "rb") as infile, open("repaired_file.csv", "wb") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    conversion = set('_"/.$')
    # text =  input.read()
    # newtext = '_'
    for row in reader:
        newrow = [''.join('_' if c in conversion else c for c in entry) for entry in row]
        writer.writerow(newrow)

infile.close()
outfile.close()