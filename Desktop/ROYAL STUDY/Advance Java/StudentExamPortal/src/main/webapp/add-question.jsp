<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
    com.model.User user = (com.model.User) session.getAttribute("user");
    if (user == null || !"admin".equals(user.getRole())) {
        response.sendRedirect("login.jsp");
        return;
    }
%>
<!DOCTYPE html>
<html>
<head>
    <title>Add Question - Admin</title>
    <style>
        body {
            font-family: Arial;
            background: #f9f9f9;
            padding: 40px;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px #ccc;
        }
        input[type="text"], select {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
        }
        button {
            padding: 10px 20px;
            background: #2c3e50;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Add New Question</h2>
        <form action="addQuestion" method="post">
            <input type="text" name="questionText" placeholder="Enter question" required>
            <input type="text" name="optionA" placeholder="Option A" required>
            <input type="text" name="optionB" placeholder="Option B" required>
            <input type="text" name="optionC" placeholder="Option C" required>
            <input type="text" name="optionD" placeholder="Option D" required>
            <select name="correctOption" required>
                <option value="">-- Correct Option --</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>
            </select>
            <button type="submit">Add Question</button>
        </form>
    </div>
</body>
</html>
