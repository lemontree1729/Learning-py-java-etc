<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="dto.Product" %>
<%@ page import="dao.ProductRepository" %>
<jsp:useBean id="productDAO" class="dao.ProductRepository" scope="session"/>
<html>
<head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Product detail</title>
</head>
<body>
<jsp:include page="menu.jsp"/>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">Product info</h1>
    </div>
</div>
<%
    String id = request.getParameter("id");
    ProductRepository dao = ProductRepository.getInstance();
    Product product = dao.getProductById(id);
%>
<div class="container">
    <div class="row">
        <div class="col-md-5">
            <img src="c:/upload/<%=product.getFilename()%>" style="width:100%"/>
        </div>
        <div class="col-md-6">
            <h3><%=product.getPname()%>
            </h3>
            <p><%=product.getDescription()%>
            </p>
            <p><b>product id : </b><span class="badge badge-danger">
                <%=product.getProductId()%></span></p>
            <p><b>manufacturer</b> : <%=product.getManufacturer()%>
            </p>
            <p><b>category</b> : <%=product.getCategory()%>
            </p>
            <p><b>units in stock</b> : <%=product.getUnitsInStock()%>
            </p>
            <h4><%=product.getUnitPrice()%>원
            </h4>
            <p><a href="#" class="btn btn-info"> 상품 주문 &raquo;</a>
                <a href="products.jsp" class="btn btn-secondary"> 상품 목록 &raquo;</a></p>
        </div>
    </div>
</div>
<jsp:include page="footer.jsp"/>
</body>
</html>
