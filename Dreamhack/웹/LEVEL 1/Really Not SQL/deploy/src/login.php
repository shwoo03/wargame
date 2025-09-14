<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $userDir = __DIR__ . '/user/';
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    $filename = $username . '.json';
    $filepath = $userDir . $filename;

    if ($username !== "admin" && $username !== "guest") {
        $error = "User not found";
    } else {
        $userData = json_decode(file_get_contents($filepath), true);
        if ($userData['id'] !== $username){
            $error = "Error occured";
        } else if ($userData['password'] !== hash("sha256", $password)) {
            $error = "Invalid password";
        } else {
            $_SESSION['user'] = $username;
            $success = true;
        }
    }
    
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<div class="container">
    <h1>Login</h1>
    <form method="post" action="login.php">
        <label for="username">User ID</label>
        <input type="text" id="username" name="username" required>

        <label for="password">Password</label>
        <input type="password" id="password" name="password" required>

        <button type="submit">Login</button>
    </form>
</div>

<?php if ($error): ?>
<script>
    alert("<?= $error ?>");
</script>
<?php elseif ($success): ?>
<script>
    alert("Hello <?= $username ?>");
    window.location.href = "/";
</script>
<?php endif; ?>

</body>
</html>
