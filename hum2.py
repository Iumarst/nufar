class Human:
    def __init__ (self,n,a,b):
        print('Создан объукт клвсса Human')
        self.__name = n
        self.__age = a
        self.__height = b
        
    def print(self):
        print(f'имя:{self.__name}')
        print(f'возраст:{self.__age}')
        print(f'рост:{self.__height}')

    @property
    def name(self):
        return self.__name.upper()
       
    @name.setter       
    def name(self,n):
        self.__name=n.capitalize()
        
    @property
    def age(self):
        return self.__age
       
    @age.setter       
    def age(self,a):
        if (a>0 and a <100): 
            self.__age=a
        else :
            print(fallse)            
           
    @property
    def height(self):
        return self.__height
       
    @height.setter       
    def height(self,b):
        if (b>0 and b <200): 
            self.__height=b
        else :
            print(fallse)
   
    
        
person1 = Human('фунтик',23,17)
person1.print()
person1.name = 'skuf'
print(person1.name)
person1.age = 25
print(person1.age)
person1.height = 175
print(person1.height)