<?

$from = $argv[1];
$to = $argv[2];
$dir = new DirectoryIterator($from);
@mkdir($to);
foreach ($dir as $fileinfo) {
	$name = $fileinfo->getFilename();

	if (substr($name, 0, 1) == ".") {continue;}

	$pathname = $fileinfo->getPathname();
	$filename = $fileinfo->getFilename();
	$filename = str_replace("Category-", "", $filename);
	$filename = str_replace(".plist", "", $filename);
	$filename = strtolower($filename);
	$dest = "$to/$filename.$to";


	$go = [
		'{"CVCategoryData":{"Data":"',
		'"}}',
		'}}',
		'"CVSkipNullGlyphs":true}}',
		'"CVCategoryDigestData":""}',
		'"',
		'}',
		':',
		'CVSkipNullGlyphstrue'

	];

	$contents = file_get_contents($pathname);
	$contents = str_replace(",", "\n", $contents);




	foreach($go as $g) {
		$contents = str_replace($g, "", $contents);
	}
	// $contents = preg_replace('/([\w{}:"]{2,})/', "\n", $contents);


	// $contents = str_replace('"}}', "", $contents);
	// $contents = preg_replace("/\n.{3}\n/", "\n\n", $contents);

	$f = fopen($dest, "w+");
	fwrite($f, $contents);
	fclose($f);


}


// print_r($fns);

