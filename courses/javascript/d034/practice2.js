// practice 2
const body = document.body

//nav bar
const nav = document.createElement('div')
nav.id = 'nav'
body.append(nav)
const menu = document.createElement('div')
menu.id = 'menu'
nav.append(menu)
for (let i = 0; i < 3; i++) {
    let temp = document.createElement('div')
    temp.className = 'bar'
    menu.append(temp)
}
const screenMode = document.createElement('div')
screenMode.id = 'screen-mode'
nav.append(screenMode)
const circleBtn = document.createElement('div')
circleBtn.id = 'circle-btn'
screenMode.append(circleBtn)
const profileMenu = document.createElement('div')
profileMenu.id = 'profile-menu'
nav.append(profileMenu)
const menuImg = document.createElement('img')
menuImg.src = './src/hamster.png'
profileMenu.append(menuImg)
const title = document.createElement('div')

//title
title.id = 'title'
body.append(title)
const center = document.createElement('div')
center.id = 'center'
title.append(center)
const heading = document.createElement('div')
heading.id = 'heading'
center.append(heading)
const titleText = document.createElement('h1')
titleText.append("My photo gallery")
heading.append(titleText)
const subtitleText = document.createElement('h4')
subtitleText.append("my old memories from my life")
heading.append(subtitleText)
const search = document.createElement('div')
search.id = 'search'
center.append(search)
const searchInput = document.createElement('input')
searchInput.type = 'text'
searchInput.placeholder = 'Search photo ...'
search.append(searchInput)

// photolist
const photoList = document.createElement('div')
photoList.id = 'photo-list'
body.append(photoList)
for (let i = 0; i < 9; i++) {
    let temp1 = document.createElement('div')
    temp1.className = 'photo-container'
    photoList.append(temp1)
    let temp2 = document.createElement('div')
    temp2.className = 'photo-card'
    temp1.append(temp2)
    let temp3 = document.createElement('img')
    temp3.src = './src/watermelon.jpg'
    temp3.alt = ''
    temp2.append(temp3)
    let temp4 = document.createElement('div')
    temp4.className = 'photo-name'
    temp4.append("name")
    temp1.append(temp4)
}

// modal window
const modalWindow = document.createElement('div')
modalWindow.className = 'modal-window'
body.append(modalWindow)
const modalHeader = document.createElement('div')
modalHeader.id = 'header'
modalHeader.append("Food Recipe")
modalWindow.append(modalHeader)
const modalBody = document.createElement('div')
modalBody.id = 'body'
modalWindow.append(modalBody)
const modalBodyText = document.createElement('p')
modalBodyText.append("Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, magni voluptatibus commodi voluptate, ipsa ab\
itaque excepturi nesciunt velit ratione possimus impedit rerum accusantium quod at molestias iure, facere blanditiis.\
Doloribus distinctio culpa fugiat quae, totam possimus perspiciatis fuga, dolorem officia dicta adipisci quidem tempora\
suscipit ad magnam aliquid atque! Quae aut voluptatem cumque officia inventore maiores maxime necessitatibus optio!\
Placeat aspernatur esse obcaecati ex saepe quo, possimus qui sapiente sequi temporibus.Enim, non officiis quaerat\
nesciunt alias architecto repellat consequatur nemo porro ducimus ipsam repudiandae est cum, necessitatibus consectetur!")
modalBody.append(modalBodyText)
const modalFooter = document.createElement('div')
modalFooter.id = 'footer'
modalWindow.append(modalFooter)
const closeButton = document.createElement('button')
closeButton.append("Close")
modalFooter.append(closeButton)

// practice 3
const h4 = body.querySelector('h4')
console.log("h4.innerText", h4.innerText)
h4.innerText = "foods that i want to eat right now"

// practice 4
const profile = body.querySelector('div#profile-menu')
console.log("profile", profile)
profile.firstElementChild.src = './src/owl.jpg'

// practice 5
const thirdimg = photoList.querySelector('div:nth-of-type(3)>div>img')
console.log("thirdimg", thirdimg)
thirdimg.src = './src/pizza.jpg'

// practice 6
const fifthdiv = photoList.querySelector('div:nth-of-type(5)>div:nth-of-type(2)')
console.log("fifthdiv", fifthdiv)
fifthdiv.innerText = 'sunrise'

// practice 7
const target = body.querySelector('.modal-window')
console.log("target", target)
target.className = 'modal-window hide'