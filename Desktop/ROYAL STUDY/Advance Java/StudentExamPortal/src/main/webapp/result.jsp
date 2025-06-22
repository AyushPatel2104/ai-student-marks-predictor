<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Result</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
    <h2>Exam Result</h2>
    <p>Total Questions: <%= request.getAttribute("total") %></p>
    <p>Correct Answers: <%= request.getAttribute("correct") %></p>
    <p>Score: <%= request.getAttribute("score") %>%</p>
    <a href="logout">Logout</a>
</div>
</body>
</html>
