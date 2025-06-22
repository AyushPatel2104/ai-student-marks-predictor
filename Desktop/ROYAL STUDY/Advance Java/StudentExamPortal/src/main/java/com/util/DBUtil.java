// DBUtil.java
package com.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBUtil {

    private static final String URL = "jdbc:mysql://localhost:3306/exam_portal";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "1234"; // 🔁 Replace with your actual MySQL password

    public static Connection getConnection() throws ClassNotFoundException, SQLException {
        // Load the JDBC driver (Connector/J 8+)
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Establish and return the connection
        return DriverManager.getConnection(URL, USERNAME, PASSWORD);
    }
}
