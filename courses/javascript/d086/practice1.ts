function pickRandomNumber(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}

class Tester {
    time_to_sleep: number
    time_to_awake: number
    half_awake_count: number
    toss_count: number
    delta_wave_ratio: number
    sleep_rating = 0

    constructor() {
        this.time_to_sleep = pickRandomNumber(1, 10)
        this.time_to_awake = pickRandomNumber(1, 10)
        this.half_awake_count = Number(Math.random() * 5 + 1)
        this.toss_count = pickRandomNumber(1, 10)
        this.delta_wave_ratio = pickRandomNumber(0, 50)
        this.sleep_rating = this.calculate_rating()
    }
    calculate_rating() {
        return this.delta_wave_ratio / (this.time_to_sleep * this.time_to_awake * this.half_awake_count * this.toss_count)
    }
    get getRating() {
        return this.sleep_rating
    }
    well_sleep() {
        if (this.sleep_rating >= 0.37)
            return true
        return false
    }
}
const total_group: Array<Array<Tester>> = []
for (let i = 0; i < 3; i++) {
    const group = []
    for (let j = 0; j < 100; j++) {
        group.push(new Tester())
    }
    total_group.push(group)
}
console.log(total_group)
total_group.forEach((v, i) => console.log(`group${i}: ${v.filter(tester => tester.well_sleep()).length}`))
