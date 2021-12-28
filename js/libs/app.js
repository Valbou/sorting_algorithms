import { algos, getAlgo } from "./algos.js";

function getRandInt(min, max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

async function prompt(message) {
    const buf = new Uint8Array(1024);
    await Deno.stdout.write(new TextEncoder().encode(message));
    const n = await Deno.stdin.read(buf);
    return new TextDecoder().decode(buf.subarray(0, n)).trim();
}

class Benchmark {
    #start;
    #end;

    go() {
        this.#start = Date.now();
    }

    stop() {
        this.#end = Date.now();
    }

    toString() {
        return `Ran in ${(this.#end - this.#start)} ms`;
    }
}

class ConfigApp {
    #mini = -100;
    #maxi = 100;
    #size = 50;
    #theList = [];

    getRandomList() {
        if(this.#theList.length == 0) {
            this.#theList = [...Array(this.#size)].map(x => getRandInt(this.#mini, this.#maxi));
        }
        return this.#theList;
    }

    async manualConfig() {
        console.log("#### Configuration ####");
        console.log("Min, max and size must be integers");
        this.#mini = await this.getInt("Set the min of the list:");
        this.#maxi = await this.getInt("Set the max of the list:");
        this.#size = await this.getInt("Set the size of the list:");
        console.log("Your config:");
        console.log(`Min: ${this.#mini}`);
        console.log(`Max: ${this.#maxi}`);
        console.log(`Size: ${this.#size}`);
        this.#theList = [];
        this.getRandomList();
    }

    async getInt(info) {
        let conf = "";
        while(typeof conf !== 'number') {
            conf = await prompt(info);
            conf = parseInt(conf);
        }
        return conf;
    }
}

export class App {
    #appChoices;
    #algosChoices;
    #config;

    constructor() {
        this.#appChoices = ['exit', 'config'];
        this.#algosChoices = Object.keys(algos);
        this.#config = new ConfigApp();

        console.log("############################");
        console.log("#    Valbou - Sort Algos   #");
        console.log("# Version 1.0 (JavaScript) #");
        console.log("############################");
    }

    async exec() {
        while(await this.menu()) {}
        console.log("############################");
    }

    async menu() {
        console.log("Choose an algo to sort your list (by number or name) :");
        let choices = this.#appChoices.concat(this.#algosChoices);
        choices.forEach((el, i) => console.log(` ${i}: ${el.toLowerCase()}`));

        let choice = await this.getInputChoice();
        return await this.treatChoice(choice);
    }

    async getInputChoice() {
        let choice = await prompt('Your choice:');
        let result = "";

        let ichoice = parseInt(choice);
        if(typeof ichoice == 'number') {
            result = this.#appChoices.concat(this.#algosChoices)[ichoice];
        }
        else {
            if(this.#appChoices.concat(this.#algosChoices).indexOf(choice) >= 0) {
                result = choice;
            }
        }
        if(result) {
            console.log(`Selected: ${result}`);
        }
        return result;
    }

    async treatChoice(choice) {
        if(this.#appChoices.indexOf(choice) >= 0) {
            if(choice === 'exit') {
                console.log("Exiting...");
                return false;
            }
            else if(choice === 'config') {
                await this.#config.manualConfig();
                return true;
            }
        }

        else if(this.#algosChoices.indexOf(choice) >= 0) {
            let toSort = this.#config.getRandomList();
            console.log("List to sort: ", toSort);
            let bench = new Benchmark();
            bench.go();
            let algo = getAlgo(choice);
            let result = algo.process([...toSort]);
            bench.stop(0);
            console.log("Sorted: ", result);
            console.log(algo.toString());
            console.log(bench.toString());
            return true;
        }
        return false;
    }
}
