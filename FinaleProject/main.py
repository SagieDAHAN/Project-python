from datetime import datetime


def readAccounts():
    accounts_file = open("accounts.csv", "r")
    accounts_list = []
    for line in accounts_file:
        att_list = line[:-1].split(",")
        if len(att_list) > 3:
            att_list = [att_list[0], att_list[1], att_list[2] + att_list[3]]
        accountsTuple = tuple(att_list)
        if accountsTuple == ('', '', ''):
            break

        accounts_list.append(accountsTuple)
    accounts_file.close()
    return accounts_list


def readTransactions():
    transactions_file = open("transaction.csv", "r")
    transactions_list = []
    for line in transactions_file:
        attr_list = line[:-1].split(",")
        tuple_list = tuple(attr_list)
        transactions_list.append(tuple_list)
    transactions_file.close()
    return transactions_list


account_list = readAccounts()
list_of_transactions = readTransactions()


def init():
    a,b = readAccounts(),readTransactions()
    return a,b


def saveAccounts(acc_list):
    file = open("accounts.csv", "w")
    for account_tuple in acc_list:
        line = ','.join(account_tuple)
        line += "\n"
        file.write(line)


def saveTransactions(Trans_list):
    file = open("transaction.csv", "w")
    for Transaction_tuple in Trans_list:
        line = ','.join(Transaction_tuple)
        line += "\n"
        file.write(line)
    file.close()


def save():
    saveAccounts(acc_list=account_list)
    saveTransactions(Trans_list=list_of_transactions)


def menu():
    user_options = input(f"Welcome !,Menu:\n('1').Create new Account\n('2').Deposit money into the account\n('3').Withdraw money from the account\n('4').Check balance\n('5').Account movements report\n('6').Exit\nchoose what kind of action you would like to do from above:")
    if user_options == '1' or user_options == '2' or user_options == '3' or user_options == '4' or user_options == '5' or user_options == '6':
        return user_options
    else :
        print("Wrong input , please insert one of the numbers below !")


def add_account():
    new_account_num = input("Please insert your new account number :")
    full_name = input("Please insert full name :")
    for accountTuple in account_list:
        account_num, balance, customerName = accountTuple
        if new_account_num == account_num:
            print("This account already exists ! you need to type a new account that doesnt exist")
            break

    else:
        balance = str(0)
        new_tuple = (str(new_account_num), balance, full_name)
        account_list.append(new_tuple)


def deposit():
    account_num = input("Please insert your account number:")
    deposit_amount = float(input("Please insert the amount you would like to deposit:"))
    flag = False
    for accountTuple in account_list:
        account, balance, customerName = accountTuple

        if account_num == account:
            this_time = datetime.now().strftime("%d/%m/%Y %H:%M")
            new_transactionTuple = (str(account), str(this_time), str(deposit_amount))
            balance = float(balance) + float(deposit_amount)
            account_list.remove(accountTuple)
            NewTuple = (str(account), str(balance), customerName)
            list_of_transactions.append(new_transactionTuple)

            account_list.append(NewTuple)
            flag = True
            break

    if deposit_amount < 0:
        print("You cant insert a negative number for a withdraw action ! ")
    if deposit_amount == 0:
        print('You cant insert 0 has this action does not exist ,please insert a higher number !')
    if flag == False:
        print('This account does not exist,if you dont have an account please create one or try again !')


def withdraw():
    account_num = input("Please insert your account number:")
    withdraw_amount = float(input("Please insert the amount you would like to withdraw:"))
    flag = False
    for accountTuple in account_list:
        account, balance, customerName = accountTuple

        if account_num == account:
            this_time = datetime.now().strftime("%d/%m/%Y %H:%M")
            new_transactionTuple = str(account_num), str(this_time), "-"+str(withdraw_amount)

            new_balance = float(balance) - withdraw_amount
            if new_balance < 0:
                print("Sorry not enough money to withdraw at your account balance!")
                flag = True
                break
            account_list.remove(accountTuple)

            newTuple = (account, str(new_balance), customerName)
            list_of_transactions.append(new_transactionTuple)
            account_list.append(newTuple)
            flag = True
            break

    if withdraw_amount < 0:
        print("You cant insert a negative number for a withdraw action ! ")
    if withdraw_amount == 0:
        print('You cant insert 0 has this action does not exist ,please insert a higher number !')
    if flag == False:
        print('This account does not exist,if you dont have an account please create one or try again !')


def Balance():
    account_num = input("Please insert your account number:")
    flag = False
    for accountTuple in account_list:
        account, balance, customerName = accountTuple

        if account_num == account:
            print(f'You\'e total Balance is :\n{balance}')
            flag = True
    if flag == False:
        print('This account does not exist,if you dont have an account please create one or try again !')


def report():
    account_num = input("Please insert your account number:")
    flag = False
    count = 0
    for transactionTuple in list_of_transactions:
        Transaction_num, date, Transaction = transactionTuple
        if Transaction_num == account_num:
            if count > 0:
                print(f'{date} {Transaction.rjust(28)}')
            else:
                count += 1
                print(f'For the following account Number -{account_num}:')
                print(f'{"Date and Hour of the Transaction:"} {"Account transactions:".rjust(25)}')
                print(f'{date} {Transaction.rjust(28)}')
                flag = True

    if flag == False:
        print('This account does not exist,if you dont have an account please create one or try again !')


def main():
    on = True
    init()
    while on:
        user_choice = menu()
        if user_choice == '1':
            add_account()
        if user_choice == '2':
            deposit()
        if user_choice == '3':
            withdraw()
        if user_choice == '4':
            Balance()
        if user_choice == '5':
            report()
        if user_choice == '6':
            save()
            print('Thank you for using us ! see you next time !')
            on = False
        else:
            on = True


main()






