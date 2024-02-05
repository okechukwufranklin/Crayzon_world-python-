PhoneBook = []

def PhoneBook_Display():
    PhoneBook_Menu = """ PhoneBook Menu
1.Save Number
2.Edit Number
3.Delete Number
4.Search Number
5.View Contacts
6.Exit"""


def Save_Number():
    contact_info = {}
    number = int(input("How Many Numbers would u like to save:"))
    for i in range (number):
     ContactName = input("Enter Name:")
    ContactNumber = int(input("Enter Phone Number:"))
    contact_info[ContactName] = ContactNumber
    PhoneBook.append(contact_info)
    print("Saved contact:")
    print(len(contact_info))
    print(contact_info)

def Delete_Number(name):
    input("Enter Name To Delete:")


    
