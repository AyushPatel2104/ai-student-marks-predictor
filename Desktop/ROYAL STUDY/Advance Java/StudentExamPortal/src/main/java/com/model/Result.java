package com.model;

import java.sql.Timestamp;

public class Result {
    private int id;
    private int studentId;
    private int totalQuestions;
    private int correctAnswers;
    private double score;
    private int durationMinutes;
    private Timestamp examDate;

    // Getters and setters
    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }

    public int getStudentId() {
        return studentId;
    }
    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public int getTotalQuestions() {
        return totalQuestions;
    }
    public void setTotalQuestions(int totalQuestions) {
        this.totalQuestions = totalQuestions;
    }

    public int getCorrectAnswers() {
        return correctAnswers;
    }
    public void setCorrectAnswers(int correctAnswers) {
        this.correctAnswers = correctAnswers;
    }

    public double getScore() {
        return score;
    }
    public void setScore(double score) {
        this.score = score;
    }

    public int getDurationMinutes() {
        return durationMinutes;
    }
    public void setDurationMinutes(int durationMinutes) {
        this.durationMinutes = durationMinutes;
    }

    public Timestamp getExamDate() {
        return examDate;
    }
    public void setExamDate(Timestamp examDate) {
        this.examDate = examDate;
    }
}
