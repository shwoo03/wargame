<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>php7cmp4re</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-stop">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">php7cmp4re</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">index page</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <div class="container">
      <div class="box">
      <h4>Enter the correct Input.</h4>
        <p>
          <form method="post" action="/check.php">
              <input type="text" placeholder="input1" name="input1">
              <input type="text" placeholder="input2" name="input2">
              <input type="submit" value="제출">
          </form>
        </p>
      </div>

    <?php
        require_once('flag.php');
        error_reporting(0);
    ?> 
    </div> 
</body>
</html>