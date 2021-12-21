#!/usr/bin/env python3
# coding: utf-8

from random import randint
import algos


class ConfigApp:
    mini = -100
    maxi = 100
    size = 50
    verbose = True

    def get_random_list(self):
        return [randint(self.mini, self.maxi) for _ in range(self.size)]

    def manual_config(self):
        print("#"*4, "Configuration", "#"*4)
        print("Min, max and size must be integers")
        self.mini = self.get_int("Set the min of the list:")
        self.maxi = self.get_int("Set the max of the list:")
        self.size = self.get_int("Set the size of the list:")
        self.verbose = self.get_bool("Verbose mode (y/n):")
        print(
            "Your config:",
            f"Min: {self.mini}",
            f"Max: {self.maxi}",
            f"Size: {self.size}",
            f"Verbose: {self.verbose}",
            sep="\n"
        )

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
    limit = 3
    stats = True
    app_choices = ['exit', 'config']
    algos_choices = algos.AlgoFabric.get_choices()
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
        for i, name in enumerate(self.app_choices + self.algos_choices):
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
            result = (self.app_choices + self.algos_choices)[ichoice]
        except Exception:
            if choice in (self.app_choices + self.algos_choices):
                result = choice
        if result:
            print(f"Selected: {result}")
        return result

    def treat_choice(self, choice: str):
        if choice in self.app_choices:
            if choice == 'exit':
                print("Exiting...")
                return None
            if choice == 'config':
                self.config.manual_config()
                return 1

        elif choice in self.algos_choices:
            to_sort = self.config.get_random_list()
            if self.config.verbose:
                print("List to sort:", to_sort)
            algo = algos.AlgoFabric.get_algo(choice)
            result = algo.process(to_sort, self.config.verbose)
            if self.config.verbose:
                print("Sorted:", result)
            return 1

        else:
            return None


if __name__ == "__main__":
    ui = App()
    ui.exec()    
