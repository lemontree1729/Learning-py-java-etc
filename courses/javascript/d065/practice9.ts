// @ts-ignore
// import fetch from "node-fetch"
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
const products: any = []
let filtered: any = []
const root = document.getElementById("root")!
const priceBtn = document.getElementById("price-btn")!
const searchInput = <HTMLInputElement>document.getElementById("search-input")!

type Product = {
    value: any
    name: string
    price: number
}

function buildElements(product: any) {
    const myproduct = document.createElement("div")
    myproduct.classList.add("product")
    myproduct.innerHTML = `
<div class="product-img"><img src="${product?.image_link}"></div>
<div class="product-name">${product?.name}($${product?.price})</div>
<div class="product-description">${product?.description}</div>`
    products.push({value: myproduct, name: product.name, price: product.price})
    return myproduct
}

function replaceElement(product: Array<Product>) {
    root.innerHTML = ""
    product.forEach((v: Product) => root.append(v.value))
}

fetch(API_URL)
    .then((res: Response) => res.json())
    .then((data: any) => {
        data.map(buildElements).forEach((v: HTMLDivElement) => root.append(v))
        filtered = products
    })

let sign = 1
priceBtn.addEventListener("click", () => {
    replaceElement(filtered.sort((a: Product, b: Product) => sign * (a.price - b.price)))
    sign *= -1
})

searchInput.addEventListener("input", () => {
    const reg = new RegExp(searchInput.value, "i")
    filtered = products.filter((v: Product) => v.name.match(reg))
    replaceElement(filtered)
    sign = 1
})