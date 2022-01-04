// @ts-ignore
// import fetch from "node-fetch"

const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'

function buildElement(product: any) {
    const myproduct = document.createElement("div")
    myproduct.classList.add("product")
    myproduct.innerHTML = `
<div class="product-img"><img src="${product?.image_link}"></div>
<div class="product-name">${product?.name}($${product?.price})</div>
<div class="product-description">${product?.description}</div>`
    return myproduct
}

function displayProduct(product: HTMLDivElement) {
    document.getElementById("root")!.append(product)
}

fetch(API_URL)
    .then((res: Response) => res.json())
    .then((products: any) => {
        console.log(products)
        products.map(buildElement).forEach(displayProduct)
    })
