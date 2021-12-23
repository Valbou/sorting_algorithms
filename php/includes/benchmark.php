<?php
    class Benchmark {
        private $start;
        private $end;

        public function go() {
            $this->start = microtime(TRUE);
        }

        public function stop() {
            $this->end = microtime(TRUE);
        }

        public function __toString(): string {
            $result = round($this->end - $this->start, 4);
            return "Ran in {$result} seconds\n";
        }
    }
