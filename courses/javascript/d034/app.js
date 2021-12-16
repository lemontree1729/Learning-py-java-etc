// Create DOM(Document Object Model)
const input = document.createElement('input')
input.className = 'search-img'
input.type = 'text'
input.placeholder = "search word..."
// Show DOM at console
console.log("input", input)

const div = document.createElement('div')
div.className = 'container'
div.innerHTML = "<img src='' alt=''/> <p>You have happy family</p>"
console.log("div", div)

const img = document.createElement('img')
img.src = 'http://127.0.0.1:5500'
img.alt = 'javascript'
img.id = 'photo'
console.log("img", img)

// Mount
const root = document.getElementById('root') // should be in real html file
console.log("document.getElementById('photo')", document.getElementById('photo')) // not mounted yet!!!
root.append("hello", img, input) // mounted
console.log("root", root)

// Select objects
console.log("document.getElementById('photo')", document.getElementById('photo'))
console.log("document.querySelector('#photo')", document.querySelector('#photo'))
console.log("root.querySelector('div>img')", root.querySelector('div>img'))
console.log("root.querySelector('div>img:nth-of-type(2)')", root.querySelector('div>img:nth-of-type(2)'))
console.log("root.querySelectorAll('div>img')", root.querySelectorAll('div>img'))
// selectorAll is greedy(search for all possibilities)
console.log("root.querySelectorAll(':scope>div>img')", root.querySelectorAll(':scope>div>img'))
// add ':scope' then it will works what you expected
let cnt = 0
for (const i of root.querySelectorAll('div>img'))
    console.log(`root.querySelcetorAll('div>img')[${cnt++}]`, i)
console.log("root.parentElement", root.parentElement)
console.log("root.parentNode", root.parentNode)
console.log("root.children", root.children)
console.log("root.childNode", root.childNodes)
console.log("root.firstChild", root.firstChild)
console.log("root.firstElementChild", root.firstElementChild)