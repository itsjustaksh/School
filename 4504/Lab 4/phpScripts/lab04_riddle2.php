<?php

    function door_lock($grades){
        $lock[] = 'X';

        foreach ($grades as $grade) {
            if ($grade >= 90) {
                $lock[] .= 'A';
            } 
            else if ($grade >= 80){
                $lock[] .= 'B';
            }
            else if ($grade >= 70){
                $lock[] .= 'C';
            }
            else if ($grade >= 60){
                $lock[] .= 'D';
            }
            else if ($grade >= 40){
                $lock[] .= 'E';
            }
            else {
                $lock[] .= 'F';
            }
            
        }

        return $lock;
    }

    $lockVal = door_lock([40, 1000, 63, 80, 100]);
    foreach ($lockVal as $val) {
        printf("%s", $val);
        echo "";
    }
?>