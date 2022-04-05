def list_of_name(name_to_age, given_age):
    # names = []
    # for key in name_to_age.keys():
    #     if name_to_age[key] <= given_age:
    #         names.append(key)

    # return names

    return [key for key in name_to_age.keys() if name_to_age[key] <= given_age]

def main():
    name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
    print(list_of_name(name_to_age, 30))


if __name__ == '__main__':
    main()
