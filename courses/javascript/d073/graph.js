const graph = document.getElementById('graph')

const points = []
const dx = 1
let x = 0
let y = 0
let radx = 0

function getNextPoint() {
    radx = x * (Math.PI / 180)
    y = Math.sin(radx)
    y = Math.sin((x++) * (Math.PI / 180))
    points.push([x, y])
    x += dx
    // console.log(points)
}


function displayPoint(point) {
    const pointEl = document.createElement('div')
    pointEl.className = 'dot'
    pointEl.style.left = `${point[0] * 2}px` // x-scale: 2
    pointEl.style.top = `${point[1] * 100 * -1 + 100}px` // y-scale : 100
    graph.appendChild(pointEl)
}
function movePoint(pointEl) {
    // console.log(pointEl.style.left)
    pointEl.style.left = `${(parseFloat(pointEl.style.left) + 2) % 720}px`
    pointEl.style.right = `${(parseFloat(pointEl.style.right) + 100) % 200}px`
}

for (let i = 0; i < 360; i++) {
    getNextPoint()
}
// console.table(points)
points.forEach(displayPoint)
setInterval(() => graph.childNodes.forEach(movePoint), 1)