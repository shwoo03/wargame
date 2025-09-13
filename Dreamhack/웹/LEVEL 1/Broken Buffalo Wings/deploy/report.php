<?php

# path 값이 있으면 받고 없으면 haha 기본 값 
$path = $_POST["path"] ?? "haha";
if(isset($_POST["path"])){
    # path 값을 인자로 bot.py 실행
    $arg = escapeshellarg($path);
    $result = shell_exec("python3 ./bot/bot.py {$arg}");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>

<body>
    <div class="container mt-5">
        <h2>Report</h2>
        <form method="post" action="/report.php">
            <div class="form-group">
                <label for="reportTitle">Admin will check your request</label>
                <input type="text" class="form-control" name="path" id="path" placeholder="/?key=value">
            </div>
            <button type="submit" class="btn btn-outline-primary">Report</button>
        </form>
    </div>


    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.bundle.min.js"></script>
</body>

</html>
