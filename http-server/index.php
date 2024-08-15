<?php
// Define the correct credentials
$correct_username = 'nsa_admin';
$correct_password = 'secret_nsa_password';
$file_path = 'answer.exe'; // Replace with the correct path to answer.exe

// Check if both 'username' and 'password' parameters are set
if (isset($_GET['username']) && isset($_GET['password'])) {
    $username = $_GET['username'];
    $password = $_GET['password'];

    // Verify the username and password
    if (($username === $correct_username) && $password === $correct_password) {
        if (file_exists($file_path)) {
            // Set headers to force download
            header('Content-Description: File Transfer');
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename=' . basename($file_path));
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($file_path));
            flush(); // Flush system output buffer
            readfile($file_path);
            exit;
        } else {
            http_response_code(404);
            $response = array('message' => 'File not found!');
        }
    } else {
        http_response_code(401);
        $response = array('message' => 'Unauthorized access!');
    }
} else {
    http_response_code(400);
    $response = array('message' => 'username and/or password parameter is missing!');
}

// Set the content type to JSON
header('Content-Type: application/json');
echo json_encode($response);
?>
