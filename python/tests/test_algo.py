from random import randint
from copy import copy
from unittest import TestCase

from python.algos import (
    Bubble,
    Counting,
    Insertion, 
    Selection,
    Tree,
    Algo,
    AlgoFabric
)


MINI = -100
MAXI = 100
SIZE = 50


class AlgoFabricTest(TestCase):
    def test_fabric_choices(self):
        choices = AlgoFabric.get_choices()
        self.assertIsInstance(choices, list)
        for choice in choices:
            with self.subTest(choice):
                self.assertIsInstance(choice, str)

    def test_fabric_installed_algos(self):
        for algo in AlgoFabric.installed_algos:
            self.assertIsInstance(algo, type)

    def test_fabric_algo(self):
        for algo in AlgoFabric.get_choices():
            instance_algo = AlgoFabric.get_algo(algo)
            self.assertIsInstance(instance_algo, Algo)


class SortAlgoTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list = [randint(MINI, MAXI) for _ in range(SIZE)]

    def _test_sort(self, result):
        for k, v in enumerate(result):
            with self.subTest(f"list[{k}] = {v}"):
                if k > 0:
                    self.assertTrue(
                        result[k-1] <= v,
                        msg=f"list[{k}] = {v} is not greater than list[{k-1}] = {result[k-1]}"
                    )

    def test_bubble(self):
        algo = Bubble()
        result = algo.process(copy(self.list))
        self.assertEqual(len(self.list), len(result))
        self._test_sort(result)

    def test_counting(self):
        algo = Counting()
        result = algo.process(copy(self.list))
        self.assertEqual(len(self.list), len(result))
        self._test_sort(result)

    def test_insertion(self):
        algo = Insertion()
        result = algo.process(copy(self.list))
        self.assertEqual(len(self.list), len(result))
        self._test_sort(result)

    def test_selection(self):
        algo = Selection()
        result = algo.process(copy(self.list))
        self.assertEqual(len(copy(self.list)), len(result))
        self._test_sort(result)

    def test_tree(self):
        algo = Tree()
        print(self.list)
        result = algo.process(copy(self.list))
        print(result)
        self.assertEqual(len(copy(self.list)), len(result))
        self._test_sort(result)
