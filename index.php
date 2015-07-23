<?php
// Start output buffering
ob_start();

// Start session
session_start();
?>
<!DOCTYPE html>
<html>
  <head>
    <title>Sample file</title>
  </head>
  <body>
    <h1>Sample file</h1>
  </body>
</html
<?php
// End output buffering and flush
ob_end_flush();
?>