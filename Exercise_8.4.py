#The solution for the problem 8.4:

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in lst: continue
        lst.append(word)
        
sorted_lst = sorted(lst)
print(sorted_lst)
