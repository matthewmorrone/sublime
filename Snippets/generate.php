<?



$file = file("glyphs.tsv");
$dir = "snippets";
@mkdir($dir);

foreach($file as $line) {
	if (!$line || trim($line) === "") {continue;}
	$pair = explode("\t", $line);
	$tabTrigger = trim($pair[0]);
	$content = trim($pair[1]);
	if ($pair[2]) {
		$name = trim($pair[2]);
	}
	else {
		$name = trim($pair[0]);
	}
	if ($pair[3]) {
		$pair[3] = trim($pair[3]);
		$name = $pair[3]."-".$name;
	}
	$nameline = "	<!-- $name -->";
	// echo $content, $tabTrigger, "\n";
	$temp = "<snippet>
$nameline
	<content>$content</content>
	<tabTrigger>$tabTrigger</tabTrigger>
	<!-- <scope></scope> -->
</snippet>
";
	$f = fopen("$dir/$name.sublime-snippet", "w+");
	fwrite($f, $temp);
	fclose($f);
}

