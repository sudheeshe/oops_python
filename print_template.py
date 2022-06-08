# Creating a function to print in a template

def template(func):

    def format():
        print("\n#####################################################################################")
        print("\t\t\t\t\tUSING DECORATORS FOR PRINTING THE INFO\t\t")
        print("#######################################################################################")

        print("\n")
        print("Demo of Abstraction : ")
        print(f'\t\tPrinting the "PUBLIC_VARIABLE" of Parent_1  using Child              : {func().name}')
        print(f'\t\tPrinting the "PRIVATE_VARIABLE" of Parent_1  using Child             : {func()._age}')
        print(f'\t\tPrinting the "PROTECTED_VARIABLE" of Parent_1  using Child           : {func()._Parent_1__gender}')
        print("#####################################################################################\n")
        print("Demo of Multiple Inhertence  : ")
        print("\t\tThe 'Child' is Inheriting both 'Parent_1' and 'Parent_2' classes")
        func().parent_1_method()
        func().parent_2_method()

    return format()