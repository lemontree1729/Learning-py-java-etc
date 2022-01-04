"use strict";
// @ts-ignore
// import fetch from "node-fetch"
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline';
function buildElement(product) {
    const myproduct = document.createElement("div");
    myproduct.classList.add("product");
    myproduct.innerHTML = `
<div class="product-img"><img src="${product === null || product === void 0 ? void 0 : product.image_link}"></div>
<div class="product-name">${product === null || product === void 0 ? void 0 : product.name}($${product === null || product === void 0 ? void 0 : product.price})</div>
<div class="product-description">${product === null || product === void 0 ? void 0 : product.description}</div>`;
    return myproduct;
}
function displayProduct(product) {
    document.getElementById("root").append(product);
}
fetch(API_URL)
    .then((res) => res.json())
    .then((products) => {
    console.log(products);
    products.map(buildElement).forEach(displayProduct);
});
