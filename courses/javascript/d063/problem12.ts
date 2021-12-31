import fetch from "node-fetch"

const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'

function buildElement(product) {
    const myproduct = document.createElement("div")
    myproduct.classList.add("product")
    myproduct.innerHTML = `
<div class="product-img"><img></div>
<div class="product-name"></div>
<div class="product-description"></div>`
    myproduct.querySelector<HTMLImageElement>(".product-img>img")!.src = product.image_link
    myproduct.querySelector<HTMLElement>(".product-name")!.innerHTML = `${product.name}($${product.price})`
    myproduct.querySelector<HTMLElement>(".product-description")!.innerHTML = product.description
    return myproduct
}

function displayProduct(product) {
    document.getElementById("root")!.append(product)
}

fetch(API_URL)
    .then(function (res) {
        console.log(res.json())
        return res.json()
    })
    .then(function (products) {
        console.log(products)
        const productsRefined = products.map(buildElement)
        productsRefined.forEach(displayProduct)
    })
