class Book {
    private name: string
    private price: number
    private release: string
    private authors: Array<string>
    constructor(name: string, price: number, release: string, authors: Array<string>) {
        this.name = name
        this.price = price
        this.release = release
        this.authors = authors
    }
    getInfo() {
        console.log('----- 책 정보 -----')
        console.log('제목: ', this.name)
        console.log('가격: ', this.price)
        console.log('초판: ', this.release)
        console.log('저자: ', this.authors.join(' '))
    }
    get getPrice() {
        return this.price
    }
    set setPrice(price: number) {
        this.price = price
    }
    get getName() {
        return this.name
    }
    set addAuthor(newAuthor: any) {
        this.authors.push(newAuthor)
    }
}
class BookStore extends Book {
    constructor(name: string, price: number, release: string, authors: Array<string>) {
        super(name, price, release, authors)
    }
    discount() {
        if (this.getName === 'python') {
            this.setPrice = this.getPrice - 1000
        }
    }
}

const book1 = new (BookStore as any)(
    'javascript',
    21000,
    '2019-12-03',
    ['mark', 'victoria']
)
const book2 = new (BookStore as any)(
    'python',
    18700,
    '2022-01-07',
    ['syleemomo']
)


book1.discount()
book1.addAuthor = 'sunrise'
console.log(book1.name, book1.getPrice)
console.log(book1.authors)

book2.discount()
console.log(book2.name, book2.getPrice)