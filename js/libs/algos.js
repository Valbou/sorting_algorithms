
class Bubble {
    /*
    * Perf: O(n²) - O(n)
    * Mem: O(n)
    */

    #invert = 0;

    process(toSort) {
        let size = toSort.length;
        let swap = true;
        let fixed = 0;
        while(swap) {
            swap = false;
            for(let i = 0; i < size - fixed; ++i) {
                if(toSort[i] < toSort[i-1]) {
                    // Invert positions
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
    /*
    * Perf: O(n+k) - O(n+k) where k is the count_list size
    * Mem: O(n+k)
    */
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

class Insertion {
    /*
    * Perf: O(n²) - O(n)
    * Mem: O(n)
    */
    #invert = 0;

    process(toSort) {
        toSort.forEach((_, k) => {
            let j = k
            while(j > 0 && toSort[j-1] > toSort[j]) {
                // Invert positions
                let temp = toSort[j-1];
                toSort[j-1] = toSort[j];
                toSort[j] = temp;
                ++this.#invert;
                --j;
            }
        });

        return toSort;
    }

    toString() {
        return `Sorted in ${this.#invert} inverts`;
    }
}

class Selection {
    /*
    * Perf: O(n²) - O(n)
    * Mem: O(n)
    */
    #invert = 0;
    #comp = 0;

    process(toSort) {
        let listSize = toSort.length;
        toSort.forEach((v, k) => {
            let mini = v;
            let index = k;
            for(let j = k; j<listSize; ++j) {
                if(toSort[j] <= mini) {
                    mini = toSort[j];
                    index = j;
                    this.#comp += 1;
                }
            }
            if(index != k) {
                // Invert positions
                let temp = toSort[index];
                toSort[index] = toSort[k];
                toSort[k] = temp; 
                this.#invert += 1;
            }
        });

        return toSort;
    }

    toString() {
        return `Sorted in ${this.#invert} inverts and ${this.#comp} comparisons`;
    }
}

export const algos = {
    "bubble": Bubble,
    "counting": Counting,
    "insertion": Insertion,
    "selection": Selection
}

export function getAlgo(choice) {
    return new algos[choice]();
}
