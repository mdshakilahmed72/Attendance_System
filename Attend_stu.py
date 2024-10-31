
import datetime
import csv
header = False


def input_data(name,roll,Course):
    global header
    date = datetime.datetime.now()
    date.strftime("%d-%m-%y  %H:%M:%S")
    data = [name,roll,Course,date]
    head = ["Name", "Roll", "Course","Date&Time"]
    on = open(r"D:\Python\Project\Attendance\Att.csv","a",newline='')
    dt = csv.writer(on)
    if not header:
        dt.writerow(head)
        header = True

    dt.writerow(data)
    on.close()

def output_data():
    op = open(r"D:\Python\Project\Attendance\Att.csv","r")
    dt = csv.reader(op)
    for r in dt:
        print(r)
    op.close()



while True:
    char = str(input("If You want to give the Attendance y/n ?"))
    name = str(input("Enter Your Name "))
    roll = int(input("Enter your Roll "))
    course_name = str(input("Enter Your Course Name "))
    
    if(char=="n"):
        output_data()
        break
    input_data(name,roll,course_name)



