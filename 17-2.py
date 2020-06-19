import csv
list1=[1,3.5,7,9]
list2=[2,4,6,8,10]
list3=[2,4,8,16,32]
with open('libiao.csv','a') as f:
    writer=csv.writer(f)
    writer.writerow(list1)
    writer.writerow(list2)
    writer.writerow(list3)
myfile=open(r'libiao.csv','r')
myfilecontent=myfile.read()
myfile.close()
for i in myfilecontent:
    print(i,end='')
print('*'*30)
with open('libiao.csv','r') as file:
    content=csv.reader(file)
    for i in content:
        print(i,end='')