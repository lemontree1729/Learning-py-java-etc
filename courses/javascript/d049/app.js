const pageContents = [
    'page 1', 'page 2', 'page 3', 'page 4', 'page 5',
    'page 6', 'page 7', 'page 8', 'page 9', 'page 10',
]

const contents = document.getElementById('contents')
const pageBtns = document.getElementById('page-btns')

for (let i = 0; i < pageContents.length; i++) {
    const btn = document.createElement('button')
    btn.className = 'page-btn'
    btn.innerText = i + 1
    pageBtns.appendChild(btn)
}
contents.innerHTML = pageContents[0]

function changePage(e) {
    const target = e.target
    if (target.className === 'page-btn') {
        console.log(target)
        const indexSelected = parseInt(target.innerText) - 1
        console.log(indexSelected)
        contents.innerHTML = pageContents[indexSelected]
    }
}

pageBtns.addEventListener('click', changePage)