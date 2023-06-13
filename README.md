# Python-for-Everybody

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    if line.startswith("From"):
        raw = line.split(":")
        hey = raw[0]
        ray = hey[-2:]
        if ray == int:
            continue
        d[ray] = d.get(ray,0) + 1

lst = list()
for key,val in d.items():
    way = (key,val)
    lst.append(way)

lst = sorted(lst)

for key,val in lst[:-1]:
    print(key,val)
