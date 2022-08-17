#Make a CLI program that asks the user for an input then prints it out.
print("Enter quit to exit")

Prompt = input("\nEnter receipt number to be converted as a GCID:\n")
while Prompt != "quit":
    store = Prompt[0:4]
    #if the first number of store is a 0, then remove the first number
    if store[0] == "0":
        store = store[1:]
    till = Prompt[4:7]
    #if the first number of till is a 0, then remove the first number
    if till[0] == "0":
        till = till[1:]

    invoice = Prompt[7:11]
    date_ = Prompt[11:21]
    #remove the / from the date_ and place the last two numbers at the beginning of the string
    date_ = date_.replace("/", "")
    date_ = date_[-2:] + date_[:-2]

    print("==========================\n")
    print("Converted", store, date_, till, invoice,"\n")
    print("==========================\n")
    Prompt = input("Enter receipt number to be converted as a GCID:\n")

#0081042634007/05/19
#07/05/19