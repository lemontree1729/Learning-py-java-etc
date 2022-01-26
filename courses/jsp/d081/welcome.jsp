<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%--    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">--%>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Welcome</title>
</head>
<body>
<nav class="navbar navbar-expand navbar-dark bg-dark">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="welcome.jsp">Home</a>
        </div>
    </div>
</nav>
<%! String greeting = "Welcome to Web Shopping Mall";
    String tagline = "Welcome to Web Market!";%>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">
            <%= greeting%>
        </h1>
    </div>
</div>
<main role="main">
    <div class="container">
        <div class="text-center">
            <h3>
                <%=tagline%>
            </h3>
            <%
                out.print(new java.util.Date());
            %>
        </div>
    </div>
</main>
<footer class="container">
    <p>&copy; WebMarket</p>
</footer>


</body>
</html>
