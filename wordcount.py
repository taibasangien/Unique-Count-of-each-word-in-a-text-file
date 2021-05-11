a = open('choc.txt', 'r')
w = input('Enter the word to be searched')

s = a.read()
list=s.split()
print(list)
count=0
for i in list:
   if(i==w):
       count+=1
print("WORD {} OCCURED {} TIMES".format(w,count))