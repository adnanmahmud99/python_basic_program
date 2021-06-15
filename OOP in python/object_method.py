class Person:
  def __init__(self, name, age, adress):
    self.name = name
    self.age = age
    self.adress=adress
  def func(self):
    print("Hello my name is " + self.name)
    print("Hello my Age is " + self.age)
    print("Hello my Adress is " + self.adress)
p1 = Person("Adnan", "36" ,"Dhaka")
p1.func()
