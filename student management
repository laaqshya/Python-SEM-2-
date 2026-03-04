#1.print details of a student
details={"name":"sruthi", "Roll No.":"25071A0501", "Dept.":"CSE"}
print(details)
for x in details:
    print(details[x])
#2. update the age
details.update({"age":"18yrs"})
print(details)
#3.update the value of an existing key
details.update({"name":"Sameera"})
print(details)
#4.delete a key
details.pop("age")
print(details)
#5.check whether a key exists
s=(input("enter key to search:"))
for x in details.keys():
    if(s==x):
        print("found")
#6.length of dictionary
print("length of dictionary:",len(details))
#7.print all keys indictionary
print("keys:",details.keys())
#8.print all values
print("values:",details.values())
#9.print key values
for x in details.items():
    print(x)
#10.count frequency of character in a string
s=(input("enter a string:"))
fre={}
for x in s:
      fre.update({x:s.count(x)})
print(fre)
#11.count frequency of words in a sentence
s=input("enter a sentence:")
freqw={}
b=s.split()
for i in b:
     freqw.update({i:b.count(i)})
print(freqw)
#print square 1 to n
n=int(input("enter n:"))
squares={}
for i in range(1,n+1):
    squares.update({i:i**2})
print(squares)
#merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
merged_dict = d1 | d2
print(merged_dict)
#sort dictionary by keys
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict_asc = dict(sorted(my_dict.items()))
print(f"Original dictionary: {my_dict}")
print(f"Sorted by keys (ascending): {sorted_dict_asc}")
#keep two lists in dictionary
l1=["name", "class", "sec"]
l2=["honey", "6", "A"]
stud={}
for key,value in zip(l1,l2):
    stud[key]=value
print(stud)
