<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buffalo Wings</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
</head>

<body>
    <div class="container my-5">
        <figure class="text-center">
            <blockquote class="blockquote">
                <h2>Food Post</h2>
            </blockquote>
            <figcaption class="blockquote-footer">
                Descriptions from <cite title="Source Title">ChatGPT</cite>
            </figcaption>
        </figure>
        <div class="row">
            <div class="col-md-6 offset-md-3">
                <div class="card">
                    <img class="card-img-top" src="./img/bw.jpeg" alt="Buffalo-Wing">
                    <div class="card-body">
                        <h4 class="card-title">Buffalo Wings</h4>
                        <p class="card-text">Buffalo wings, also known as hot wings or chicken wings, are a popular
                            American dish. They are named after their city of origin, Buffalo, New York, where they were
                            first served at a local restaurant called the Anchor Bar in 1964.

                            Buffalo wings are typically deep-fried without any breading and then coated in a
                            vinegar-based cayenne pepper hot sauce and melted butter. They are traditionally served with
                            celery sticks and blue cheese or ranch dressing for dipping.

                            Buffalo wings are often spicy with varying levels of heat based on the hot sauce used, but
                            they can also be prepared with other flavors like barbecue, honey mustard, or teriyaki.

                            Buffalo wings are a popular dish in bars and restaurants, especially during sporting events.
                            They are also a common appetizer and party food, and many places have wing eating contests
                            or "all you can eat" wings specials.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="text-center">
        <?php   
                # comment 를 GET으로 받고 500글자 이상은 안됨 
                if (strlen($_GET['comment'])>500){
                    echo 'Too Long';
                    die();

                }

                # comment에 lol이 포함되어 있으면 Dreame : Looks delicious ~~ But I like pizza more  출력
                # comment에 script가 포함되어 있으면 script 문자열을 제거하고 Malicious string Detected !!!!! 출력
                if (isset($_GET['comment'])) {
                    $comment = $_GET['comment'];

                    if (strpos($comment, 'lol') !== false){
                        $prefix = 'Dreame : Looks delicious ~~ But I like pizza more ';
                        echo $prefix . $comment;
                    }

                    if (strpos($comment, 'script') !== false){
                        $untrusted_comment = $_GET['comment'];

                        while (strpos($untrusted_comment, 'script') !== false) {
                            $alert = 'Malicious string Detected !!!!!';
                            $untrusted_comment = str_replace('script', '', $untrusted_comment);
                            echo $alert;
                            echo $untrusted_comment;
                            
                        }
                    }
                } 

                # CSP 적용
                # default-src 'self'; script-src *.bootstrapcdn.com 'nonce-{랜덤값}'; style-src-elem *.bootstrapcdn.com;
                # 랜덤값은 base64로 인코딩된 20바이트 길이의 랜덤 바이트
                $nonce = base64_encode(random_bytes(20));
                $csp_header = "Content-Security-Policy: default-src 'self'; script-src *.bootstrapcdn.com 'nonce-" . $nonce . "'; style-src-elem *.bootstrapcdn.com;";
                header($csp_header);
        ?>
        </div>
        <form>
            <div class="form-group">
                <label for="commentContent">Comment</label>
                <textarea class="form-control" name="comment" id="comment" rows="3"
                    placeholder="Enter your comment"></textarea>
            </div>
            <button type="submit" class="btn btn-outline-primary">Submit</button>
        </form>
    </div>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</body>

</html>
