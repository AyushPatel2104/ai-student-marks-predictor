package com.servlet;

import com.dao.UserDAO;
import com.model.User;
import com.util.DBUtil;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.Connection;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        try (Connection conn = DBUtil.getConnection()) {
            UserDAO userDAO = new UserDAO();
            User user = userDAO.validateUser(conn, username, password);

            if (user != null) {
                HttpSession session = request.getSession();
                session.setAttribute("user", user);
                if ("admin".equals(user.getRole())) {
                    response.sendRedirect("admin.jsp");
                } else {
                    response.sendRedirect("welcome.jsp");
                }
            } else {
                request.setAttribute("error", "Invalid username or password.");
                request.getRequestDispatcher("login.jsp").forward(request, response);
            }
        } catch (Exception e) {
            e.printStackTrace();
            request.setAttribute("error", "Login error occurred.");
            request.getRequestDispatcher("login.jsp").forward(request, response);
        }
    }
}
