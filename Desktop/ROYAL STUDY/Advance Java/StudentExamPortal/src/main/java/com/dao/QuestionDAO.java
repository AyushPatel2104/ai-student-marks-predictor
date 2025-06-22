package com.dao;

import com.model.Question;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class QuestionDAO {

    // Get all questions
    public static List<Question> getAllQuestions(Connection conn) throws SQLException {
        List<Question> questions = new ArrayList<>();
        String sql = "SELECT * FROM questions";
        try (PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            while (rs.next()) {
                Question q = new Question();
                q.setId(rs.getInt("id"));
                q.setQuestionText(rs.getString("question_text"));
                q.setOptionA(rs.getString("option_a"));
                q.setOptionB(rs.getString("option_b"));
                q.setOptionC(rs.getString("option_c"));
                q.setOptionD(rs.getString("option_d"));
                q.setCorrectOption(rs.getString("correct_option"));
                questions.add(q);
            }
        }
        return questions;
    }

    // Add a new question
    public static boolean addQuestion(Connection conn, Question question) throws SQLException {
        String sql = "INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_option) VALUES (?, ?, ?, ?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, question.getQuestionText());
            stmt.setString(2, question.getOptionA());
            stmt.setString(3, question.getOptionB());
            stmt.setString(4, question.getOptionC());
            stmt.setString(5, question.getOptionD());
            stmt.setString(6, question.getCorrectOption());

            int rowsInserted = stmt.executeUpdate();
            return rowsInserted > 0;
        }
    }
}
