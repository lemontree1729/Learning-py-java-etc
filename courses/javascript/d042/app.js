const popupBtn = document.querySelector("#popup")
console.log(popupBtn)
popupBtn.onclick = function () {
    alert('popup')
}
popupBtn.addEventListener('mouseover', setBtnColor)
popupBtn.addEventListener('mouseout', unsetBtnColor)
document.addEventListener('click', getXY)
function setBtnColor(e) {
    console.log(e)
    popupBtn.style.background = "skyblue"
}
function unsetBtnColor(e) {
    console.log(e)
    popupBtn.style.background = ""
}


function getXY(e) {
    console.log("page:", e.pageX, e.pageY, "client:", e.clientX, e.clientY)
}


const form = document.querySelector('form')
const id = form.children[0]
const password = form.children[1]
const p = document.querySelector('p')
function login(e) {
    if (true == '1') {
        p.innerText = "hello?"
    }
    if (id.value == "" || password.value == "") {
        e.preventDefault()
        // p.innerText = "login failed"
    }
    else {
        alert('login is processing ...')
        p.innerText = ""
    }
}
form.addEventListener('submit', login)


const intstantMsg = document.querySelector('.instant-msg')
function showMsg() {
    intstantMsg.classList.add('show')
}
function hideMsg() {
    intstantMsg.classList.remove('show')
}
setTimeout(showMsg, 1000)
setTimeout(hideMsg, 3000)

const clock = document.querySelector("#clock")
console.log(clock)

function getTime() {
    function f(n) {
        return n < 10 ? '0' + n : n
    }
    const time = new Date()
    const h = time.getHours()
    const m = time.getMinutes()
    const s = time.getSeconds()
    clock.innerText = `${f(h)}:${f(m)}:${f(s)}`
}
setInterval(getTime, 1000)
