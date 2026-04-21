l=[1,2,2,4,5]
print("maximum:",max(l),"minimum:",min(l))
import statistics
print("mean:",statistics.mean(l))
print("median:",statistics.median(l))
print("mode:",statistics.mode(l))
print("ascending:",sorted(l))
print("descending:",sorted(l,reverse=True))
a=int(input("enter any number:"))
print("count of a:",l.count(a))
print("duplicates:",list(set(l)))
c=[1,4,3]
d=[6,2,5]
print("merged list:",c+d)
l=list(set(l))
l.sort()
print("second largest:",l[-2])
#string to list
s=input("enter a string:")
print("string to list:",list(s))
print("common elements:",list(set(c) & set(d)))
print("difference:",list(set(c)-set(d)))
