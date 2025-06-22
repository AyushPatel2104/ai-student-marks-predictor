<%@ page import="java.util.*, com.model.Question" %>
<%@ page session="true" %>
<%
    HttpSession sessionObj = request.getSession(false);
    if (sessionObj == null || sessionObj.getAttribute("user") == null) {
        response.sendRedirect("login.jsp");
        return;
    }

    List<Question> questions = (List<Question>) request.getAttribute("questions");
    if (questions == null) {
        out.println("<h3>No questions available!</h3>");
        return;
    }

    com.model.User currentUser = (com.model.User) sessionObj.getAttribute("user");
%>

<html>
<head>
    <title>Online Exam</title>
    <style>
        body {
            font-family: Arial;
            margin: 20px;
        }
        .question-box {
            background: #f0f0f0;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
        }
        h2 { color: #2c3e50; }
    </style>
</head>
<body>

<h2>Online Exam</h2>
<form method="post" action="exam">
    <input type="hidden" name="totalQuestions" value="<%= questions.size() %>" />
    <input type="hidden" name="studentId" value="<%= currentUser.getId() %>" />

    <%
        int i = 1;
        for (Question q : questions) {
    %>
        <div class="question-box">
            <p><strong>Q<%= i %>:</strong> <%= q.getQuestionText() %></p>
            <input type="radio" name="q<%= i %>" value="A" required> <%= q.getOptionA() %><br>
            <input type="radio" name="q<%= i %>" value="B"> <%= q.getOptionB() %><br>
            <input type="radio" name="q<%= i %>" value="C"> <%= q.getOptionC() %><br>
            <input type="radio" name="q<%= i %>" value="D"> <%= q.getOptionD() %><br>
            <input type="hidden" name="correct<%= i %>" value="<%= q.getCorrectOption() %>" />
        </div>
    <%
            i++;
        }
    %>

    <input type="submit" value="Submit Exam">
</form>
</body>
</html>
