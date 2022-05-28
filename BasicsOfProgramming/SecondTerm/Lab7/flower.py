class Flower:
    """Flower Class"""
    def __init__(self, petals=0, price=0, color='') -> None:
        """Initializating the class
        >>> fl = Flower(10, 20, "red")
        >>> print(fl.color)
        "red"
        """
        self.petals = petals
        self.price = price
        self.color = color


class Tulip(Flower):
    """Tulip Class"""
    def __init__(self, petals, price) -> None:
        """Initializating the class
        >>> tul = Tulip(10, 30)
        >>> print(tul.price)
        30
        """
        super().__init__(petals, price)
        self.color = "pink"


class Rose(Flower):
    """"Rose class"""
    def __init__(self, petals, price) -> None:
        """
        Initializating the class
        >>> roz = Rose(10, 30)
        >>> print(roz.petals)
        10
        """
        super().__init__(petals, price)
        self.color = "red"


class Chamomile(Flower):
    """Chamomile class"""
    def __init__(self, petals, price) -> None:
        """Initializating the class
        >>> cham = Chamomile(10, 30)
        >>> print(cham.price)
        30
        """
        super().__init__(petals, price)
        self.color = "white"


class FlowerSet:
    """Flowerset Class"""
    def __init__(self) -> None:
        """Initializating the class
        >>> set1 = FlowerSet()
        >>> print(len(set1.flower_set)
        0
        """
        self.flower_set = list()

    def add_flower(self, flower: object):
        """
        Adding one Flower to set
        >>> set1 = FlowerSet()
        >>> roz = Rose(10, 30)
        >>> set1.add_flower(roz)
        >>> print(len(set1.flower_set))
        1
        """
        self.flower_set.append(flower)


class Bucket:
    """Bucket Class"""
    def __init__(self) -> None:
        """Initializating the class
        >>> bucket1 = Bucket()
        >>> print(bucket1.bucket)
        []
        """
        self.bucket = list()

    def add_set(self, flower_set: FlowerSet):
        """
        Adding one set to the bucket
        >>> bucket1 = Bucket()
        >>> set1 = FlowerSet()
        >>> roz = Rose(10, 30)
        >>> set1.add_flower(roz)
        >>> bucket1.add_set(set1)
        >>> print(len(bucket1.bucket))
        1
        """
        self.bucket.append(flower_set)

    def total_price(self):
        """
        Calculates the total price of bucket
        >>> bucket1 = Bucket()
        >>> set1 = FlowerSet()
        >>> roz = Rose(10, 30)
        >>> set1.add_flower(roz)
        >>> bucket1.add_set(set1)
        >>> print(bucket1.total_price())
        30
        """
        total_price = 0
        for flowers_set in self.bucket:
            for flower in flowers_set.flower_set:
                total_price += flower.price
        return total_price
