import os 
print(os.path.dirname(os.path.abspath(__file__)))


for dir, subdir, files in os.walk(path):
    for file in files:
        print path.join(dir, file)