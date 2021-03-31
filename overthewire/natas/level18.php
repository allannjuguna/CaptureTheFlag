<?php


#TRUE
$hex=0x342;
$num=234;
$num_string="22";
$exponential=5e5;
$exponentialstring="5e5";



#FALSE
$string="allan";
$hexstring="0x2d";
$array=array("shit");
$NULL=NULL;



/*$NaN=NaN;*/








var_dump('\n               string => '.is_numeric($string));
var_dump('\n               hex => '.is_numeric($hex));
var_dump('\n               hexstring => '.is_numeric($hexstring));
var_dump('\n               num => '.is_numeric($num));
var_dump('\n               num_string => '.is_numeric($num_string));
var_dump('\n               array => '.is_numeric($array));
var_dump('\n               exponential => '.is_numeric($exponential));
var_dump('\n               exponentialstring => '.is_numeric($exponentialstring));
/*print('NaN => '.is_numeric($NaN));*/
var_dump('\n               NULL => '.is_numeric($NULL));


function isValidAdminLogin($string) { 
    if($string == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
} 

print('Function result is : '.isValidAdminLogin($NULL));


?>

<!-- 
Step 1 ; remove PHPSESSID from cookie or make PHPSESSID a string
Step 2 : -->



