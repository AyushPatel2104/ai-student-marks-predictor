package com.servlet;

import com.dao.ResultDAO;
import com.model.Result;
import com.util.DBUtil;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.Connection;
import java.util.List;

public class ViewResultsServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {

        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        try (Connection conn = DBUtil.getConnection()) {
            List<Result> results = ResultDAO.getAllResults(conn);
            request.setAttribute("results", results);
            RequestDispatcher dispatcher = request.getRequestDispatcher("view-results.jsp");
            dispatcher.forward(request, response);
        } catch (Exception e) {
            e.printStackTrace();
            response.sendRedirect("error.jsp");
        }
    }
}
