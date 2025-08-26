<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Happy Trashy</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background-color: white;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;   /* center horizontally */
      align-items: center;       /* center vertically */
      height: 100vh;             /* full screen height */
      position: relative;
    }

    .logo {
      max-width: 300px; /* adjust this size if you want bigger/smaller */
      height: auto;
    }

    .email {
      position: absolute;
      top: 20px;
      right: 30px;
      font-size: 18px;
      color: #333;
    }

    .email a {
      color: #333;
      text-decoration: none;
    }

    .email a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <!-- Right corner email text -->
  <div class="email">
    Email: <a href="mailto:forest@happytrashy.com">forest@happytrashy.com</a>
  </div>

  <!-- Centered logo -->
  <img src="logo.png" alt="Happy Trashy Logo" class="logo">
</body>
</html>