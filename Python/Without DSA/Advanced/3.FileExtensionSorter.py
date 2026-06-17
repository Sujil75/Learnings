files = input("Enter the files with extensions use comma to separate the files: ").split(",")

files = list(map(lambda each: each.strip(), files))

new_files = {}
exts = []
for file in files:
    ext = file.split('.')[1]

    exts.append(ext)

exts = list(set(exts))

for ext in exts:
    ext_files = []

    for file in files:
        if ext in file:
            ext_files.append(file)

    new_files[ext] = ext_files

print(new_files)

# check: hello.txt, files.txt, log.py