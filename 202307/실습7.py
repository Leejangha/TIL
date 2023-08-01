# 과제 7-2

# 아래 클래스를 수정하시오.
class StringRepeater():
    def repeat_string(self, repeat, string):
        for _ in range(repeat):
            print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")


# 과제 7-4

# 아래 클래스를 수정하시오.
class Person():
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.number_of_people += 1
    
    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
       

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)