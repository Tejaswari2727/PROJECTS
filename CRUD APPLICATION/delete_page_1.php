<?php include('dbcon.php'); ?> 

<?php
if (isset($_GET['id'])) {
    $id = $_GET['id'];

    // Check if the ID is a valid integer
    if (!filter_var($id, FILTER_VALIDATE_INT)) {
        die("Invalid ID provided.");
    }

    // Update the SQL query to use backticks or no quotes for table and column names
    $query = "DELETE FROM students WHERE id = '$id'";
    $result = mysqli_query($connection, $query);

    if (!$result) {
        die("Query Failed: " . mysqli_error($connection));
    } else {
        header('Location: index.php?delete_msg=You have deleted successfully.');
        exit(); // Always call exit after a header redirect
    }
} else {
    die("No ID provided.");
}
?>
