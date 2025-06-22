<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Error Occurred</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ffe6e6;
            margin: 50px;
            text-align: center;
        }
        .error-container {
            background-color: #fff0f0;
            padding: 30px;
            border-radius: 8px;
            border: 2px solid #ff4c4c;
            display: inline-block;
        }
        h1 {
            color: #cc0000;
        }
        p {
            font-size: 18px;
        }
        a {
            text-decoration: none;
            color: #cc0000;
            font-weight: bold;
            margin-top: 20px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="error-container">
        <h1>Oops! Something Went Wrong.</h1>
        <p>Please try again later or contact support.</p>
        <a href="login.jsp">Back to Login</a>
    </div>
</body>
</html>
