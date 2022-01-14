//practice1
const _2dArray = []
for (let i = 0; i < 10; i++) {
    _2dArray.push([i + 1, i + 2])
}
console.log(_2dArray)

//practice2
function build2DArray(rows, columns) {
    return Array.from({ length: rows }, () => Array.from({ length: columns }, () => 0))
}
console.log(build2DArray(7, 3))

//practice3
let fruits = [['apple', 570], ['orange', 270], ['strawberry', 30]]
let newfruits = []
fruits.forEach(v => {
    let temp = new Object()
    temp[v[0]] = v[1]
    newfruits.push(temp)
})
console.log(newfruits)

//practice4
fruits = [['apple', 570, 32], ['orange', 270, 65], ['strawberry', 30, 120]]
newfruits = []
fruits.forEach(v => {
    let temp = new Object()
    temp = { "name": v[0], "totalPrice": v[1] * v[2] }
    newfruits.push(temp)
})
console.log(newfruits)