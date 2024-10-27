class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание объектов класса Store
store1 = Store("Овощи, фрукты", "Улица Некрасова, 8")
store2 = Store("Продукты круглосуточно", "Улица Чапаева, 45")
store3 = Store("Витаминка", "Переулок Солнечный, 89")
store4 = Store("Гипермаркет", "Улица Щорса ")

# Добавление товаров в магазины
store1.add_item('яблоки', 5.5)
store1.add_item('груша', 9.95)

store2.add_item('молоко', 5.55)
store2.add_item('творог', 12.15)

store3.add_item('колбаса', 23.0)
store3.add_item('сыр', 24.89)

store4.add_item('хлеб', 3.40)
store4.add_item('яйца', 19.65)


# Тестирование методов на одном из магазинов
print(f"Начальный ассортимент в {store1.name}: {store1.items}")

store1.add_item('апельсины', 11.15)
print(f"Добавлены апельсины. Ассортимент в {store1.name}: {store1.items}")

store1.update_price('яблоки', 6.05)
print(f"Обновлена цена яблок. Ассортимент в {store1.name}: {store1.items}")

store1.remove_item('груша')
print(f"Удалены грушы. Ассортимент в {store1.name}: {store1.items}")

price_of_apples = store1.get_price('яблоки')
print(f"Цена яблок в {store1.name}: {price_of_apples}")

price_of_bananas = store1.get_price('груша')
print(f"Цена груш в {store1.name}: {price_of_bananas}")