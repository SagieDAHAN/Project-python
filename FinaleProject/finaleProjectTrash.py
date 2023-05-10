def readAccounts():
    accounts_file = open("accounts.csv", "r")
    accounts_list = []
    for line in accounts_file:
        if line == 'Number,Balance,customerName\n':
            continue
        att_list = line[:-1].split(",")
        if len(att_list) > 3:
            att_list = [att_list[0],att_list[1],att_list[2] + att_list[3]]
        accountsTuple = tuple(att_list)
        if accountsTuple == ('', '', ''):
            break

        accounts_list.append(accountsTuple)
    print(accounts_list)
    accounts_file.close()
    return accounts_list

readAccounts()
