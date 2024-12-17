import  os
with open("grades.txt", mode="r") as grades:
    print(f"{"ID": <5} {"Name":<10} {"Grade":<10}")
    for grade in grades:
        id, name, grade = grade.split()
        print(f"{id:<5} {name:<10} {grade:<10}")
#updating text files in python
accounts = open("accounts.txt", mode="r")
tempfile = open("tempfile.txt", mode="w")
with accounts, tempfile:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            tempfile.write(record)
        else:
            new_record = ' '.join((account, 'Williams ', balance))
            tempfile.write(new_record + '\n')
grade1 = open("grades.txt", mode="r")
temp_grade = open("temp_grade.txt", mode="w")
with grade1, temp_grade:
    for record in grades:
        id, name, grade = record.split()
os.remove('acounts.txt')
os.rename('tempfile.txt', 'accounts.txt')