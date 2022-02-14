<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.Arrays" %>
<%@ page import="java.lang.reflect.Array" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>    <%--    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">--%>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Add product</title>
</head>
<body>
<jsp:include page="menu.jsp"/>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">Add product</h1>
    </div>
</div>
<div class="container">
    <form name="newProduct" action="processAddProduct.jsp" class="form-horizontal" method="post">
        <div class="form-group row">
            <label class="col-sm-2">Product id</label>
            <div class="col-sm-3">
                <input type="text" name="productId" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Name</label>
            <div class="col-sm-3">
                <input type="text" name="name" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Price</label>
            <div class="col-sm-3">
                <input type="text" name="unitPrice" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Description</label>
            <div class="col-sm-5">
                <textarea name="description" cols="50" rows="2" class="form-control"></textarea>
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Manufacturer</label>
            <div class="col-sm-3">
                <input type="text" name="manufacturer" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Category</label>
            <div class="col-sm-3">
                <input type="text" name="category" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Units in stock</label>
            <div class="col-sm-3">
                <input type="text" name="unitsInStock" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2">Condition</label>
            <div class="col-sm-5">
                <input type="radio" name="condition" value="New">New product
                <input type="radio" name="condition" value="Old">Old product
                <input type="radio" name="condition" value="Refurbished">Refurbished product
            </div>
        </div>
        <div class="form-group row">
            <label class="col-sm-2"></label>
            <div class="col-sm-offset-2 col-sm-10">
                <input type="submit" class="btn btn-primary" value="submit">
            </div>
        </div>
    </form>
</div>
</body>
</html>