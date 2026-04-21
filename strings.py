s=input("enter a string:")
print("length:",len(s))
print("uppercase:",s.upper())
print("lowercase:",s.lower());
print("titlecase:",s.title())
vowels="aeiouAEIOU"
v=c=0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)
ch=input("enter a character:");
print("Frequecy:",s.count(ch))
b=s.replace(" ","")
print(b)
old=input("Old substring: ")
new=input("New substring: ")
print("Replaced:", s.replace(old, new))
print("reversed string:",s[::-1])
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")
print("duplicates:","".join(set(s)))
pwd = input("Enter password: ")
if (len(pwd) >= 8 and
    any(c.isupper() for c in pwd) and
    any(c.islower() for c in pwd) and
    any(c.isdigit() for c in pwd) and
    any(not c.isalnum() for c in pwd)):
    print("Strong Password")
else:
    print("Weak Password")
