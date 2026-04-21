# FILE NAME
filename = "sample.txt"

# 1. Create file and write data
with open(filename, "w") as f:
    f.write("Hello world\n")
    f.write("Python programming is fun\n")
    f.write("This is a test file\n")

print("File created and data written.\n")

# 2. Read and display contents
with open(filename, "r") as f:
    print("File Content:")
    print(f.read())

# 3. Read file line by line
print("\nReading line by line:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# 4. Append data
with open(filename, "a") as f:
    f.write("Appending new line\n")

print("\nData appended.")

# 5. Read first n lines
n = 2
print(f"\nFirst {n} lines:")
with open(filename, "r") as f:
    for i in range(n):
        print(f.readline().strip())

# 6. Read last n lines
print(f"\nLast {n} lines:")
with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line.strip())

# 7. Copy file
with open(filename, "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())
print("\nFile copied to copy.txt")

# 8. Merge two files
with open("file1.txt", "w") as f:
    f.write("File1 content\n")

with open("file2.txt", "w") as f:
    f.write("File2 content\n")

with open("merged.txt", "w") as f3:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
        f3.write(f1.read())
        f3.write(f2.read())

print("Files merged into merged.txt")

# 9. Word frequency
with open(filename, "r") as f:
    words = f.read().split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

print("\nWord Frequency:")
print(freq)

# 10. Longest word
longest = max(words, key=len)
print("\nLongest word:", longest)

# 11. Count uppercase, lowercase, digits, special chars
uc = lc = dc = sc = 0
with open(filename, "r") as f:
    for ch in f.read():
        if ch.isupper():
            uc += 1
        elif ch.islower():
            lc += 1
        elif ch.isdigit():
            dc += 1
        elif not ch.isspace():
            sc += 1

print("\nUppercase:", uc)
print("Lowercase:", lc)
print("Digits:", dc)
print("Special Characters:", sc)

# 12. Replace word
with open(filename, "r") as f:
    data = f.read()

data = data.replace("Hello", "Hi")

with open("updated.txt", "w") as f:
    f.write(data)

print("\nWord replaced and saved in updated.txt")

# 13. Reverse content
with open(filename, "r") as f:
    content = f.read()

with open("reverse.txt", "w") as f:
    f.write(content[::-1])

print("Reversed content saved in reverse.txt")

# 14. Check file exists
try:
    f = open(filename, "r")
    print("\nFile exists.")
    f.close()
except:
    print("\nFile does not exist.")

# 15. File size (in bytes)
with open(filename, "rb") as f:
    size = len(f.read())

print("\nFile size:", size, "bytes")

# 16. Count characters, words, lines
with open(filename, "r") as f:
    content = f.read()
    lines = content.split("\n")

print("\nCharacters:", len(content))
print("Words:", len(content.split()))
print("Lines:", len(lines))
