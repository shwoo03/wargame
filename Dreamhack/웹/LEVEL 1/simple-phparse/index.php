<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <title>PHParse</title>
</head>
<body>


    <!-- php code -->
    <?php
     $url = $_SERVER['REQUEST_URI'];
     $host = parse_url($url,PHP_URL_HOST);
     $path = parse_url($url,PHP_URL_PATH);
     $query = parse_url($url,PHP_URL_QUERY);
     echo "<div><h1> host: $host <br> path: $path <br> query: $query<br></h1></div>";

     if(preg_match("/flag.php/i", $path)){
        echo "<div><h1>NO....</h1></div>";
     }
     else echo "<div><h1>Cannot access flag.php: $path </h1></div> ";
    ?> 

<style type="text/css">
        body {
            margin: 1em;
        }
        div {
            margin: 0 5px 0 0;
            padding: 0.1em;
            border: 2px solid silver;
            border-radius: 7px;
        }

</style>
</body>
</html>