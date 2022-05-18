#Multiples of tree
input_string = input('Enter number list elements seperated by commas ') 
number_list = input_string.split(',')
for i in range(len(number_list)):
    number_list[i] = int(number_list[i])

list_for_3 = list()
list_for_5 = list()
list_for_3_and_5 = list()
for i in number_list:
     if i%3==0 and i%5==0:
         list_for_3_and_5.append(i)
     if i%3==0:
         list_for_3.append(i)
     if i%5==0:
        list_for_5.append(i)
print(len(list_for_3), len(list_for_5), len(list_for_3_and_5), sep='\n')

#second version
input_string = input('Enter number list elements seperated by commas ') 
number_list = input_string.split(',')
number_list = [int(i) for i in number_list]

list_for_3 = 0
list_for_5 = 0
list_for_3_and_5 = 0

for i in number_list:
     if i%3==0 and i%5==0:
        list_for_3_and_5 += 1
     if i%3==0:
        list_for_3 += 1
     if i%5==0:
        list_for_5 += 1

print(list_for_3, list_for_5, list_for_3_and_5, sep='\n')