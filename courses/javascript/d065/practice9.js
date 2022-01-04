"use strict";
// @ts-ignore
// import fetch from "node-fetch"
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline';
const products = [];
let filtered = [];
const root = document.getElementById("root");
const priceBtn = document.getElementById("price-btn");
const searchInput = document.getElementById("search-input");
function buildElements(product) {
    const myproduct = document.createElement("div");
    myproduct.classList.add("product");
    myproduct.innerHTML = `
<div class="product-img"><img src="${product === null || product === void 0 ? void 0 : product.image_link}"></div>
<div class="product-name">${product === null || product === void 0 ? void 0 : product.name}($${product === null || product === void 0 ? void 0 : product.price})</div>
<div class="product-description">${product === null || product === void 0 ? void 0 : product.description}</div>`;
    products.push({ value: myproduct, name: product.name, price: product.price });
    return myproduct;
}
function replaceElement(product) {
    root.innerHTML = "";
    product.forEach((v) => root.append(v.value));
}
fetch(API_URL)
    .then((res) => res.json())
    .then((data) => {
    data.map(buildElements).forEach((v) => root.append(v));
    filtered = products;
});
let sign = 1;
priceBtn.addEventListener("click", () => {
    replaceElement(filtered.sort((a, b) => sign * (a.price - b.price)));
    sign *= -1;
});
searchInput.addEventListener("input", () => {
    const reg = new RegExp(searchInput.value, "i");
    filtered = products.filter((v) => v.name.match(reg));
    replaceElement(filtered);
    sign = 1;
});
