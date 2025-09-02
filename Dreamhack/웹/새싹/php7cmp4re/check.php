<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>php7cmp4re</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">php7cmp4re</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Index page</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
    <div class="container">
    <?php
    require_once('flag.php'); // 'flag.php' 파일을 불러옵니다. 이 파일에는 $flag 변수에 플래그 값이 저장되어 있을 것입니다.
    error_reporting(0); // PHP의 모든 오류 보고를 비활성화합니다. 오류 메시지가 사용자에게 노출되지 않도록 합니다.

    // POST 요청인지 확인합니다.
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // 입력 값 1을 POST 데이터에서 가져옵니다. 값이 없을 경우 빈 문자열로 설정합니다.
        $input_1 = $_POST["input1"] ? $_POST["input1"] : "";
        
        // 입력 값 2를 POST 데이터에서 가져옵니다. 값이 없을 경우 빈 문자열로 설정합니다.
        $input_2 = $_POST["input2"] ? $_POST["input2"] : "";
        
        sleep(1); // 서버에서 1초간 대기합니다. (아마도 타이밍 공격을 방지하기 위해 추가된 코드로 추정됩니다.)

        // 두 입력 값이 모두 빈 문자열이 아닌지 확인합니다.
        if($input_1 != "" && $input_2 != ""){
            // 첫 번째 입력 값의 길이가 4보다 작은지 확인합니다.
            if(strlen($input_1) < 4){
                // 첫 번째 입력 값이 문자열 "8"보다 작은지 확인합니다.
                // 또한, 첫 번째 입력 값이 문자열 "7.A"보다 작고 "7.9"보다 큰지 확인합니다.
                if($input_1 < "8" && $input_1 < "7.A" && $input_1 > "7.9"){
                    // 두 번째 입력 값의 길이가 2인지 확인합니다. (3보다 작고 1보다 큽니다.)
                    if(strlen($input_2) < 3 && strlen($input_2) > 1){
                        // 두 번째 입력 값이 정수 74보다 작고, 문자열 "74"보다 큰지 확인합니다.
                        if($input_2 < 74 && $input_2 > "74"){
                            // 모든 조건을 만족하면 플래그를 출력합니다.
                            echo "</br></br></br><pre>FLAG\n";
                            echo $flag; // flag.php에서 불러온 플래그를 출력합니다.
                            echo "</pre>";
                        } else {
                            // 조건이 맞지 않을 경우 "Good try." 메시지를 출력합니다.
                            echo "<br><br><br><h4>Good try.</h4>";
                        }
                    } else {
                        // 두 번째 입력 값의 길이가 조건을 만족하지 않으면 "Good try." 메시지를 출력합니다.
                        echo "<br><br><br><h4>Good try.</h4><br>";
                    }
                } else {
                    // 첫 번째 입력 값이 조건을 만족하지 않으면 "Try again." 메시지를 출력합니다.
                    echo "<br><br><br><h4>Try again.</h4><br>";
                }
            } else {
                // 첫 번째 입력 값의 길이가 4 이상이면 "Try again." 메시지를 출력합니다.
                echo "<br><br><br><h4>Try again.</h4><br>";
            }
        } else {
            // 두 입력 값 중 하나라도 비어 있으면 "Fill the input box." 메시지를 출력합니다.
            echo '<br><br><br><h4>Fill the input box.</h4>';
        }
    } else {
        // POST 요청이 아닌 경우 "WHat??!" 메시지를 출력합니다.
        echo "<br><br><br><h3>WHat??!</h3>";
    }
?>

    </div> 
</body>
</html>