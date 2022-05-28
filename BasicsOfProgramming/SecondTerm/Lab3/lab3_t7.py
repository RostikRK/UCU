import random


class Item:
    def __init__(self, name: str, price: float):
        assert  price >= 0, f"Price {price} is not grater than zero"

        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} costs {self.price}."

class Location:
    def __init__(self, city: str, postoffice: int):
        assert  postoffice > 0, f"Postoffice nomer cannot be zero and lower."

        self.city = city
        self.postoffice = postoffice

class Vehicle:
    def __init__(self, vehicleNo: int, isAvailable = True):

        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

class Order:
    def __init__(self, user_name: str, city, postoffice, items: list, vehicle: None = None, orderId = -1):
        if orderId == -1:
            ranin = random.randint(100000000, 999999999)
            self.orderId = ranin
        else:
            self.orderId = orderId
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items
        self.vehicle = vehicle
    def __str__(self):
        return f"Your order number is {self.orderId}."
    def calculate_Amount(self):
        tot_am = 0
        for item in self.items:
            tot_am += item.price
        return tot_am
    def assignVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        return None

# order_lst = []

class LogisticSystem:
    def __init__(self, vehicles: list, orders: list = []):
        self.orders = orders
        self.vehicles = vehicles
    def placeOrder(self, order: Order):
        indu = 0
        for ven in self.vehicles:
            if ven.isAvailable == True:
                self.orders.append((order.orderId, order))
                indu += 1
                ven.isAvailable = False
                break
        if indu == 0:
            return "There is no available vehicle to deliver an order."
    def trackOrder(self, orderId: int):
        res = "No such order."
        for orderr in self.orders:
            if orderr[0] == orderId:
                res = f"Your order #{orderr[1].orderId} is sent to {orderr[1].city}.  Total price: {orderr[1].calculate_Amount()} UAN."
        return res


# if __name__ == "__main__":
#     vehicles = [Vehicle(1), Vehicle(2)]
#     logSystem = LogisticSystem(vehicles)
#     my_items = [Item('book', 110), Item('chupachups', 44)]
#     my_order = Order(user_name='Oleg', city='Lviv', postoffice=53, items=my_items)
#     print(my_order)
#     logSystem.placeOrder(my_order)
#     print(logSystem.trackOrder(my_order.orderId))
#     my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
#     my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
#     print(my_order2)
#     logSystem.placeOrder(my_order2)
#     print(logSystem.trackOrder(my_order2.orderId))
#     my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
#     my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
#     print(my_order3)
#     print(logSystem.placeOrder(my_order3))
#     print(logSystem.trackOrder(my_order3.orderId))

