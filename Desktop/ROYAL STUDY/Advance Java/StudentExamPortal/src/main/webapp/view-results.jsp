<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.List" %>
<%@ page import="com.model.Result" %>
<%@ page import="java.text.SimpleDateFormat" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Exam Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f1f1f1;
            padding: 20px;
        }
        h2 {
            color: #333;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: #fff;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: center;
        }
        th {
            background-color: #007BFF;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .back-btn {
            margin-top: 20px;
        }
        .back-btn a {
            text-decoration: none;
            padding: 10px 20px;
            background: #007BFF;
            color: white;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h2>All Exam Results</h2>

    <%
        List<Result> results = (List<Result>) request.getAttribute("results");
        if (results != null && !results.isEmpty()) {
    %>
        <table>
            <tr>
                <th>ID</th>
                <th>Student ID</th>
                <th>Total Questions</th>
                <th>Correct Answers</th>
                <th>Score</th>
                <th>Duration (minutes)</th>
                <th>Exam Date</th>
            </tr>
            <%
                for (Result result : results) {
            %>
            <tr>
                <td><%= result.getId() %></td>
                <td><%= result.getStudentId() %></td>
                <td><%= result.getTotalQuestions() %></td>
                <td><%= result.getCorrectAnswers() %></td>
                <td><%= result.getScore() %></td>
                <td><%= result.getDurationMinutes() %></td>
                <td><%= new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(result.getExamDate()) %></td>
            </tr>
            <% } %>
        </table>
    <% 
        } else { 
    %>
        <p>No results available yet.</p>
    <% } %>

    <div class="back-btn">
        <a href="admin.jsp">← Back to Dashboard</a>
    </div>
</body>
</html>
