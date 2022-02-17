<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Login</title>
</head>
<body>
<jsp:include page="menu.jsp"/>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">login</h1>
    </div>
</div>
<div class="container" align="center">
    <div class="col-md-4 col-md-offset-4">
        <h3 class="form-signin-heading">Please sign in</h3>
        <%
            String error = request.getParameter("error");
            if(error != null){
                out.println("<div class='alert alert-danger'>");
                out.println("Wrong id or password!");
                out.println("</div>");
            }
        %>
        <form class="form-signin" action="j_security_check" method="post">
            <div class="form-group">
                <label for="inputUserName" class="sr-only">User Name</label>
                <input type="text" class="form-control" placeholder="ID" name="j_username" required autofocus>
            </div>
            <div class="form-group">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" class="form-control" placeholder="Password" name="j_password" required>
            </div>
            <button class="btn btn btn-lg btn-success btn-block" type="submit">login</button>
        </form>
    </div>
</div>

</body>
</html>
