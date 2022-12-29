import csv
import os
from collections import Counter

def edit():
    name = []
    list_of_names = []
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../csv_files/last_update/patients.csv')
    errors_filename = os.path.join(dirname, '../csv_files/last_update/appointment-2022-10-20_errors.csv')
    with open(filename, 'r', encoding='utf-16') as file, open(errors_filename, 'w', encoding='utf-16') as errors_file:
        reader = csv.reader(file)
        writer = csv.writer(errors_file)
        for row in reader:
            name =row[0]    
            list_of_names.append(name)
            # cprint (list_of_names)
            
        c = Counter(list_of_names)

        for word, count in c.items():
            if count >= 2:
                print(word)



            # if count == 1:
            #     print(word)
            # else:
            #     print(f'{word} appeared: {count}')
            # try:
            #     # print ("000000000000000000000000000000000000000")
            #     # print ("000000000000000000000000000000000000000")
            #     # print (mypat)
            #     myappo = Appointment.objects.create(
            #         patient = mypat,
            #         appointmentDate = row[1],
            #         appointmentType = row[2],
            #         appointmentStatus = row[3],
            #         )                 
            #     # myappo.patient.add(mypat)
            #     # print (myappo)
            #     x=x+1
            #     print (x)
            # except Exception as e:
            #     print("111111111111111111111111111111111111111111111111111111111111")
            #     row.insert(0, e)
            #     writer.writerow(row)
    return 0




y = edit()
