
<?php
// Start the session
session_start();

// Include the database connection file
include('dbcon.php'); // Make sure this file contains the connection initialization

if (isset($_POST['add_students'])) {

    $fname = $_POST['f_name'];
    $lname = $_POST['l_name'];
    $age = $_POST['age'];

    // Check if first name is empty
    if (empty($fname)) {
        header('location:index.php?message=You need to fill in the first name!');
        exit; // Stop further execution after redirect
    }
    
    // Insert into the database
    $query = "INSERT INTO students (first_name, last_name, age) VALUES ('$fname', '$lname', '$age')";
    
    // Make sure to pass the database connection variable here
    $result = mysqli_query($connection, $query);
    
    if (!$result) {
        die("Query Failed: " . mysqli_error($connection));
    } else {
        // Store the success message in a session variable
        $_SESSION['insert_msg'] = "Your Data has been added Successfully";
        header('location:index.php');
        exit; // Stop further execution after redirect
    }
}
?>

