const hairColors = ['black', 'brown', 'yellow', 'white', 'gold']
const hairTypes = ['curly', 'straight', 'wavy', 'coily']
const glasses = [true, false]
const heights = [150, 160, 170, 180, 190, 200]
const weights = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

function pickRandomNumber(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}

function pickRandonElement(array: Array<any>) {
    return array[pickRandomNumber(0, array.length - 1)]
}

class Person {
    hairColor: string
    hairType: string
    glasses: boolean
    height: number
    weight: number
    constructor() {
        this.hairColor = pickRandonElement(hairColors)
        this.hairType = pickRandonElement(hairTypes)
        this.glasses = pickRandonElement(glasses)
        this.height = pickRandonElement(heights)
        this.weight = pickRandonElement(weights)
    }
}

const total_user: Array<Person> = []
for (let i = 0; i < 10000; i++)
    total_user.push(new Person())

const total_count: any = {}
total_user.forEach(
    v => Object.values(v).forEach(
        ele => {
            if (typeof total_count[ele] === 'undefined')
                total_count[ele] = 1
            else
                total_count[ele] += 1
        }
    ))
console.log(total_count)