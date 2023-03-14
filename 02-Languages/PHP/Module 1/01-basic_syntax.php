<?php

// This is single line comment
	
/*
	This is multiline comment
*/

/**
 * These are doc Blocks i.e. documentation comment
 */ 
echo "Comments";

$br = "\n";

// Double quote string for escape characters and for string interpolation
echo "Hello World{$br}";

// Single quote string won't support this
echo 'Hello World{$br}';

print $br;

echo print 'Hello';

print $br;

$var1 = 10;

var_dump($var1);
echo gettype($var1);