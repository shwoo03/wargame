<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>Type c-j</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">Type c-j</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">index page</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav><br/><br/><br/>
    <div class="container">
      <div class="box">
      <h4>Enter the correct ID & Password.</h4>
        <p>
          <form method="post" action="/check.php">
              <input type="text" placeholder="Id" name="input1">
              <input type="text" placeholder="Password" name="input2">
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