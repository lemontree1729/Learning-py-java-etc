<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="dto.Product" %>
<%@ page import="dao.ProductRepository" %>
<%--<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>--%>
<jsp:useBean id="productDAO" class="dao.ProductRepository" scope="session"/>
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Product list</title>
</head>
<body>
<jsp:include page="menu.jsp"/>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">Product list</h1>
    </div>
</div>
<%
    ProductRepository dao = ProductRepository.getInstance();
    ArrayList<Product> listOfProducts = dao.getAllProducts();
%>
<div class="container">
    <div class="row" align="center">
        <%
            for (int i = 0; i < listOfProducts.size(); i++) {
                Product product = listOfProducts.get(i);
        %>
        <div class="col-md-4">
            <img src="c:/upload/<%=product.getFilename()%>" style="width:100%"/>
            <h3><%=product.getPname()%>
            </h3>
            <p><%=product.getDescription()%>
            </p>
            <p><%=product.getUnitPrice()%>원</p>
            <p><a href="product.jsp?id=<%=product.getProductId()%>" class="btn btn-secondary" role="button"> 상세 정보
                &raquo;</a></p>
        </div>
        <%
            }
        %>
    </div>
</div>
<jsp:include page="footer.jsp"/>
</body>
</html>
