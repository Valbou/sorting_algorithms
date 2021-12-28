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

        public function menu(): bool {
            echo "\nChoose an algo to sort your list (by number or name) :\n";
            $choices = array_merge($this->app_choices, $this->algo_choices);
            foreach($choices as $key => $option) {
                echo "{$key}: ". ucwords($option) ."\n";
            }
            $choice = $this->getInputChoice();
            return $this->treatChoice($choice);
        }

        public function treatChoice(string $choice): bool {
            if(in_array($choice, $this->app_choices)) {
                switch($choice) {
                    case 'exit':
                        echo "Exiting...";
                        return FALSE;
                    case 'config':
                        $this->config->manualConfig();
                        return TRUE;
                }
            }
            else if(in_array($choice, $this->algo_choices)) {
                $toSort = $this->config->getRandomList();
                $bench = new Benchmark();
                echo "\nList to sort:";
                print_r($toSort);
                $bench->go();
                $algo = AlgoFabric::getAlgo($choice);
                $sorted = $algo->process($toSort);
                $bench->stop();
                echo "\nSorted:";
                print_r($sorted);
                echo (string) $algo;
                echo (string) $bench;
                return TRUE;
            }
            return FALSE;
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
