#!/usr/bin/env python3
# coding: utf-8

from random import randint
from python import algos


MINI = -100
MAXI = 100
SIZE = 50


class App:
    limit = 3
    stats = True
    algos = ['exit'] + algos.AlgoFabric.get_choices()

    def sorting(self, to_sort: list) -> list:
        algo = self.menu()
        if isinstance(algo, algos.Algo):
            return algo.process(to_sort, self.stats)
        return to_sort

    def menu(self, iter: int = 0):
        if iter >= self.limit:
            print('Exiting...')
            return None

        print("Choose an algo to sort your list (by number or name) :")
        for i, name in enumerate(self.algos):
            print(f" {i}: {name.capitalize()}")

        choice = self.get_input()
        if choice and choice != 'exit':
            return algos.AlgoFabric.get_algo(choice)
        elif choice == 0 or choice == 'exit':
            return self.menu(iter=self.limit)
        return self.menu(iter+1)

    def get_input(self) -> str:
        choice = input('Your choice :')
        result = ""
        try:
            ichoice = int(choice)
            result = self.algos[ichoice]
        except Exception:
            if choice in self.algos:
                result = choice
        if result:
            print(f"Selected: {result}")
        return result


if __name__ == "__main__":
    print("#"*24)
    print("#", " Valbou - Sort Algos", "#")
    print("#", "Version 1.0 (Python)", "#")
    print("#"*24)

    to_sort = [randint(MINI, MAXI) for _ in range(SIZE)]

    print(to_sort)
    ui = App()
    sorted_list = ui.sorting(to_sort)
    print(sorted_list)

    print("#"*24)
