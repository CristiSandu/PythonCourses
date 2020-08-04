fname = input("Enter file name: ")
fh = open(fname)
nr = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    nr = nr + 1
    index = line.find(':')
    index = index + 2
    count = count + float(line[index:]) 
   # fw.writelines(line[index:] + "\n")
   
   # fw.close()
print("Average spam confidence:", count/nr)
##fw = open("smt.txt")
