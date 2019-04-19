<?php
	$message = $_GET['message'];

	// do process message... probably calling python file(?)
	// $result = $message . " - bot";
	// $p = new Python('test','Main');
	$script = "python test.py" . " " . $message;
	$command = escapeshellcmd($script);
	$output = shell_exec($command);
	echo $output;
	// echo $p->getAnswer($message);
	
	// header("location:index.php?result=".$result);
	// echo $result;

?>