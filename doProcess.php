<?php
	$message = $_GET['message'];

	// do process message... probably calling python file(?)
	$result = $message . " - bot";
	
	// header("location:index.php?result=".$result);
	echo $result;

