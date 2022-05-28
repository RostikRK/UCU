from typing import Tuple
from unittest import TestCase, main
from flower import *


class TestFlower(TestCase):
    def test_flower_attributes(self):
        fl = Flower(10, 20, "red")
        self.assertEqual(fl.color, "red")
        self.assertEqual(fl.petals, 10)
        self.assertEqual(fl.price, 20)

    def test_tulip_attributes(self):
        tul = Tulip(10, 30)
        self.assertEqual(tul.petals, 10)
        self.assertEqual(tul.price, 30)
        self.assertEqual(tul.color, "pink")

    def test_rose_attributes(self):
        roz = Rose(10, 30)
        self.assertEqual(roz.petals, 10)
        self.assertEqual(roz.price, 30)
        self.assertEqual(roz.color, "red")

    def test_chamomile_attributes(self):
        cham = Chamomile(10, 30)
        self.assertEqual(cham.petals, 10)
        self.assertEqual(cham.price, 30)
        self.assertEqual(cham.color, "white")

    def test_flowerset(self):
        roz = Rose(10, 30)
        set1 = FlowerSet()
        set1.add_flower(roz)
        self.assertEqual(len(set1.flower_set), 1)
        cham = Chamomile(10, 30)
        set1.add_flower(cham)
        set1.add_flower(roz)
        self.assertEqual(len(set1.flower_set), 3)

    def test_bucker(self):
        bucket1 = Bucket()
        self.assertEqual(bucket1.bucket, [])
        roz = Rose(10, 30)
        set1 = FlowerSet()
        set1.add_flower(roz)
        cham = Chamomile(15, 66)
        set1.add_flower(cham)
        set1.add_flower(roz)
        bucket1.add_set(set1)
        set2 = FlowerSet()
        tul = Tulip(7, 120)
        set2.add_flower(tul)
        set2.add_flower(roz)
        bucket1.add_set(set2)
        self.assertEqual(len(bucket1.bucket), 2)
        self.assertEqual(bucket1.total_price(), 276)
        set3 = FlowerSet()
        bucket1.add_set(set3)
        self.assertEqual(bucket1.total_price(), 276)


if __name__ == "__main__":
    main()
