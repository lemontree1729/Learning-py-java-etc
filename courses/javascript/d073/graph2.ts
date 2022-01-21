const canvas = document.getElementById('graph')!
const unit = document.createElement('div')
unit.className = 'dot'

const dx = 5
const maxwidth = parseInt(window.getComputedStyle(canvas).width)
const maxheight = parseInt(window.getComputedStyle(canvas).height)
// const unitwidth = parseInt(window.getComputedStyle(unit).width)
// const unitheight = parseInt(window.getComputedStyle(unit).height)

function drawPoint(surface: HTMLElement, x: number, y: number) {
    const pointEl = document.createElement('div')
    pointEl.className = 'dot'
    pointEl.style.left = `${x}px`
    pointEl.style.top = `${maxheight / 2 - y}px`
    surface.appendChild(pointEl)
}

// function getPoint(div: HTMLDivElement) {
//     return [parseFloat(div.style.left), parseFloat(div.style.top)]
// }

function drawGraph(surface: HTMLElement, graph: Function) {
    surface.innerHTML = ""
    while (surface.childNodes.length < maxwidth)
        drawPoint(surface, surface.childNodes.length, graph(surface.childNodes.length))
}

function movePoint(div: HTMLDivElement, dx: number, dy: number) {
    div.style.left = `${parseFloat(div.style.left) + dx}px`
    div.style.top = `${parseFloat(div.style.top) + dy}px`
}

function moveGraph(surface: HTMLElement, graph: Function, dx: number, offset: number) {
    for (let i = 0; i < dx; i++)
        surface.removeChild(surface.firstChild!)
    // surface.removeChild(surface.lastChild!)
    surface.childNodes.forEach(v => movePoint(<HTMLDivElement>v, dx, 0))
    while (surface.childNodes.length < maxwidth)
        drawPoint(surface, surface.childNodes.length, graph(surface.childNodes.length + offset))
}

let c = 0
let myfunction = (x: number) => Math.sin(x * Math.PI / 180) * 100
drawGraph(canvas, myfunction)
let a = setInterval(() => moveGraph(canvas, myfunction, dx, c += dx), 1000)
setTimeout(() => clearInterval(a), 5000)