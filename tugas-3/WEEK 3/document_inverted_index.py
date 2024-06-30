index = {}	

def read_files(filename, file_number):
  f = open(filename)
  l1 = f.readlines()
  counter = 0
  words = []
  for i in l1:
    temp = i.split(' ')
    for j in temp:
      words.append(j.lower().replace("\n", ""))
  for i in words:
    if not i in index.keys():
      index[i] = [(file_number, counter)]
      counter = counter + len(i) + 1
    else:
      index[i].append((file_number, counter))
      counter = counter + len(i) + 1
    
  f.close()
  return None


read_files('./input1.txt', 1)
read_files('./input2.txt', 2)
read_files('./input3.txt', 3)


sorted_keys = sorted(index.keys())

f = open("output.txt", "w")
output_line = "Word".ljust(15) + "Frequency".ljust(15) + "Posting List".ljust(15) + "\n"
f.writelines(output_line)
f.writelines('-------------------------------------------------------------------------\n\n')
for i in sorted_keys:
  print(i, len(index[i]), index[i])
  output_string = str(i).ljust(15) + str(len(index[i])).ljust(15) + str(index[i]).ljust(15) + "\n"
  f.writelines(output_string)
  
f.close()
