thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" 
print(thislist)


thislist.append("org")
thislist.append("banana")
print(thislist)

thislist.remove("org")
print(thislist)

thislist.insert(0, "orange")
print(thislist)

for items in thislist:
  print(items)

for i in range(len(thislist)-1):
    print(thislist[i])

    