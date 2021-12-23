const FPS = 120, limitBottom = 500, limitLeft = 700, limitTop = 300
const box = document.getElementById('box')
const bar = document.getElementById("bar")
const varrow = 7, vspace = 7
let x = 0, y = -100, vx = 0, vy = 0, ax = 0, ay = 1
let isJumping = true, isDead = false, keyStore = {}
let direction = ""
function move(target) {
    x += vx += ax
    y += vy += ay
    target.style.left = x + "px"
    target.style.top = y + "px"
}

function checkCollide(target, origin) {
    let targetRect = target.getBoundingClientRect()
    let originRect = origin.getBoundingClientRect()

    direction = ""
    if (!(
        ((targetRect.top + targetRect.height) < originRect.top) ||
        (targetRect.top > (originRect.top + originRect.height)) ||
        ((targetRect.left + targetRect.width) < originRect.left) ||
        (targetRect.left > (originRect.left + originRect.width))
    )) {
        let targetCenterX = (targetRect.left + targetRect.right) / 2, targetCenterY = (targetRect.top + targetRect.bottom) / 2
        if (targetCenterY < originRect.top)
            direction += "N"
        if (targetCenterY > originRect.bottom)
            direction += "S"
        if (targetCenterX > originRect.right)
            direction += "E"
        if (targetCenterX < originRect.left)
            direction += "W"
        return direction
    }
    return ""
}
function changePos() {
    console.time()
    ay = 0.2, vx = 0
    // gravity
    var collide = checkCollide(box, bar)
    console.log(collide)
    // key move
    if (keyStore["ArrowRight"]) {
        box.style.backgroundImage = `url("src/cartoon-right.png")`
        vx = varrow
    }
    if (keyStore["ArrowLeft"]) {
        box.style.backgroundImage = `url("src/cartoon-left.png")`
        if (x > 0)
            vx = -varrow
    }
    if (keyStore[" "] || keyStore["ArrowUp"]) {
        if (!isJumping && y >= limitTop) {
            vy = -7
            isJumping = vspace
        }
    }
    if (!isDead && (collide.includes("N") || collide.includes("S"))) {
        ay = 0, vy = 0
        isJumping = false
    }
    else if (!isDead && (collide.includes("E") || collide.includes("W"))) {
        vx = 0
    }
    move(box)
    console.log(`checkCollide: ${checkCollide(box, bar)}, isJumping: ${isJumping}, isDead: ${isDead}`)
    console.log(`(x, y): (${x}, ${y}), (vx, vy): (${vx}, ${vy}), keyStore:`, keyStore)
    console.timeEnd()
}
setInterval(changePos, 1000 / FPS)
window.addEventListener("keydown", e => { keyStore[e.key] = true })
window.addEventListener("keyup", e => { keyStore[e.key] = false })