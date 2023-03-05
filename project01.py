#Project thuc hanh Python basic voi Excel

'''De bai: xu ly diem thi: Tinh ra diem trung binh, tong diem va ket qua
cua bai thi dua vao file excel cho truoc'''

#Read file goc va tao new file
orinal_file = open('directory.csv', mode = 'r', encoding= 'utf-8-sig')
new_file = open('new_name_directory.csv', mode = 'w', encoding= 'utf-8-sig')

#Read first row (head)
header = orinal_file.readline()

#add header cho new file
new_file.write(header.strip() + ',Diem Trung Binh' + ',Tong Diem' + ',Ket Qua'+ '\n')

#tinh toan 
row = orinal_file.readline().strip()
while row != '': #vong lap ket thuc khi row = null
    list_row = row.split(',')
    # tach theo index trong list roi tinh toan
    mon1 = float(list_row[3])
    mon2 = float(list_row[4])
    mon3 = float(list_row[5])
    mon4 = float(list_row[6])
    tb_diem = round((mon1 + mon2 + mon3 + mon4)/4, 2)
    sum_diem = round(mon1 + mon2 + mon3 + mon4, 2)
    #dieu kien cho column ket qua
    if sum_diem >= 30:
        ketqua = 'Lop chon'
    elif sum_diem >= 25:
        ketqua = 'Lop thuong'
    else:
        ketqua = 'Truot'
    #write row by row
    new_file.write(row.strip() + ',' + str(tb_diem) + ',' + str(sum_diem) + ',' + ketqua +'\n')
    row = orinal_file.readline().strip()
print ('Du lieu da duoc xu ly xong!')