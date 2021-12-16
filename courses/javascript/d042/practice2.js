const body = document.querySelector('body')
const container = document.createElement('div')
container.style.width = '100%'
container.style.height = '100vh'
body.appendChild(container)
function makeImage(e) {
    console.log("hello?")
    const image = document.createElement('div')
    image.className = 'circle'
    image.style.top = e.pageY + "px"
    image.style.left = e.pageX + "px"
    container.appendChild(image)
}
container.addEventListener('click', makeImage)