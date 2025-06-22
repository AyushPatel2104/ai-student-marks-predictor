package com.dao;

import com.model.Result;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class ResultDAO {
    public static void insertResult(Connection conn, int studentId, int totalQuestions, int correctAnswers, double score, int durationMinutes) throws SQLException {
        String sql = "INSERT INTO results (student_id, total_questions, correct_answers, score, duration_minutes) VALUES (?, ?, ?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, studentId);
            stmt.setInt(2, totalQuestions);
            stmt.setInt(3, correctAnswers);
            stmt.setDouble(4, score);
            stmt.setInt(5, durationMinutes);
            stmt.executeUpdate();
        }
    }

    public static List<Result> getAllResults(Connection conn) throws SQLException {
        List<Result> resultList = new ArrayList<>();
        String sql = "SELECT * FROM results ORDER BY exam_date DESC";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                Result r = new Result();
                r.setId(rs.getInt("id"));
                r.setStudentId(rs.getInt("student_id"));
                r.setTotalQuestions(rs.getInt("total_questions"));
                r.setCorrectAnswers(rs.getInt("correct_answers"));
                r.setScore(rs.getDouble("score"));
                r.setDurationMinutes(rs.getInt("duration_minutes"));
                r.setExamDate(rs.getTimestamp("exam_date"));
                resultList.add(r);
            }
        }
        return resultList;
    }
}
