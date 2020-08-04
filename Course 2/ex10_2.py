#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = {}
for index in handle :
    if index.startswith("From ") :
        lst = index.split()
        hower = lst[5]
        lsth = hower.split(':')
        howr = lsth[0]
        #print()
        count[howr] = count.get(howr,0) + 1

lst2 = list()
for k,v in count.items() :
    lst2.append((k,v))
lst2.sort()

for k, v in lst2 :
    print(k,v)
