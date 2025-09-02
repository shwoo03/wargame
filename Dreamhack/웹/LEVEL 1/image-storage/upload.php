<?php
  if ($_SERVER['REQUEST_METHOD'] === 'POST') {  # POST 방식으로 요청이 들어왔을 때
    if (isset($_FILES)) {   # 파일이 업로드 되었을 때 
      $directory = './uploads/';   # 저장할 디렉터리 경로 
      $file = $_FILES["file"];     # 파일의 정보를 담는 변수 
      $error = $file["error"];     # 업로드 중 발생한 에러 코드를 담는 변수
      $name = $file["name"];       # 업로드한 파일의 이름을 담는 변수
      $tmp_name = $file["tmp_name"];    # 업로드한 파일의 임시 경로를 담는 변수
     
      if ( $error > 0 ) {
        echo "Error: " . $error . "<br>";   # 에러 검사 
      }else {
        if (file_exists($directory . $name)) {   # 파일이 이미 존재하는지 검사
          echo $name . " already exists. ";
        }else {
          if(move_uploaded_file($tmp_name, $directory . $name)){   # 파일을 업로드할 디렉터리로 이동
            echo "Stored in: " . $directory . $name;
          }
        }
      }
    }else {
        echo "Error !";
    }
    die();
  }
?>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>Image Storage</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">Image Storage</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="/">Home</a></li>
            <li><a href="/list.php">List</a></li>
            <li><a href="/upload.php">Upload</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav><br/><br/><br/>
    <div class="container">
      <form enctype='multipart/form-data' method="POST">
        <div class="form-group">
          <label for="InputFile">파일 업로드</label>
          <input type="file" id="InputFile" name="file">
        </div>
        <input type="submit" class="btn btn-default" value="Upload">
      </form>
    </div> 
</body>
</html>