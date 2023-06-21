#The solution for the problem 9.4:
name = input("Enter file:")
dicty = dict()
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if not line.startswith("From "):continue
    line = line.rstrip()
    words = line.split()
    email = words[1]
    dicty[email] = dicty.get(email, 0) + 1

bigcount = None
bigemail = None
for email,count in dicty.items():
    if bigcount == None or count > bigcount:
        bigmail = email
        bigcount = count
print(bigemail,bigcount)
