import csv
#تظبيت التاريخ في فايل ال appointment 

def edit():
    name = []
    date = []
    print ('111111111111111111111111111111')
    with open('/home/ahmed/Desktop/Clinic_project/clinic/csv_files/last_update/appointment-2022-10-20.csv', 'r+', encoding='utf-16-le') as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        dateAfterEdit= []
        rows = []
        for row in reader: 
            # print (row)
            # name =row[0]
            # print (name)
            date  = row[1]
            # print (date)
            # satt = row[2]
            date = str(date)
            d= date[0:2]
            m = date[3:5]
            y= date[6:10]
            date = y + '-'+ m  +  '-'  + d
            row[1]= date 
            # print (d)
            row[4]= "1000-01-01"
            rows.append(row)
            # print (date)
            print (row)
        writer.writerow(['111111111111111111111111111111111111','111111111111111111111111111111111111','111111111111111111111111111111111111','111111111111111111111111111111111111'])

        for i in rows:
            # writer.writerow([i[0],i[1],"["+ "'"+i[2] + "'"+"]","["+ "'"+i[3] + "'"+"]"])
            writer.writerow([i[0],i[1],i[2],i[3],i[4]])
            # print (i[1])
    return name , date

# def edit2(name, date):
#     with open('app.csv', 'w', encoding='utf-16') as file:
x,y = edit()
print("done")
# edit2(x, y)

