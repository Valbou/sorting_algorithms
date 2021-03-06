#!/usr/bin/env python3
# coding: utf-8

from random import randint
from time import time
from copy import copy
import algos


class Benchmark:
    def go(self) -> None:
        self.start = time()

    def stop(self) -> None:
        self.end = time()

    def __enter__(self) -> None:
        self.go()

    def __exit__(self, *args) -> None:
        self.stop()

    def __str__(self) -> str:
        return f"Ran in {round(self.end - self.start, 4)} seconds"


class ConfigApp:
    _mini = -100
    _maxi = 100
    _size = 50
    _the_list = []

    def get_random_list(self) -> list:
        if len(self._the_list) == 0:
            self._the_list = [randint(self._mini, self._maxi) for _ in range(self._size)]
        return self._the_list

    def manual_config(self) -> None:
        print("#"*4, "Configuration", "#"*4)
        print("Min, max and size must be integers")
        self._mini = self.get_int("Set the min of the list:")
        self._maxi = self.get_int("Set the max of the list:")
        self._size = self.get_int("Set the size of the list:")
        print(
            "Your config:",
            f"Min: {self._mini}",
            f"Max: {self._maxi}",
            f"Size: {self._size}",
            sep="\n"
        )
        self._the_list = []
        self.get_random_list()

    def get_int(self, info) -> int:
        conf = None
        while not isinstance(conf, int):
            conf = input(info)
            try:
                conf = int(conf)
            except Exception:
                pass
        return conf


class App:
    _app_choices = ['exit', 'config']
    _algos_choices = algos.AlgoFabric.get_choices()
    config = ConfigApp()

    def __init__(self) -> None:
        print("#"*24)
        print("#", " Valbou - Sort Algos", "#")
        print("#", "Version 1.0 (Python)", "#")
        print("#"*24)

    def exec(self) -> None:
        while self.menu():
            pass
        print("#"*24)

    def menu(self) -> bool:
        print("Choose an algo to sort your list (by number or name) :")
        for i, name in enumerate(self._app_choices + self._algos_choices):
            print(f" {i}: {name.capitalize()}")

        choice = self.get_input_choice()
        return self.treat_choice(choice)

    def get_input_choice(self) -> str:
        choice = input('Your choice :')
        result = ""
        try:
            ichoice = int(choice)
            result = (self._app_choices + self._algos_choices)[ichoice]
        except Exception:
            if choice in (self._app_choices + self._algos_choices):
                result = choice
        if result:
            print(f"Selected: {result}")
        return result

    def treat_choice(self, choice: str) -> bool:
        if choice in self._app_choices:
            if choice == 'exit':
                print("Exiting...")
                return False
            elif choice == 'config':
                self.config.manual_config()
                return True

        elif choice in self._algos_choices:
            to_sort = copy(self.config.get_random_list())
            print("List to sort:", to_sort)
            algo = algos.AlgoFabric.get_algo(choice)
            bench = Benchmark()
            with bench:
                result = algo.process(to_sort)
            print("Sorted:", result)
            print(algo)
            print(bench)
            return True

        else:
            return False


if __name__ == "__main__":
    ui = App()
    ui.exec()    
