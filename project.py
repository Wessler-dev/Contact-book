def add_contact(contacts, name_contact, e_mail, phone):
    contact = {"contact": name_contact, "email":e_mail, "phone_number":phone, "added":False}
    contacts.append(contact)
    print(f"contact {name_contact}, {e_mail}, {phone} has been successfully added!")
    return

def update_contact(contacts, index_contacts, updated_contact_name, updated_contact_email, updated_contact_phone):
    updated_index = int(index_contacts) -1
    if updated_index >=0 and updated_index <len(contacts):
        contacts[updated_index]["contact"] = updated_contact_name
        contacts[updated_index]["email"] = updated_contact_email
        contacts[updated_index]["phone_number"] = updated_contact_phone
        print(f"Contado atualizado para:{index_contacts}, {updated_contact_name}, {updated_contact_email}, {updated_contact_phone}")
    else:
        print("deu merda")

def add_favorites(contacts,index_contacts,):
    index_favorite = int(index_contacts) -1
    contacts[index_favorite]["added"] = True
    print(f"contact {index_contacts} has been successfully added!")
    return

def remove_favorites(contacts,index_contacts,):
    index_favorite = int(index_contacts) -1
    contacts[index_favorite]["added"] = False
    print(f"contact {index_contacts} has been successfully removed!")
    return


def view_contacts(contacts):
    for index, options in enumerate(contacts, start= 1):
        status = "★" if options["added"] else " "
        option_choose = options["contact"]
        email = options["email"]
        phone = options["phone_number"]
        print(f"{index}. [{status}] {option_choose} {email} {phone} ")
        return
    

def view_favorites(contacts):
     for index, options in enumerate(contacts, start= 1):
        status = "★" if options["added"] else " "
        option_choose = options["contact"]
        email = options["email"]
        phone = options["phone_number"]
        if status == True:
            print(f"{index}. [{status}] {option_choose} {email} {phone} ")
        return

def remove_contact(contacts,index_contact):
    contacts.pop(int(index_contact)-1)
    print("Contact removed successfully!")
    return
     

options = []
while True:
    print("\nContact list manager: ")
    print("1.Add new contact with e-mail and phone number")
    print("2.Add the contact to your favorites.")
    print("3.Remove the contact to your favorites.")
    print("4.view contact list")
    print("5.View list of favorite contacts")
    print("6.Delete contact")
    print("7. Exit")
    print("8.Uptade contact")

    action = input("Choose an option: ")
    if action == "1":
        name_contact = input("Enter the name of the contact you wish to add: ")
        email_contact = input("Enter the E-mail of the contact you wish to add: ")
        phone_contact = input("Enter the phone number of the contact you wish to add: ")
        add_contact(options,name_contact,email_contact, phone_contact)

    elif action =="2":
        view_contacts(options)
        index_contacts = input("Enter the contact number you wish to add to your favorites; ")
        add_favorites(options,index_contacts)
    
    elif action =="3":
        view_favorites(options)
        index_contacts = input("Enter the contact number you wish to remove to your favorites: ")
        remove_favorites(options,index_contacts)
    

    elif action == "4":
        view_contacts(options)
    
    elif action == "5":
        view_favorites(options)
    
    elif action == "6":
       view_contacts(options)
       index_contacts = input("Enter the contact number you wish to remove: ")
       remove_contact(options,index_contacts)

    elif action == "7":
        break

    elif action =="8":
        view_contacts(options)
        index_contacts = input("Digite o número da contato que deseja atualizar:")
        novo_nome = input ("digite o novo nome")
        novo_email = input ("digite o novo email")
        novo_phone = input ("digite o novo phone")
        update_contact(options, index_contacts, novo_nome, novo_email, novo_phone)