<html>
    <head></head>
    <link rel="stylesheet" href="/static/bulma.min.css" />
    <body>
        <div class="container card">
        <div class="card-content">
        <h1 class="title">Online File Box</h1>
        <form action="upload.php" method="post" enctype="multipart/form-data">
            <div class="field">
                <div id="file-js" class="file has-name">
                    <label class="file-label">
                        <input class="file-input" type="file" name="file">
                        <span class="file-cta">
                            <span class="file-label">Choose a file...</span>
                        </span>
                        <span class="file-name">No file uploaded</span>
                    </label>
                </div>
            </div>
            <div class="control">
                <input class="button is-success" type="submit" value="submit">
            </div>
        </form>
        </div>
        </div>
        <script>
            const fileInput = document.querySelector('#file-js input[type=file]');
            fileInput.onchange = () => {
                if (fileInput.files.length > 0) {
                const fileName = document.querySelector('#file-js .file-name');
                fileName.textContent = fileInput.files[0].name;
                }
            }
        </script>
    </body>
</html>