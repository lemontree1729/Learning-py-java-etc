const tiles = document.querySelectorAll("td")
function changeTileColor(event) {
    let r = Math.floor(Math.random() * 256)
    let g = Math.floor(Math.random() * 256)
    let b = Math.floor(Math.random() * 256)
    console.log(`rgb(${r}, ${g}, ${b})`)
    event.target.style.backgroundColor = `rgb(${r}, ${g}, ${b})`
}
for (let j = 0; j < tiles.length; j++) {
    tiles[j].addEventListener('click', changeTileColor)
}