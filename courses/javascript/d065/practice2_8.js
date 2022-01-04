"use strict";
//practice2
const companies = ['Samsung', 'LG', 'Google', 'Facebook', 'Amazon'];
const companiesReversed = [];
[...companies].forEach(() => companiesReversed.push(companies.pop()));
console.log(companiesReversed);
//practice3
const friends = [
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
const newFriends = [
    { name: 'Ami', age: 27, city: 'ulsan' },
    { name: 'gracias', age: 21, city: 'ulsan' },
];
const mergeFriends = [...friends];
mergeFriends.splice(2, 0, ...newFriends);
console.log(mergeFriends);
//practice4
console.log(friends.filter(value => value.name !== "hannah" && value.name !== "shara"));
//practice5
console.log(friends.filter(value => value.city !== "seoul"));
//practice6
console.log([...friends]
    .sort((a, b) => a.age - b.age)
    .filter(value => value.age < 30));
//practice7
console.log([...friends].sort((a, b) => a.name.localeCompare(b.name)));
//practice8
const movies = [
    { title: 'Harry Potter', release: '2003-02-22' },
    { title: 'Indiana Jhones', release: '2009-01-09' },
    { title: 'Terminator', release: '2007-04-11' },
    { title: 'Dracula', release: '2007-04-13' },
    { title: 'Jurassic Park', release: '2007-05-13' },
    { title: 'Iron man', release: '2012-12-18' },
    { title: 'Spider man', release: '2017-03-07' }
];
console.log([...movies].sort((a, b) => -a.release.localeCompare(b.release)));
