<%@ page import="com.model.Question, java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page session="true" %>
<%
    HttpSession currentSession = request.getSession(false);
    if (currentSession == null || currentSession.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");
        return;
    }

    com.model.User user = (com.model.User) currentSession.getAttribute("user");
    if (!"admin".equals(user.getRole())) {
        response.sendRedirect("login.jsp");
        return;
    }

    List<Question> questions = (List<Question>) request.getAttribute("questions");
%>

<!DOCTYPE html>
<html>
<head>
    <title>Admin Panel - Online Exam Portal</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <style>
        body {
            display: flex;
            min-height: 100vh;
        }

        .sidebar {
            width: 220px;
            background-color: #343a40;
            color: white;
            padding: 20px;
            flex-shrink: 0;
        }

        .sidebar h4 {
            margin-bottom: 20px;
        }

        .sidebar a {
            display: block;
            color: white;
            padding: 10px 0;
            text-decoration: none;
        }

        .sidebar a:hover {
            background-color: #495057;
        }

        .content {
            flex: 1;
            padding: 30px;
            background-color: #f8f9fa;
        }

        table {
            margin-top: 30px;
        }

        .alert {
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="sidebar">
    <h4>Admin Panel</h4>
    <p><strong>User:</strong> <%= user.getUsername() %></p>
    <a href="dashboard.jsp">Dashboard</a>
    <a href="logout">Logout</a>
</div>

<div class="content">
    <h2>Add New Question</h2>

    <% if (request.getAttribute("message") != null) { %>
        <div class="alert alert-success"><%= request.getAttribute("message") %></div>
    <% } else if (request.getAttribute("error") != null) { %>
        <div class="alert alert-danger"><%= request.getAttribute("error") %></div>
    <% } %>

    <form action="add-question" method="post" class="row g-3">
        <div class="col-md-12">
            <label class="form-label">Question Text</label>
            <textarea name="questionText" class="form-control" required></textarea>
        </div>
        <div class="col-md-6">
            <label class="form-label">Option A</label>
            <input type="text" name="optionA" class="form-control" required>
        </div>
        <div class="col-md-6">
            <label class="form-label">Option B</label>
            <input type="text" name="optionB" class="form-control" required>
        </div>
        <div class="col-md-6">
            <label class="form-label">Option C</label>
            <input type="text" name="optionC" class="form-control" required>
        </div>
        <div class="col-md-6">
            <label class="form-label">Option D</label>
            <input type="text" name="optionD" class="form-control" required>
        </div>
        <div class="col-md-3">
            <label class="form-label">Correct Option (A/B/C/D)</label>
            <input type="text" name="correctOption" class="form-control" maxlength="1" required>
        </div>
        <div class="col-12">
            <button type="submit" class="btn btn-primary">Add Question</button>
        </div>
    </form>

    <%
        if (questions != null && !questions.isEmpty()) {
    %>
    <h3 class="mt-5">All Questions</h3>
    <table class="table table-striped table-bordered">
        <thead>
        <tr>
            <th>ID</th>
            <th>Question</th>
            <th>A</th>
            <th>B</th>
            <th>C</th>
            <th>D</th>
            <th>Correct</th>
        </tr>
        </thead>
        <tbody>
        <%
            for (Question q : questions) {
        %>
        <tr>
            <td><%= q.getId() %></td>
            <td><%= q.getQuestionText() %></td>
            <td><%= q.getOptionA() %></td>
            <td><%= q.getOptionB() %></td>
            <td><%= q.getOptionC() %></td>
            <td><%= q.getOptionD() %></td>
            <td><strong><%= q.getCorrectOption() %></strong></td>
        </tr>
        <%
            }
        %>
        </tbody>
    </table>
    <% } else { %>
    <p class="mt-4 text-muted">No questions available.</p>
    <% } %>
</div>

</body>
</html>
