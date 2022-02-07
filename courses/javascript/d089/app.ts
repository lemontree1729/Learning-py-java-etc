function Music() {
    const music = {
        name: '금요일에 만나요',
        artist: 'IU',
        release: '2013-12-20',
        info() {
            console.log(this)
            console.log(`${this.name} - ${this.artist} 는 ${this.release} 에 발매되었다.`)
        }
    }
    return music
}

const music = Music()
music.info()