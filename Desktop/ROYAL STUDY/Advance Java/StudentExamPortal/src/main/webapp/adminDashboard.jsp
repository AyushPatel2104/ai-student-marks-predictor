<%@ page import="java.sql.*, com.util.DBUtil" %>
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

    int userCount = 0;
    int questionCount = 0;
    int resultCount = 0;

    try (Connection conn = DBUtil.getConnection()) {
        Statement stmt = conn.createStatement();

        ResultSet rs1 = stmt.executeQuery("SELECT COUNT(*) FROM users");
        if (rs1.next()) userCount = rs1.getInt(1);

        ResultSet rs2 = stmt.executeQuery("SELECT COUNT(*) FROM questions");
        if (rs2.next()) questionCount = rs2.getInt(1);

        ResultSet rs3 = stmt.executeQuery("SELECT COUNT(*) FROM results");
        if (rs3.next()) resultCount = rs3.getInt(1);

    } catch (Exception e) {
        e.printStackTrace();
    }
%>

<!DOCTYPE html>
<html>
<head>
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <style>
        body {
            display: flex;
        }

        .sidebar {
            width: 220px;
            background-color: #343a40;
            color: white;
            padding: 20px;
            min-height: 100vh;
        }

        .sidebar a {
            color: white;
            display: block;
            padding: 10px;
            text-decoration: none;
        }

        .sidebar a:hover {
            background-color: #495057;
        }

        .content {
            flex-grow: 1;
            padding: 40px;
            background-color: #f8f9fa;
        }

        .card {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<div class="sidebar">
    <h4>Admin Panel</h4>
    <p><strong><%= user.getUsername() %></strong></p>
    <a href="dashboard.jsp">Dashboard</a>
    <a href="admin.jsp">Add Questions</a>
    <a href="view-results.jsp">View Results</a>
    <a href="logout">Logout</a>
</div>

<div class="content">
    <h2>Welcome to the Admin Dashboard</h2>
    <div class="row mt-4">
        <div class="col-md-4">
            <div class="card text-white bg-primary">
                <div class="card-body">
                    <h5 class="card-title">Total Users</h5>
                    <p class="card-text"><%= userCount %></p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-success">
                <div class="card-body">
                    <h5 class="card-title">Total Questions</h5>
                    <p class="card-text"><%= questionCount %></p>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card text-white bg-danger">
                <div class="card-body">
                    <h5 class="card-title">Total Results</h5>
                    <p class="card-text"><%= resultCount %></p>
                </div>
            </div>
        </div>
    </div>
</div>

</body>
</html>
