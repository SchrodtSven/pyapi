<?php

declare(strict_types=1);
/**
 * @author Sven Schrodt<sven@schrodt.club>
 * @link https://github.com/SchrodtSven/pyapi
 * @package PyApi
 * @version 0.1
 * @since 2025-04-28
 */

namespace PyApi\Backend;

class Http
{
    private string $method;

    private $ct = 'application/json'; 
    private array $dta;

    public function __construct( ) 
    {
        $this->method = $_SERVER['REQUEST_METHOD'];
    }

    public function debug(): string
    {
        switch($this->method) {
            case 'POST':
                $this->dta = $_POST;
                break;
            case 'PUT':
                $this->dta = $this->getPutParams();
                break;
            default:
                $this->dta = $_REQUEST;
        }

        $this->handleContentType();
        $this->dta = array_merge($this->dta, $_SERVER);
        return json_encode($this->dta);
    }

    public function trimme(string $input): string
    {
        $output = preg_replace('! \s+! ', '', $input);
        return trim(str_replace(['Array', '(', ')'], '', $output));
    }

    private function handleContentType()
    {
        $this->ct = $_REQUEST['ct'] ?? null;
        header('Content-Type: application/json');
        #@FIXME
        return true;

        // ob_start();
        print_r(['UA' => $_SERVER['HTTP_USER_AGENT'], 'method' => strtolower($this->method)]);
        print_r($this->dta);

        $outp = ob_get_contents();
        ob_end_clean();
        return $this->trimme($outp);
    }


    public function getParams(): array
    {
        return match($this->method) {
            'PUT' => $this->getPutParams(),
            'POST' => $_POST,
            'GET' => $_GET, 
            default => $_REQUEST
        };
    }

    public function getPutParams(): array
    {
        $tmp = [];
        // Getting payload from input stream (<STDIN>) and parse it to assoc. array 
        parse_str(file_get_contents('php://input'), $tmp);
        return $tmp;
    }
}
