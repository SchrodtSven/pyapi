<?php
namespace PyApi\Backend;
require_once 'Http.php';
use PyApi\Backend\Http;

$http = new Http();
echo 'Foo';
?>

<h2><?php echo "I am: " . __FILE__;?></h2>

<p><pre><code><?= $http->debug() ?></code>   
    </pre></p>