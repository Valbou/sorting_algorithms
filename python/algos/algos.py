
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
        swap = True
        fixed = 0
        while swap:
            swap = False
            for i in range(1, list_size - fixed):
                if to_sort[i] < to_sort[i-1]:
                    # Invert positions
                    to_sort[i], to_sort[i-1] = to_sort[i-1], to_sort[i]
                    self.invert += 1
                    swap = True
            fixed += 1

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
        mini = min(to_sort)  # Used to shift negative numbers and optimize positive only not zero started
        maxi = max(to_sort)
        count_list = [0 for _ in range(maxi - mini + 1)]
        return mini, count_list

    def show_stats(self):
        print(f"Sorted in {self.moves} moves")


class Insertion(Algo):
    invert = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        for k, v in enumerate(to_sort):
            j = k
            while j > 0 and to_sort[j-1] > to_sort[j]:
                # Invert positions
                to_sort[j-1], to_sort[j] = to_sort[j], to_sort[j-1]
                self.invert += 1
                j -= 1

        return to_sort

    def show_stats(self):
        print(f"Sorted in {self.invert} invert")


class Selection(Algo):
    invert = 0

    def process(self, to_sort: list, stats: bool = False) -> list:
        list_size = len(to_sort)
        for k, v in enumerate(to_sort):
            mini = v
            index = k
            for j in range(k, list_size):
                if to_sort[j] <= mini:
                    mini = to_sort[j]
                    index = j
            if index != k:
                # Invert positions
                to_sort[index], to_sort[k] = to_sort[k], to_sort[index]
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
