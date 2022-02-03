class Station {
    name: string
    longitude: number
    latitude: number
    constructor(name: string, latitude: number, longitude: number) {
        this.name = name
        this.latitude = latitude
        this.longitude = longitude
    }
    get getName() {
        return this.name
    }
    getDistance(destination: Station) {
        const R = 6371e3;
        const φ1 = this.latitude * Math.PI / 180;
        const φ2 = destination.latitude * Math.PI / 180;
        const Δφ = φ2 - φ1;
        const Δλ = (destination.longitude - this.longitude) * Math.PI / 180;
        const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
            Math.cos(φ1) * Math.cos(φ2) *
            Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c
    }
    getPrice(destination: Station) {
        const price_per_km = 100
        const distance = this.getDistance(destination)
        return distance / 1000 * price_per_km
    }
}
const total_station = []
total_station.push(new Station("seoul", 37.55620110026294, 126.97223116703012))
total_station.push(new Station("daejeon", 36.332516127741, 127.43421099777726))
total_station.push(new Station("daegu", 35.88049128950934, 128.62837657353532))
total_station.push(new Station("busan", 35.116613680508806, 129.04009077373016))
const priseTable: any = {}
for (let station of total_station)
    for (let other_station of total_station) {
        if (station === other_station)
            break
        priseTable[`${station.getName}_to_${other_station.getName}`] = station.getPrice(other_station);
    }
console.table(priseTable)