const photos = document.getElementById('photos')
const photoItems = photos.querySelectorAll('.photo')
const options = document.querySelectorAll('.options')
let timerID = null
let initID = null
let cnt = 0
let prev = 0
options[prev].style.backgroundColor = 'black'

function findKey(object, value) {
    for (key in object) {
        if (value === object[key])
            return key
    }
}
function changePosition() {
    let n = photoItems.length
    cnt++
    photos.style.marginLeft = cnt * -500 + 'px'
    if (cnt === n - 1) {
        initID = setTimeout(function () {
            photos.style.transition = 'all 0s'
            photos.style.marginLeft = '0'
        }, 900)
        setTimeout(function () {
            photos.style.transition = 'all 1s'
        }, 1000)
        cnt = 0
    }
    toggleOptions(cnt)
    prev = cnt
}
function toggleOptions(num) {
    options[prev].style.backgroundColor = ''
    options[num].style.backgroundColor = 'black'
}
function toggleCarousel(e) {
    let num = findKey(options, e.target)
    stopCarousel()
    clearTimeout(initID)
    toggleOptions(num)
    cnt = prev = num
    photos.style.marginLeft = cnt * -500 + 'px'
    startCarousel()
}

function startCarousel() {
    timerID = setInterval(changePosition, 3000)
}

function stopCarousel() {
    clearInterval(timerID)
}
startCarousel()
photos.addEventListener('mouseenter', stopCarousel)
photos.addEventListener('mouseleave', startCarousel)
for (let i = 0; i < photoItems.length - 1; i++)
    options[i].addEventListener('click', toggleCarousel)
