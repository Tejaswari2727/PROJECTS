<?php include('header.php'); ?> 
<?php include('dbcon.php'); ?> 

<?php
if (isset($_GET['id'])) {
    $id = $_GET['id'];
    
    // Correcting the SQL query
    $query = "SELECT * FROM students WHERE id = '$id'";
    $result = mysqli_query($connection, $query);
    
    if (!$result) {
        die("Query Failed: " . mysqli_error($connection));
    } else {
        $row = mysqli_fetch_assoc($result);
        
        // Check if row is fetched successfully
        if (!$row) {
            // Handle the case where no data is found
            die("No student found with this ID.");
        }
    }
} else {
    die("No ID provided.");
}
?>

<?php
if (isset($_POST['update_students'])) {
    $fname = $_POST['f_name'];
    $lname = $_POST['l_name'];
    $age = $_POST['age'];

    // Corrected the SQL update query
    $query = "UPDATE students SET first_name = '$fname', last_name = '$lname', age = '$age' WHERE id = '$id'";
    
    $result = mysqli_query($connection, $query);
    
    if (!$result) {
        die("Query Failed: " . mysqli_error($connection));
    } else {
        header('location:index.php?update_msg=You have Successfully Updated the data.');
        exit; // Always good to exit after a redirect
    }
}
?>

<div class="container vh-100 d-flex justify-content-center align-items-start custom-padding">
    <form action="update_page_1.php?id=<?php echo $row['id']; ?>" method="post"> <!-- Added action and method -->
        <div class="form-group">
            <label for="f_name">First Name</label>
            <input type="text" id="f_name" name="f_name" class="form-control" value="<?php echo isset($row['first_name']) ? htmlspecialchars($row['first_name']) : ''; ?>" required>
        </div>
        <div class="form-group">
            <label for="l_name">Last Name</label>
            <input type="text" id="l_name" name="l_name" class="form-control" value="<?php echo isset($row['last_name']) ? htmlspecialchars($row['last_name']) : ''; ?>" required>
        </div>
        <div class="form-group">
            <label for="age">Age</label>
            <input type="number" id="age" name="age" class="form-control" value="<?php echo isset($row['age']) ? htmlspecialchars($row['age']) : ''; ?>" required>
        </div>
        <div class="form-group">
            <input type="submit" class="btn btn-primary" name="update_students" value="Update">
        </div>
    </form>
</div>

<?php include('footer.php'); ?>