import csv

def edit():
    name = []
    date = []
    with open('/home/ahmed/Desktop/klinik/csv files/all patients test.csv', 'r+',encoding='utf-16-le',newline = "") as file:
        reader = csv.reader(file)
        writer = csv.writer(file)
        dateAfterEdit= []
        rows = []
        for row in reader: 
            name =row[0]
            age = row[1]
            yorm = row [2]
            referrd = row[6]
            causes = row[10]
            diagnosis = row[11]
            treatments = row[12]
            operations = row[13]

            if yorm == 'Years':
                year = 2022 - int(age)
                birthday = str(year) + '-' + '01' + '-' + '01'
                row[1] = birthday
                #print (row[1])
            elif yorm == 'Months':
                month = 12 - int(age)
                if month == 0:
                    month =1
                birthday = '2022' + '-' + str(month) + '-' + '01'
                row[1] = birthday

            ######################
            referrd = "["+ "'"+ referrd + "'"+ "]"
            row[6] = referrd
            #####################
            causessplit = causes.split("/")
            row[10] = causessplit
            ###########################
            diagnosissplit = diagnosis.split("/")
            row[11] = diagnosissplit
            ###########################
            treatmentssplit = treatments.split("/")
            row[12] = treatmentssplit
            ###########################
            operationssplit = operations.split("/")
            row[13] = operationssplit



            rows.append(row)
        #print (rows)
        for i in rows:
            writer.writerow([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13]])
            # print ([i[0], i[1]], i[6])
    return name , date

# def edit2(name, date):
#     with open('app.csv', 'w', encoding='utf-16') as file:
x,y = edit()
print("done")
# edit2(x, y)

