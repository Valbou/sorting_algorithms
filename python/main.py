#!/usr/bin/env python3
# coding: utf-8

from random import randint
from time import time
import algos


class Benchmark:
    def go(self):
        self.start = time()

    def stop(self):
        self.end = time()

    def __str__(self):
        return f"Ran in {round(self.end - self.start, 4)} seconds"


class ConfigApp:
    _mini = -100
    _maxi = 100
    _size = 50
    _the_list = []
    verbose = True

    def get_random_list(self):
        if len(self._the_list) == 0:
            self._the_list = [randint(self._mini, self._maxi) for _ in range(self._size)]
        return self._the_list

    def manual_config(self):
        print("#"*4, "Configuration", "#"*4)
        print("Min, max and size must be integers")
        self._mini = self.get_int("Set the min of the list:")
        self._maxi = self.get_int("Set the max of the list:")
        self._size = self.get_int("Set the size of the list:")
        self.verbose = self.get_bool("Verbose mode (y/n):")
        print(
            "Your config:",
            f"Min: {self._mini}",
            f"Max: {self._maxi}",
            f"Size: {self._size}",
            f"Verbose: {self.verbose}",
            sep="\n"
        )
        self._the_list = []
        self.get_random_list()

    def get_int(self, info):
        conf = None
        while not isinstance(conf, int):
            conf = input(info)
            try:
                conf = int(conf)
            except Exception:
                pass
        return conf

    def get_bool(self, info):
        conf = input(info)
        if conf.lower() in ['', 'y', 'yes', '1']:
            conf = True
        else:
            conf = False
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

    def menu(self):
        print("Choose an algo to sort your list (by number or name) :")
        for i, name in enumerate(self._app_choices + self._algos_choices):
            print(f" {i}: {name.capitalize()}")

        choice = self.get_input_choice()
        state = self.treat_choice(choice)
        if state is not None:
            self.menu()

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

    def treat_choice(self, choice: str):
        if choice in self._app_choices:
            if choice == 'exit':
                print("Exiting...")
                return None
            if choice == 'config':
                self.config.manual_config()
                return 1

        elif choice in self._algos_choices:
            to_sort = self.config.get_random_list()
            bench = Benchmark()
            if self.config.verbose:
                print("List to sort:", to_sort)
                bench.go()
            algo = algos.AlgoFabric.get_algo(choice)
            result = algo.process(to_sort)
            if self.config.verbose:
                bench.stop()
                print("Sorted:", result)
                algo.show_stats()
                print(bench)
            return 1

        else:
            return None


if __name__ == "__main__":
    ui = App()
    ui.exec()    
