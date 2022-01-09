
    use std::collections::HashMap;
    use std::fmt;

    pub trait Algo: fmt::Display {
        fn process(&mut self, _:&mut Vec<isize>);
    }

    struct Bubble {
        invert:usize
    }

    impl Algo for Bubble {
        fn process(&mut self, list:&mut Vec<isize>){
            // Perf: O(n²) - O(n)
            // Mem: O(n)

            let size = list.len();
            let mut fixed :usize = 0;
            let mut swap :bool = true;

            while swap {
                swap = false;
                for i in 1..(size - fixed) {
                    if list[i] < list[i-1] {
                        let temp = list[i];
                        list[i] = list[i-1];
                        list[i-1] = temp;
                        self.invert+=1;
                        swap = true;
                    }
                }
                fixed+=1;
            }
        }
    }

    impl fmt::Display for Bubble {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "Sorted in {} inverts", self.invert)
        }
    }

    struct Counting {
        moves:usize,
        count_list_size:usize
    }

    impl Algo for Counting {
        fn process(&mut self, list:&mut Vec<isize>){
            // Perf: O(n+k) - O(n+k) where k is the count_list size
            // Mem: O(n+k)

            let min = *list.iter().min().unwrap();
            let max = *list.iter().max().unwrap();
            self.count_list_size = (max - min).abs() as usize + 1_usize;
            let mut vec_counting :Vec<isize> = vec![0; self.count_list_size];

            for i in 0..list.len() {
                vec_counting[(list[i] - min).abs() as usize] += 1;
            }

            let mut index :usize = 0;
            for i in 0..vec_counting.len() {
                for j in 0..vec_counting[i] {
                    list[index] = i as isize + min;
                    self.moves += 1;
                    index += 1;
                }
            }
        }
    }

    impl fmt::Display for Counting {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "Sorted in {} moves + {}", self.moves, self.count_list_size)
        }
    }

    struct Insertion {
        invert:usize
    }

    impl Algo for Insertion {
        fn process(&mut self, list:&mut Vec<isize>){
            // Perf: O(n²) - O(n)
            // Mem: O(n)
        }
    }

    impl fmt::Display for Insertion {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "Sorted in {} inverts", self.invert)
        }
    }

    struct Selection {
        invert:usize,
        comp:usize
    }

    impl Algo for Selection {
        fn process(&mut self, list:&mut Vec<isize>){
            // Perf: O(n²) - O(n)
            // Mem: O(n)
        }
    }

    impl fmt::Display for Selection {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "Sorted in {} inverts and {} comparisons", self.invert, self.comp)
        }
    }

    enum Algos {
        Bubble,
        Counting,
        Insertion,
        Selection,
    }

    pub struct AlgoFabric {
        algos:HashMap<String, Algos>
    }

    impl AlgoFabric {
        pub fn new() -> AlgoFabric {
            AlgoFabric{
                algos:HashMap::from([
                    ("Bubble".to_string(), Algos::Bubble),
                    ("Counting".to_string(), Algos::Counting),
                    ("Insertion".to_string(), Algos::Insertion),
                    ("Selection".to_string(), Algos::Selection)
                ])
            }
        }

        pub fn get_algos(&self) -> Vec<String> {
            return self.algos.keys().map(|x| x.to_string()).collect();
        }

        pub fn get_algo(&self, choice:String) -> Box<dyn Algo> {
            match self.algos.get(choice.as_str()) {
                Some(e) => {
                    match e {
                        Algos::Bubble => Box::new(Bubble{invert:0}),
                        Algos::Counting => Box::new(Counting{moves:0, count_list_size:0}),
                        Algos::Insertion => Box::new(Insertion{invert:0}),
                        Algos::Selection => Box::new(Selection{invert:0, comp:0})
                    }
                },
                None => Box::new(Bubble{invert:0})
            }
        }
    }

