#python program create csv file student.csv(sid,sname,city,contact)
import csv
field=['Sid','Sname','City','Contact']
rows=[[1,'OM','Surat',1234553256],
      [2,'Sai','bardoli',456775324],
      [3,'ram','buhari',7865497535],
      [4,'Kishna','Bardoli',5667887456],
      [5,'radha','surat',6485287542]]
filename="c:\\sqlite3\\csv\\student.csv"
#insert record through user input
l=[]
for i in range(5):
    no=int(input("Enter id:"))
    name=input("Enter name:")
    city=input("Enter city:")
    contact=int(input("Enter contact number:"))
    t=(no,name,city,contact)
    l.append(t)
with open(filename,'w',newline='')as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(field)
    csvwriter.writerows(rows)
    csvwriter.writerows(l)
# Reading dat from csv file.
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for record in csvreader:
        print(record)
print("Total no.of rows:%d"%(csvreader.line_num))
