<?php
namespace PyApi\Backend;
require_once 'Http.php';
use PyApi\Backend\Http;

$http = new Http();

echo $http->debug();