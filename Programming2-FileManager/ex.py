# example.py
import os
from file_manager.manager import FileManager, MultiFileManager

# --- create sample files if they don't exist ---
for name, content in [("a.txt", "Hello\n"), ("b.txt", "World\n"), ("c.txt", "!!!\n")]:
    if not os.path.isfile(name):
        with open(name, 'w') as f:
            f.write(content)

# --- now you can safely use FileManager ---
fm1 = FileManager("a.txt")
print(f"The file name : {fm1.path} has been created ! and its : {fm1.file_size(fm1.path)} KB")
fm2 = FileManager("b.txt")
print(f"The file name : {fm2.path} has been created ! and its : {fm2.file_size(fm2.path)} KB")
fm3 = fm1 + fm2
print(f"The file name : {fm3.path} has been created ! and its : {fm3.file_size(fm3.path)} KB")
print(open(fm3.path).read())

mfm = MultiFileManager("a.txt")
print(f"The file name : {mfm.path} has been created ! and its : {mfm.file_size(mfm.path)} KB")
out = mfm.concat_many("b.txt", "c.txt")
print(f"The file name : {out.path} has been created ! and its : {out.file_size(mfm.path)} KB")
print(mfm)
print(open(out.path).read())