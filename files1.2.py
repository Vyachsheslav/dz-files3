import os
import os.path
import glob


dict_txt = {}
for filename in glob.glob('*.txt'):
   with open(os.path.join(os.getcwd(), filename), 'r') as f:
       text = f.read() 
       f.close()
       with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = len(f.readlines())
            dict_txt[filename] = [data, text]

sorted_dict = dict(sorted(dict_txt.items()))


with open('3.txt', 'a') as f:
    for text in sorted_dict.items():
        f.write(f'{text[0]}\n')
        f.write(f'{text[1][0]}\n')
        f.write(f'{text[1][1]}\n')
