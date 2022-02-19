import Friends from './Friends';
import Person from './Person';
import Book from './Book';
import Animal from './Animal';

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
]
const bookInfo = {
    title: '해리포터',
    author: '조앤K롤링',
    summary: '해리포터가 마법사로 성장해나가는 과정을 그린 이야기',
    genre: '판타지 소설',
    release: '2003년 9월 4일',
    ISBN: '1234567890'
}

const animalInfo = {
    type: 'cat',
    name: 'meyow',
    size: 'small',
    sound: 'low',
    appearence: 'cute'
}

function Practice({ num }) {
    const toggle = {
        1: <>
            {friends.map(({ name, age, city }) => < Friends name={name} age={age} city={city}></Friends>)}
        </>,
        2: <Person />,
        3: <Book {...bookInfo} />,
        4: <Animal {...animalInfo} />
    }[num]
    return (
        <div className="App">
            <header className="App-header">
                {toggle}
            </header>
        </div >
    );
}

export default Practice;