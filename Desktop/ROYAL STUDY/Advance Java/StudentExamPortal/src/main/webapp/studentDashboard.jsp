<%@ page session="true" %>
<%
    String role = (String) session.getAttribute("role");
    if (role == null || !role.equals("student")) {
        response.sendRedirect("login.jsp");
        return;
    }
%>

<!DOCTYPE html>
<html>
<head>
    <title>Student Dashboard</title>
</head>
<body>
    <h1>Welcome, Student!</h1>
    <p>Take exams and check your results here.</p>
    <a href="logout.jsp">Logout</a>
</body>
</html>
