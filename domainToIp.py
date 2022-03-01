import socket
import xlwt 
from xlwt import Workbook

file = open('','r')

domain_list = []
wb = Workbook()

for x in file.readlines():
    domain_list.append(x.rstrip())

sheet1 = wb.add_sheet('Sheet 1')
#sheet1.write(1,0,'abc')

for i in range(len(domain_list)):
    sheet1.write(i,0,domain_list[i])
    sheet1.write(i,1,socket.gethostbyname(domain_list[i]))

#for y in domain_list:
    #print(y + ' -> '+ socket.gethostbyname(y))

wb.save('D2IP_output.xls')
