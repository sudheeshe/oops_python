from print_template import template



class Parent_1:

    def __init__(self, name= "John", age = 44, gender='Male'):
        self.name = name # public variable
        self._age = age # private variable
        self.__gender = gender # protected variable

    def parent_1_method(self):
        print("\t\t'Parent_1' class method is accessing through 'Child' class")



class Parent_2:
    def __init__(self, name= "Alice", age = 39, gender='female'):
        self.name = name # public variable
        self._age = age # private variable
        self.__gender = gender # protected variable

    def parent_2_method(self):
        print("\t\t'Parent_2' class method is accessing through 'Child' class")



class Child(Parent_1, Parent_2):
    def __init__(self):
        super().__init__()





if __name__ == '__main__':
    try:
        @template
        def demo():
            a = Child()
            return a

    except Exception as e:
        raise e


