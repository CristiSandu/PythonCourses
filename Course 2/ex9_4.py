 #Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hist = {}
for index in handle :
    if index.startswith("From ") :
        lst = index.split();
        hist[lst[1]] = hist.get(lst[1],0) + 1
bigercount = None
bigword = None

for k,v in hist.items() :
    if bigercount is None or bigercount < v :
        bigword = k 
        bigercount = v

print(bigword,bigercount)        
