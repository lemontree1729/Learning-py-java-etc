const box = document.querySelectorAll('.box')
let cnt = 0
let prev = box.length - 1
function bounce() {
    box[cnt].style.marginBottom = '80px'
    box[prev].style.marginBottom = '0'
    prev = cnt
    cnt = ++cnt % box.length
}
setInterval(bounce, 500)