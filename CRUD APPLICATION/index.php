<?php 
session_start(); // Start the session for message handling
include('header.php'); 
include('dbcon.php'); 
?>

<!-- Wrap h2 and button in a box1 div -->
<div class="box1">
    <h2>ALL STUDENTS</h2>
    <button class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">ADD STUDENTS</button>
</div>

<table class="table table-hover table-bordered table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Age</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
    </thead>
    <tbody>
        <?php
            $query = "SELECT * FROM students";
            $result = mysqli_query($connection, $query);
            
            if (!$result) {
                die("Query Failed: " . mysqli_error($connection));
            } else {
                while ($row = mysqli_fetch_assoc($result)) {
        ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row['id']); ?></td>
                        <td><?php echo htmlspecialchars($row['first_name']); ?></td>
                        <td><?php echo htmlspecialchars($row['last_name']); ?></td>
                        <td><?php echo htmlspecialchars($row['age']); ?></td>
                        <td><a href="update_page_1.php?id=<?php echo urlencode($row['id']); ?>" class="btn btn-success">Update</a></td>
                        <td><a href="delete_page_1.php?id=<?php echo urlencode($row['id']); ?>" class="btn btn-danger">Delete</a></td>
                    </tr>
        <?php
                }
            }
        ?>
    </tbody>
</table>

<?php
// Display session messages for insert and other actions
if (isset($_SESSION['message'])) {
    echo "<h6>" . htmlspecialchars($_SESSION['message']) . "</h6>";
    unset($_SESSION['message']); // Clear message after displaying it
}

if (isset($_SESSION['insert_msg'])) {
    echo "<h6>" . htmlspecialchars($_SESSION['insert_msg']) . "</h6>"; 
    unset($_SESSION['insert_msg']); // Clear message after displaying it
}
?>

<form action="insert_data.php" method="post">
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">ADD STUDENTS</h5>
        <button type="button" class="close ml-auto" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">


           <div class="form-group">
            <label for="f_name">First Name</label>
            <input type="text" id="f_name" name="f_name" class="form-control" required>
           </div>
           <div class="form-group">
            <label for="l_name">Last Name</label>
            <input type="text" id="l_name" name="l_name" class="form-control" required>
           </div>
           <div class="form-group">
            <label for="age">Age</label>
            <input type="number" id="age" name="age" class="form-control" required>
           </div>
           
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <input type="submit" class="btn btn-success" name="add_students" value="ADD">
      </div>
    </div>
  </div>
</div>
</form>

<?php include('footer.php'); ?>
