<?

$file = file("glyphs.tsv");
$f = fopen("rglyphs.tsv", "w+");
foreach($file as $line) {
	$pair = explode("\t", $line);
	$pair[0] = trim($pair[0]);
	$pair[1] = trim($pair[1]);
	fwrite($f, "$pair[1]\t$pair[0]\n");
}

fclose($f);
