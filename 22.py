import random

class Pet:
    def __init__(self: str, name, form: str, happy: int = 100, health: int = 50): 
        self.name = name
        self.form = form
        self.happy = happy
        self.health = health

    def play(self, happyplus: int):
        self.happy += happyplus
        print(f'{self.name} повысил счастье до {self.happy}')

    def eat(self, food_options): 
        food_options = { 
            "Рыба": 15,
            "Мясо": 30,
            "Корм": 10,
            "Кость": 25,
        }
        
        if isinstance(food_options, dict):  
            food, hp = random.choice(list(food_options.items()))
            self.health += hp
            print(f'{self.name} потрапезничал {food} и повысил хп до {self.health}')
        elif isinstance(food_options, str):
            print(f'{self.name} потрапезничал {food_options} и повысил хп до {self.health}')
            
        

x = Pet('bobr', 'cat', 50, 50)
x.play(20)
x.eat(1)