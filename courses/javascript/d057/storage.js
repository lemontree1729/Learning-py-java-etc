const fileInput = document.getElementById('file-input')
const imgBox = document.getElementById('img-box')
let cnt = 0

function rememberImg(e) {
    console.log(localStorage)
    localStorage.setItem("file" + cnt++, e.target.result)
}
function displayImg(file) {
    const img = document.createElement('img')
    img.src = typeof file === 'string' ? file : URL.createObjectURL(file)
    imgBox.appendChild(img)
}
function uploadImg(e) {
    // initialize
    localStorage.clear()
    imgBox.innerHTML = ""
    cnt = 0
    const files = e.target.files
    // add for all files
    for (let file of files) {
        if (!file || file.type.split('/')[0] !== 'image') {
            imgBox.innerHTML = 'File type is not valid !'
            return;
        }
        let reader = new FileReader()
        reader.onload = rememberImg
        displayImg(file)
        reader.readAsDataURL(file)
    }
}
function renderImg() {
    for (let i = 0; i < localStorage.length; i++) {
        let stored = localStorage.getItem(localStorage.key(i))
        displayImg(stored)
    }
}
fileInput.addEventListener('change', uploadImg)
window.addEventListener('load', renderImg)