class Person:
    def __init__ (self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone_num)


class Customer(Person):
    def __init__(self, name, address, phone_num, cust_num, on_mailing_list):
        Person.__init__(self, name, address, phone_num)

        self.__cust_num = cust_num
        self.__on_list = on_mailing_list

    def print_person(self):
        super().print_person()

        print(self.__cust_num)
        print(self.__on_list)