import os, csv

f=open("/home/ahmed/Desktop/Clinic_project/clinic/csv_files/last_update/fielssame.csv",'r+')
w=csv.writer(f)
for path, dirs, files in os.walk("/home/ahmed/Desktop/Scrap_clinic/tutorial/tutorial/spiders/downloads"):
    for filename in files:

        pathlist = path.split("/")
        patienid= pathlist[-1]

        w.writerow([patienid,patienid+'/'+filename])
print('Done')