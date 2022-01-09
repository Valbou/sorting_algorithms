
mod algos;


use std::time::Instant;
use std::fmt;
use std::io;
use rand::prelude::*;
use algos::AlgoFabric;


fn get_integer(info:&str) -> isize {
    let mut input:String = String::new();
    println!("{}", info);
    io::stdin().read_line(&mut input).expect("Input error.");
    match input.trim().parse() {
        Ok(v) => {
            v
        }
        Err(_e) => {
            println!("Please enter a numeric value.");
            get_integer(info)
        }
    }
}

struct SliceDisplay<'a, T: 'a>(&'a [T]);

impl<'a, T: fmt::Display + 'a> fmt::Display for SliceDisplay<'a, T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut first = true;
        for item in self.0 {
            if !first {
                write!(f, ", {}", item)?;
            } else {
                write!(f, "{}", item)?;
            }
            first = false;
        }
        Ok(())
    }
}


struct Benchmark {
    start: Option<Instant>,
    end: Option<Instant>,
}

impl Benchmark {
    fn go(&mut self) {
        self.start = Some(Instant::now());
    }

    fn stop(&mut self) {
        self.end = Some(Instant::now());
    }
}

impl fmt::Display for Benchmark {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Ran in {:?} ms", ((self.end).unwrap() - (self.start).unwrap()).as_millis());
        Ok(())
    }
}


struct ConfigApp {
    min: isize,
    max: isize,
    size: usize,
    list: Vec<isize>
}

impl ConfigApp {
    fn new() -> ConfigApp {
        ConfigApp{min:-100, max:100, size:50, list:Vec::with_capacity(50_usize)}
    }

    fn get_random_list(&mut self) -> Vec<isize> {
        if self.list.len() == 0 {
            let mut rng = thread_rng();
            self.list = (0..self.size).map(|_| rng.gen_range(self.min..self.max)).collect();
        }

        self.list.to_vec()
    }

    fn manual_config(&mut self) {
        println!("#### Configuration ####");
        println!("Min, max and size must be integers");
        self.min = get_integer("Set the min of the list:");
        self.max = get_integer("Set the max of the list:");
        let mut size = get_integer("Set the size of the list:");
        while size <= 0 {
            size = get_integer("Set the size of the list:");
        }
        self.size = size as usize;

        println!(
            "Your config:\n\
            Min: {}\n\
            Max: {}\n\
            Size: {}\n",
            self.min, self.max, self.size
        );

        self.list.clear();
        self.get_random_list();
    }
}


pub struct App {
    app_choices: Vec<String>,
    algo_choices: Vec<String>,
    config: ConfigApp,
    fabric: AlgoFabric
}

impl App {
    pub fn new() -> App {
        let mut app = App{
            app_choices:vec![
                String::from("exit"),
                String::from("config")
            ],
            algo_choices:vec!(),
            config:ConfigApp::new(),
            fabric:AlgoFabric::new()
        };
        app.algo_choices = app.fabric.get_algos();

        app
    }

    pub fn exec(&mut self) {
        while self.menu() {}
        println!("{}", "#".repeat(24));
    }

    fn get_choices(&self) -> Vec<String> {
        let mut choices = self.app_choices.clone();
        choices.extend(self.algo_choices.clone());

        choices
    }

    fn menu(&mut self) -> bool {
        println!("Choose an algo to sort your list (by number) :\n");
        let choices = self.get_choices();
        for i in 0..choices.len() {
            println!(" {}: {}", i, choices[i]);
        }

        let choice = get_integer("") as usize;

        self.treat_choice(choice)
    }

    fn treat_choice(&mut self, choice:usize) -> bool {
        if choice < self.app_choices.len()
        {
            if self.app_choices[choice] == "exit".to_string() {
                    println!("Exiting...");
                    false
            }
            else if self.app_choices[choice] == "config".to_string() {
                self.config.manual_config();
                true
            }
            else {
                true
            }
        }
        else if self.app_choices.len() <= choice && choice < self.get_choices().len() {
            let choices = self.get_choices();
            let res = choices.get(choice).unwrap().to_string();
            let mut algo = self.fabric.get_algo(res);
            let mut bench = Benchmark{start:None, end:None};
            let mut list = self.config.get_random_list();

            println!("List to sort: {}\n", SliceDisplay(&list));

            bench.go();
            algo.process(&mut list);
            bench.stop();

            println!("Sorted: {}\n", SliceDisplay(&list));
            println!("{}\n{}\n", algo, bench);

            true
        }
        else {
            false
        }
    }
}
