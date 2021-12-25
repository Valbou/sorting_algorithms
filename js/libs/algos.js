
class Bubble {
    #invert = 0;

    process(toSort) {
        let size = toSort.length;
        let swap = true;
        let fixed = 0;
        while(swap) {
            swap = false;
            for(let i = 0; i < size - fixed; ++i) {
                if(toSort[i] < toSort[i-1]) {
                    let temp = toSort[i];
                    toSort[i] = toSort[i-1];
                    toSort[i-1] = temp;
                    ++this.#invert;
                    swap = true;
                }
            }
            ++fixed;
        }
        return toSort;
    }

    toString() {
        return `Sorted in ${this.#invert} inverts`;
    }
}

class Counting {
    #moves = 0;
    #countListSize = 0;

    process(toSort) {
        let min = Math.min(...toSort);
        let countList = this.#initList(min, toSort);

        toSort.forEach(el => {
            ++countList[el - min];
        });

        let index = 0;
        countList.forEach((v, k) => {
            for(let i=0; i<v; ++i) {
                toSort[index] = k + min;
                this.#moves += 1;
                index += 1;
            }
        })

        return toSort;
    }

    #initList(min, toSort) {
        let max = Math.max(...toSort);
        this.#countListSize = max - min + 1;
        return Array(this.#countListSize).fill(0);
    }

    toString() {
        return `Sorted in ${this.#moves} moves + ${this.#countListSize}`;
    }
}

export const algos = {
    "bubble": Bubble,
    "counting": Counting
}

export function getAlgo(choice) {
    return new algos[choice]();
}
