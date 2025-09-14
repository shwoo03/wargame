<?php
session_start();

if ($_SESSION['user'] !== "admin") {
    $error = "Only admin can edit user profile";
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && $_SESSION['user'] === "admin") {
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
        }
        else {
            $userData['password'] = hash("sha256", $password);
            file_put_contents($filepath, json_encode($userData));
            $success = true;
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Profile</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<div class="container">
    <h1>Edit Profile</h1>
    <form method="post" action="edit_profile.php">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" required>

        <label for="password">New Password</label>
        <input type="password" id="password" name="password" required>

        <button type="submit">Update</button>
    </form>
</div>

<?php if ($error): ?>
<script>
    alert("<?= $error ?>");
    window.location.href = "/";
</script>
<?php elseif ($success): ?>
<script>
    alert("OK");
    window.location.href = "/";
</script>
<?php endif; ?>

</body>
</html>
