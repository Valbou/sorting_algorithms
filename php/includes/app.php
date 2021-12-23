<?php
    include('algos.php');
    include('benchmark.php');
    include('configapp.php');

    class App {
        private $app_choices = array();
        private $algo_choices = array();
        private $config = null;

        public function __construct() {
            $this->config = new ConfigApp();
            $this->app_choices = array('exit', 'config');
            $this->algo_choices = AlgoFabric::getChoices();

            echo "#######################\n";
            echo "# Valbou - Sort Algos #\n";
            echo "#  Version 1.0 (PHP)  #\n";
            echo "#######################\n";
        }

        public function menu() {
            echo "\nChoose an algo to sort your list (by number or name) :\n";
            $choices = array_merge($this->app_choices, $this->algo_choices);
            foreach($choices as $key => $option) {
                echo "{$key}: ". ucwords($option) ."\n";
            }
            $choice = $this->getInputChoice();
            $state = $this->treatChoice($choice);
            if($state) {
                $this->menu();
            }
        }

        public function treatChoice(string $choice): int {
            if(in_array($choice, $this->app_choices)) {
                switch($choice) {
                    case 'exit':
                        echo "Exiting...";
                        return 0;
                    case 'config':
                        $this->config->manualConfig();
                        return 1;
                }
            }
            else if(in_array($choice, $this->algo_choices)) {
                $toSort = $this->config->getRandomList();
                $bench = new Benchmark();
                if($this->config->verbose) {
                    echo "\nList to sort:";
                    print_r($toSort);
                    $bench->go();
                }
                $algo = AlgoFabric::getAlgo($choice);
                $sorted = $algo->process($toSort);
                if($this->config->verbose) {
                    $bench->stop();
                    echo "\nSorted:";
                    print_r($sorted);
                    $algo->showStats();
                    echo (string) $bench;
                }
                return 1;
            }
            return 0;
        }

        public function getInputChoice(): string {
            $input = trim(fgets(STDIN));
            $result = "";
            $options = array_merge($this->app_choices, $this->algo_choices);
            if(is_numeric($input)) {
                $input = (int) $input;
                if(0 <= $input && $input < count($options)) {
                    $result = ($options)[$input];
                }
            }
            else {
                foreach(($options) as $choice) {
                    if($choice == $input) {
                        $result = $choice;
                    }
                }
            }
            return $result;
        }

        public function exec() {
            while($this->menu()) {}
            echo "\n#######################\n";
        }
    }
