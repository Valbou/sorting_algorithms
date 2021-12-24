<?php

    interface Algo {
        public function process(array $toSort): array;
        public function __toString(): string;
    }

    class Bubble implements Algo {
        /*
        * Perf: O(n²) - O(n)
        * Mem: O(n)
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

        public function __toString(): string {
            return "Sorted in {$this->invert} invert\n";
        }
    }

    class Counting implements Algo {
        /*
        * Perf: O(n+k) - O(n+k) where k is the count_list size
        * Mem: O(n+k)
        */

        private $moves = 0;
        private $count_list_size = 0;

        public function process(array $toSort): array {
            $mini = min($toSort);
            $count_list = $this->initList($toSort, $mini);

            foreach($toSort as $n) {
                ++$count_list[$n - $mini];
            }

            $index = 0;
            foreach($count_list as $k => $v) {
                for($i=0; $i<$v; ++$i) {
                    $toSort[$index] = $k + $mini;
                    ++$this->moves;
                    ++$index;
                }
            }

            return $toSort;
        }

        private function initList(array $toSort, int $mini): array {
            $maxi = max($toSort);
            $this->count_list_size = $maxi - $mini + 1;
            $count_list = array_fill(0, $this->count_list_size, 0);
            return $count_list;
        }

        public function __toString(): string {
            return "Sorted in {$this->moves} moves + {$this->count_list_size}\n";
        }
    }

    class Insertion implements Algo {
        /*
        * Perf: O(n²) - O(n)
        * Mem: O(n)
        */

        private $invert = 0;

        public function process(array $toSort): array {
            foreach($toSort as $k => $v) {
                $j = $k;
                while($j > 0 and $toSort[$j-1] > $toSort[$j]) {
                    // Invert positions
                    $temp = $toSort[$j-1];
                    $toSort[$j-1] = $toSort[$j];
                    $toSort[$j] = $temp;
                    ++$this->invert;
                    --$j;
                }
            }
        
            return $toSort;
        }

        public function __toString(): string {
            return "Sorted in {$this->invert} invert\n";
        }
    }

    class AlgoFabric {
        private static $installed_algos = array('bubble', 'counting', 'insertion');

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

