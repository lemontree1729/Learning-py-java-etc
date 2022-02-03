// import http from 'http'
const http = require("http")
const option = {
    hostname: "http://open.mapquestapi.com",
    path: "/geocoding/v1/address?key=KEY&location=Washington,DC",
    method: 'GET',
}
const url = "http://open.mapquestapi.com/geocoding/v1/address?key=KEY&location=Washington,DC"
const req = http.get(url, (res: any) => {
    console.log(`STATUS: ${res.statusCode}`);
    console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
    res.setEncoding('utf8');
    res.on('data', (chunk: any) => {
        console.log(`BODY: ${chunk}`);
    });
    res.on('end', () => {
        console.log('No more data in response.');
    });
});
req.end()