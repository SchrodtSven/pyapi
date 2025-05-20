<?php declare(strict_types=1);
 /**
 * @author Sven Schrodt<sven@schrodt.club>
 * @link https://github.com/SchrodtSven/pyapi
 * @package ApiClient
 * @version 0.1
 * @since 2025-04-28
 */
namespace PyApi\Backend;


error_reporting(E_ALL);
ini_set('display_startup_errors', true);
ini_set('display_errors', true);
if(str_ends_with(getcwd(), 'backend')) {
    chdir('../');
};

//echo 'FOOOO';   

