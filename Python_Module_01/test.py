class Boy:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__working_for = "FBI"
class Student(Boy):
    def get_age(self):
        print("Age:",self.age)
        
s1 = Student("yassine",21)



print(s1._age)
print(s1.name)
print(s1._Boy__working_for)