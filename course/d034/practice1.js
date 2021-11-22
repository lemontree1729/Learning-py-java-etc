// practice 1
const body = document.body
const root = document.createElement('div')
root.id = 'root'
body.append(root)
const container = document.createElement('div')
container.id = 'photo-container'
root.append(container)
for (let i = 0; i < 5; i++) {
    let item = document.createElement('div')
    item.className = 'photo-item'
    container.append(item)
    let img = document.createElement('img')
    img.src = 'http://127.0.0.1:5500'
    img.alt = `photo${i + 1}`
    item.append(img)
}
const target = document.querySelectorAll('.photo-item>img')
console.log(target[0].alt)