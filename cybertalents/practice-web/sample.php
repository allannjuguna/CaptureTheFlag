<?php

$code = $_GET['code'];

if(strlen($code)>40){
    die("Long.");
}
if(preg_match("/[A-Za-z0-9]+/",$code)){
    die("NO.");
}
@eval($code);

//$hint =  "php function getFlag() to get flag";
?>
