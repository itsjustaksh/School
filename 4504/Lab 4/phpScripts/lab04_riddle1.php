<?php 
    $lock = 0;
    $z = 11;

    for($x = 0; ;){
        $y = 1;
        while ($y < $x) {
            $lock = $lock + ($x * $y);
            $y++;
        }
    }
?>