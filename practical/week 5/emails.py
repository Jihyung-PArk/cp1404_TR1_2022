

def main():
    emails_to_names = {}
    email = input("Email: ")
    while email != " ":
        name = get_name(email)
        # print(name)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ").title()
        emails_to_names[email] = name
        # print(emails_to_names[email])
        email = input("Email: ")

    for email, name in emails_to_names.items():
        print("{0} ({1})".format(name, email))


def get_name(email):
    id = email.split("@")[0]
    # print(id)
    sep_name = id.split(".")
    # print(sep_name)
    name = "  ".join(sep_name).title()
    return name


main()
