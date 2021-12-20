
class Algo:
    def process(self, to_sort: list, stats: bool = False) -> list:
        raise NotImplementedError(
            f"Algo process method not implemented for {self.__class__.__name__}"
        )

    def show_stats(self):
        raise NotImplementedError(
            f"Algo show_stats method not implemented for {self.__class__.__name__}"
        )


class Bubble(Algo):
    invert = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        list_size = len(to_sort)
        for _ in range(list_size):
            index = list_size - 1
            for j in range(list_size):
                if to_sort[index] > to_sort[index-1] and (index - 1) > 0:
                    # Invert positions
                    to_sort[index], to_sort[index-1] = to_sort[index-1], to_sort[index]
                    self.invert += 1
                index -= 1

        if stats:
            self.show_stats()

        return to_sort

    def show_stats(self):
        print(f"Sorted in {self.invert} invert")


class Counting(Algo):
    moves = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        mini, count_list = self._init_list(to_sort)

        for n in to_sort:
            count_list[n - mini] += 1
        index = 0
        for k, v in enumerate(count_list):
            for _ in range(v):
                to_sort[index] = k + mini
                index += 1
        return to_sort

    def _init_list(self, to_sort: list) -> tuple:
        mini = min(to_sort)  # Used to shift negative numbers
        maxi = max(to_sort)
        count_list = [0 for _ in range(maxi - mini)]
        return mini, count_list

    def show_stats(self):
        print(f"Sorted in {self.moves} moves")


class Insertion(Algo):
    invert = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        list_size = len(to_sort)
        for i in range(list_size):
            j = i
            while j > 0 and j < list_size and to_sort[j-1] > to_sort[j]:
                # Invert positions
                to_sort[j-1], to_sort[j] = to_sort[j], to_sort[j-1]
                self.invert += 1
        return to_sort

    def show_stats(self):
        print(f"Sorted in {self.invert} invert")


class Selection(Algo):
    invert = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        list_size = len(to_sort)
        for i in range(list_size):
            mini = to_sort[i]
            index = i
            for j in range(list_size):
                if to_sort[j] <= mini:
                    mini = to_sort[j]
                    index = j
            if index != i:
                # Invert positions
                to_sort[index], to_sort[i] = to_sort[i], to_sort[index]
                self.invert += 1
        return to_sort

    def show_stats(self):
        print(f"Sorted in {self.invert} invert")


class AlgoFabric:
    installed_algos = [Bubble, Counting, Insertion, Selection]

    @classmethod
    def get_algo(cls, choice: str) -> Algo:
        for algo in cls.installed_algos:
            if algo.__name__.lower() == choice.lower():
                return algo()
        return None

    @classmethod
    def get_choices(cls) -> list:
        return [algo.__name__.capitalize() for algo in cls.installed_algos]
