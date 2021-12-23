<?php
    class ConfigApp {
        private $min = -100;
        private $max = 100;
        private $size = 50;
        private $list = array();
        public $verbose = TRUE;

        public function getRandomList(): array {
            if(count($this->list) == 0) {
                for($i = 0; $i < $this->size; ++$i) {
                    $this->list[] = random_int($this->min, $this->max);
                }
            }
            return $this->list;
        }

        public function manualConfig() {
            echo "#### Configuration ####\n";
            echo "Min, max and size must be integers\n";

            echo "\nSet the min of the list: ";
            trim(fscanf(STDIN, "%d", $this->min));

            echo "\nSet the max of the list: ";
            trim(fscanf(STDIN, "%d", $this->max));

            echo "\nSet the size of the list: ";
            trim(fscanf(STDIN, "%d", $this->size));

            echo "\nVerbose mode (y/n): ";
            trim(fscanf(STDIN, "%s", $this->verbose));

            echo "\nYour config:\n";
            echo "Min: {$this->min}\n";
            echo "Max: {$this->max}\n";
            echo "Size: {$this->size}\n";
            echo "Verbose: {$this->verbose}\n";

            $this->list = array();
            $this->getRandomList();
        }
    }
