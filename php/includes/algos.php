<?php

    interface Algo {
        public function process(array $toSort): array;
        public function showStats();
    }

    class Bubble implements Algo {
        /*
            Perf: O(n²) - O(n)
            Mem: O(n)
        */

        private $invert = 0;

        public function process(array $toSort): array {
            $size = count($toSort);
            $swap = TRUE;
            $fixed = 0;

            while($swap) {
                $swap = FALSE;
                for($i=1; $i < ($size - $fixed); ++$i) {
                    if($toSort[$i] < $toSort[$i-1]) {
                        // invert positions
                        $temp = $toSort[$i];
                        $toSort[$i] = $toSort[$i-1];
                        $toSort[$i-1] = $temp;
                        ++$this->invert;
                        $swap = TRUE;
                    }
                }
                ++$fixed;
            }
            return $toSort;
        }

        public function showStats() {
            echo "Sorted in {$this->invert} invert\n";
        }
    }

    class AlgoFabric {
        private static $installed_algos = array('bubble');

        public static function getAlgo(string $choice): Algo {
            $algo = ucwords($choice);
            if(in_array($algo, AlgoFabric::getChoices())) {
                return new $algo();
            }
            throw new Exception("No algo found named $choice");
        }

        public static function getChoices(): array {
            return array_map('ucwords', AlgoFabric::$installed_algos);
        }
    }

