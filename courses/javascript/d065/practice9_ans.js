const rootDiv = document.getElementById('root')
const priceBtn = document.getElementById('price-btn')
const searchInput = document.getElementById('search-input')
const API_URL = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'

let shouldSort = false
let shouldFilter = false
let originalProducts = null
let keyword = ''

function buildElement(product) {
    const item = document.createElement('div')
    item.className = 'product'
    item.innerHTML = `
                      <div class='product-img'><img src=${product.image_link} alt=${product.name}/></div>
                      <div class='product-name'>${product.name} ($${product.price})</div>
                      <div class='product-description'>${product.description}</div>
                      <div class='product-type'>${product.product_type}</div>
                  `
    return item
}

function displayProducts(products) {
    rootDiv.innerHTML = ''
    products.forEach(product => rootDiv.appendChild(buildElement(product)))
}

function updateProducts(products, keyword) {
    let newProducts = [...products]
    if (shouldFilter)
        newProducts = newProducts.filter(product => product.product_type.toLowerCase().includes(keyword.toLowerCase()))
    if (shouldSort)
        newProducts.sort((p1, p2) => parseFloat(p1.price) - parseFloat(p2.price))
    return newProducts
}

function searchProducts(e) {
    keyword = e.target.value
    shouldFilter = keyword !== ''
    console.log(shouldFilter)
    const newProducts = updateProducts(originalProducts, keyword)
    displayProducts(newProducts)
}

function sortByPrice(e) {
    shouldSort = !shouldSort
    console.log(shouldSort)
    const newProducts = updateProducts(originalProducts, keyword)
    displayProducts(newProducts)
}

fetch(API_URL)
    .then(function (res) {
        return res.json()
    })
    .then(function (products) {
        originalProducts = products
        displayProducts(products)
        priceBtn.addEventListener('click', sortByPrice)
        searchInput.addEventListener('input', searchProducts)
    })