<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Loader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>File Content Viewer</h1>
        <?php
        
        define('ALLOW_INCLUDE', true);

        if (isset($_GET['file'])) {
            # 파일 파라미터를 받아옴 
            $encodedFileName = $_GET['file'];

            # Li4v(../) 문자열이 있는지 검사하고 있으면 종료 
            if (stripos($encodedFileName, "Li4v") !== false){
                echo "<p class='error'>Error: Not allowed ../.</p>";
                exit(0);
            }
            # "ZmxhZ"(flag) 또는 "aHA="(hp) 문자열이 있는지 검사하고 있으면 종료
            if ((stripos($encodedFileName, "ZmxhZ") !== false) || (stripos($encodedFileName, "aHA=") !== false)){
                echo "<p class='error'>Error: Not allowed flag.</p>";
                exit(0);
            }

            # 실제 파일명 복원 
            $decodedFileName = base64_decode($encodedFileName);

            $filePath = __DIR__ . DIRECTORY_SEPARATOR . $decodedFileName;

            # 디코딩된 파일 명이 유효하고 파일이 존재하며 현재 디렉토리에서 시작하면 현재 파일 실행 
            if ($decodedFileName && file_exists($filePath) && strpos(realpath($filePath),__DIR__) == 0) {
                echo "<p>Including file: <strong>$decodedFileName</strong></p>";
                echo "<div>";
                require_once($decodedFileName);
                echo "</div>";
            } else {
                echo "<p class='error'>Error: Invalid file or file does not exist.</p>";
            }
        } else {
            echo "<p class='error'>No file parameter provided.</p>";
        }
        ?>
    </div>
</body>
</html>
