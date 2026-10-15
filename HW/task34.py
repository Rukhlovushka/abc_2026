# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
#book = Product("Book", 10)
#pen = Product("Pen", 2)
#order = Order()
#order.add_product(book)
#order.add_product(pen)
#print(f"Общая стоимость: {order.total_price}")  # 12

class Product:
    """Товар с защитой от отрицательной цены."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value if value >= 0 else 0


class Order:
    """Заказ со списком товаров и вычисляемой общей стоимостью."""

    def __init__(self):
        self._products = []

    @property
    def total_price(self):
        return sum(product.price for product in self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)


book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}") # Общая стоимость: 12