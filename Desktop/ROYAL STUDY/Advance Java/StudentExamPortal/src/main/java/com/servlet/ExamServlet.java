package com.servlet;

import java.io.IOException;
import java.sql.Connection;
import java.util.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import com.dao.ResultDAO;
import com.model.Question;
import com.model.User;
import com.util.DBUtil;

@WebServlet("/submit-exam")
public class ExamServlet extends HttpServlet {
    private static final long serialVersionUID = 1L; // Serializable fix

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User user = (User) session.getAttribute("user");
        List<Question> questions = (List<Question>) session.getAttribute("questions");

        int correctAnswers = 0;
        for (int i = 0; i < questions.size(); i++) {
            String selected = request.getParameter("answer" + i);
            String correct = questions.get(i).getCorrectOption();
            if (selected != null && selected.equalsIgnoreCase(correct)) {
                correctAnswers++;
            }
        }

        int totalQuestions = questions.size();
        double score = ((double) correctAnswers / totalQuestions) * 100;
        int durationMinutes = 10; // static or calculate if timing logic is added

        try (Connection conn = DBUtil.getConnection()) {
            ResultDAO.insertResult(conn, user.getId(), totalQuestions, correctAnswers, score, durationMinutes);
        } catch (Exception e) {
            e.printStackTrace();
        }

        request.setAttribute("score", score);
        request.setAttribute("correct", correctAnswers);
        request.setAttribute("total", totalQuestions);
        request.getRequestDispatcher("result.jsp").forward(request, response);
    }
}
