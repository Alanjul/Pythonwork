accounts = open('accounts.txt', 'r')
temp_file = open('temp.txt', 'w')
with accounts,temp_file:
    for line in accounts:
        account, name, balance = line.split()
        if name != "Doe":
            temp_file.write(line)
        else:
            new_name = ' '.join([account, "Smith",balance] )
            temp_file.write(new_name + '\n')