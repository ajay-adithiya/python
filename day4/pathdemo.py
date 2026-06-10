from pathlib import Path

path = Path("product.txt") # just returns product.txt (relative path)
print(path)

path = Path("bill.txt").resolve() # returns full path (absolute path)

path = Path("bill.txt") # check file exists
is_there = path.exists()
print(is_there)

path = Path("products.txt") # check file or folder
print(path.is_file()) 
print(path.is_dir())

folder = Path("Bills")     # create folder
folder.mkdir(exist_ok=True)

file = Path("product.txt")  # create file
file.touch()

file = Path("products.txt")  # write text
file.write_text(input("enter details :"))

content_f1 = file.read_text() # reads content in file
print(content_f1)

file = Path("products.txt")
print(file.name)  # file name (products.txt)
print(file.stem)  # wihtout extension (products)
print(file.suffix) # file extension (.txt)

folder = Path(".")            
for item in folder.iterdir():   # print all files in a folder
    print(item)                    

for file in Path(".").glob("*.py"):
    print(file)    # find all python files