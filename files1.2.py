import os
import os.path
data = []
len_dict = {}
files = ['1.txt', '2.txt']
for file in files:
    print(file)
    with open(file) as file1:
        data = len(file1.readlines())
        name1 = os.path.basename(file1.name)
        len_dict[name1]=data
        
max_val = (max(len_dict, key=len_dict.get))
min_val = (min(len_dict, key=len_dict.get))

with open(max_val) as file2:
    data1 = file2.read()
    with open('3.txt', 'a') as file3:
        file3.write(f'{max_val}\n{len_dict[max_val]}\n{data1}\n')

with open(min_val) as file2:
    data1 = file2.read()
    with open('3.txt', 'a') as file3:
        file3.write(f'{max_val}\n{len_dict[min_val]}\n{data1} ')
