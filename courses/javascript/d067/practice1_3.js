//practice1
const friends2 = [
    { name: 'victoria', age: 13, city: 'seoul' },
    { name: 'sun', age: 34, city: 'busan' },
    { name: 'johseb', age: 25, city: 'busan' },
    { name: 'syleemomo', age: 9, city: 'seoul' },
    { name: 'hannah', age: 41, city: 'daegu' },
    { name: 'shara', age: 37, city: 'seoul' },
    { name: 'martin', age: 28, city: 'daegu' },
    { name: 'gorgia', age: 39, city: 'seoul' },
    { name: 'nana', age: 24, city: 'busan' },
    { name: 'dannel', age: 19, city: 'seoul' },
];
console.log([...friends2]
    .sort((a, b) => a.city.localeCompare(b.city) || a.age - b.age));
// @ts-ignore
import novel from "./sherlock.js";
//practice2
let origin = novel;
console.log(origin
    .replace(/the /g, "● ")
    .replace(/of /g, "❤ ")
    .replace(/and /g, "■ "));
//practice3
let words = {};
origin.toLowerCase()
    .split(/[\n\s,.:—\-’]+/)
    .forEach(value => words[value] = words[value] ? ++words[value] : 1);
console.log(Object.entries(words).sort((a, b) => b[1] - a[1]));
let list = {};
origin.toLowerCase()
    .split("")
    .filter(value => value.match(/^[a-z]/))
    .forEach(value => list[value] = list[value] ? ++list[value] : 1);
console.log(Object.entries(list).sort((a, b) => b[1] - a[1]));
