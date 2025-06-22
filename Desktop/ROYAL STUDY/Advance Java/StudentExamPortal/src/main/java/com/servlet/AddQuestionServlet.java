package com.servlet;

import com.dao.QuestionDAO;
import com.model.Question;
import com.util.DBUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.Connection;

@WebServlet("/add-question")
public class AddQuestionServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String questionText = request.getParameter("questionText");
        String optionA = request.getParameter("optionA");
        String optionB = request.getParameter("optionB");
        String optionC = request.getParameter("optionC");
        String optionD = request.getParameter("optionD");
        String correctOption = request.getParameter("correctOption").toUpperCase();

        Question question = new Question();
        question.setQuestionText(questionText);
        question.setOptionA(optionA);
        question.setOptionB(optionB);
        question.setOptionC(optionC);
        question.setOptionD(optionD);
        question.setCorrectOption(correctOption);

        try (Connection conn = DBUtil.getConnection()) {
            boolean success = QuestionDAO.addQuestion(conn, question);
            if (success) {
                request.setAttribute("message", "Question added successfully!");
            } else {
                request.setAttribute("error", "Failed to add question. Try again.");
            }
            request.getRequestDispatcher("admin.jsp").forward(request, response);
        } catch (Exception e) {
            e.printStackTrace();
            request.setAttribute("error", "Database error occurred.");
            request.getRequestDispatcher("admin.jsp").forward(request, response);
        }
    }
}
