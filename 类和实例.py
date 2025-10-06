# 1. 定义一个“类”（蓝图）
class Dog:
    # 初始化方法，在创建实例时被调用，用于设置初始属性
    def __init__(self, name, breed, color):
        # “self” 代表将来要创建的实例本身
        self.name = name    # 实例属性
        self.breed = breed  # 实例属性
        self.color = color  # 实例属性

    # 类的方法（行为）
    def bark(self):
        print(f"{self.name} 在叫：汪汪！它是一只"+self.breed+"。它的颜色是"+self.color+"!")

# 2. 创建“实例”（具体的对象）
# 根据 Dog 类，创建了一个具体的狗实例，名叫“旺财”
my_dog = Dog("旺财", "金毛", color="棕色")
# 创建了另一个狗实例，名叫“来福”
your_dog = Dog("来福", "泰迪", color="灰色")
# 创建岩仔的狗
mars_dog = Dog("七七","泰迪","黑色")

# 3. 使用实例
print(my_dog.name)   # 输出：旺财
print(your_dog.breed) # 输出：泰迪
print(mars_dog.breed)

my_dog.bark()        # 输出：旺财 在叫：汪汪！
your_dog.bark()      # 输出：来福 在叫：汪汪！
mars_dog.bark()

print(mars_dog.color)