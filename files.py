#create a file and write data into it.
f=open("file.txt", "w")
f.writelines(["Hey! hi How are YOU?","\nIam fine thank you"])
f.close()

#read and display the contents of a file.
f=open("file.txt", "r")
print(f.read())
f.close()

#read file line by line.
with open("file.txt","r") as f:
        while True:
            line=f.readline()
            print(line)
            if line == '':
                break
f.close()

#append data to an existing file
f=open("file.txt", "a")
f.write("\n")
f.write("its not working")
f.close()

#read first n lines of a file.
f=open("file.txt", "r")
c=1
n=int(input("enter how many line do you want to read:"))
while c<=n:
    line=f.readline()
    c=c+1
    print(line)
f.close()

#read last n lines of a file
f=open("file.txt", "r")
c=0
n=int(input("enter how many line do you want to read:"))
lines=f.readlines()
while c<n and c<len(lines):
    print(lines[c-n].strip())
  
#copy lines of a file.
f=open("file.txt", "r")
f1=open("file1.txt","w")
for x in f:
    f1.write(x.strip())
    f1.write("\n")
f.close()
f1.close()

#merge two files into a third file
f=open("file.txt","r")
f1=open("file1.txt","r")
f2=open("file2.txt","w")
for x in f:
    f2.write(x.strip())
    f2.write("\n")
for y in f1:
    f2.write(y.strip())
    f2.write("\n")
f.close()
f1.close()
f2.close()

#count frequency of words in a file
f=open("file.txt","r")
s=f.read()
w=s.split()
freq={}
for x in w:
    if x in freq:
        freq[x] = freq[x]+1
    else:
        freq[x] = 1
print(freq)

#longest word in afile
f1=open("file1.txt","r")
s=f1.read()
w=s.split()
lw=""
for x in w:
    if len(x)>len(lw):
        lw=x
print(f"longest word:{lw}")

#replace a word
f=open("file.txt","r")
s=f.read()
f=open("file.txt","w")
a=input("enter the word you wan to replace:")
b=input("enter the new word:")
new=s.replace(a,b)
for x in f:
        f.write(new)
        f.write("\n")
print(f.write())
f.close()

#to count uc,lc and digits
f=open("file.txt","r")
s=f.read()
l,u,c=0
for ch in s:
    if ch.upper():
        u=u+1
    if ch.islower():
        l=l+1
    if ch.isdigit():
        c=c+1
print(f"uppercase:{u},lowercase:{l},digit:{c}")
f.close()

#to count words lines and characters
f=open("file.txt","r")
s=f.read()
l,c,w=0
for ch in s:
    if ch.isalpha():
        c=c+1
    if ch==" ":
        w=w+1
    if ch=="\n"
        l=l+1
print(f"words:{w},lines:{l},characters:{c}")
