<%--directive element--%>
<%--page directive--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%--taglib directive--%>
<html>
<head>
    <title>practice</title>
</head>
<body>
<%--declaration tag--%>
<%--placed in scripting_jsp class(run only once built)--%>
<%! int global = 0;%>
<%--scriptlet tag--%>
<%--placed in _jspService class(run every request(ex. refreshing page)--%>
<% int local = 0;%>
<% global++;%>
<% local++;%>
<%out.println(global);%>
<%--expression tag--%>
<%--placed at out.print function of _jspService class--%>
<%="global: " + global%>
<%="local: " + local%>

</body>
</html>
