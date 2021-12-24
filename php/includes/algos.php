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
            return "Sorted in {$this->invert} inverts\n";
        }
    }

    class Counting implements Algo {
        /*
        * Perf: O(n+k) - O(n+k) where k is the count_list size
        * Mem: O(n+k)
        */

        private $moves = 0;
        private $countListSize = 0;

        public function process(array $toSort): array {
            $mini = min($toSort);
            $countList = $this->initList($toSort, $mini);

            foreach($toSort as $n) {
                ++$countList[$n - $mini];
            }

            $index = 0;
            foreach($countList as $k => $v) {
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
            $this->countListSize = $maxi - $mini + 1;
            $countList = array_fill(0, $this->countListSize, 0);
            return $countList;
        }

        public function __toString(): string {
            return "Sorted in {$this->moves} moves + {$this->countListSize}\n";
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
            return "Sorted in {$this->invert} inverts\n";
        }
    }

    class Selection implements Algo {
        /*
        * Perf: O(n²) - O(n)
        * Mem: O(n)
        */

        private $invert = 0;
        private $comp = 0;

        public function process(array $toSort): array {
            $listSize = count($toSort);
            for($k=0; $k < $listSize; ++$k) {
                $mini = $toSort[$k];
                $index = $k;
                foreach(range($k, $listSize-1) as $j) {
                    if($toSort[$j] <= $mini) {
                        $mini = $toSort[$j];
                        $index = $j;
                        ++$this->comp;
                    }
                }
                if($index != $k) {
                    # Invert positions
                    $temp = $toSort[$index];
                    $toSort[$index] = $toSort[$k];
                    $toSort[$k] = $temp;
                    ++$this->invert;
                }
            }

            return $toSort;
        }

        public function __toString(): string {
            return "Sorted in {$this->invert} inverts and {$this->comp} comparisons\n";
        }
    }

    class AlgoFabric {
        private static $installed_algos = array('bubble', 'counting', 'insertion', 'selection');

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

