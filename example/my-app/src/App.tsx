import React from 'react';
import './App.css';
import Counter from './practice2/Counter'
import Title from './practice2/Title'
import Cart from './practice2/Cart'
import PhotoGallery from './practice2/PhotoGallery';
import Users from './practice3/Users';

const users = [
  { name: 'victoria', age: 13, city: 'seoul', email: 'victoria@gmail.com' },
  { name: 'sun', age: 34, city: 'busan', email: 'sun@gmail.com' },
  { name: 'johseb', age: 25, city: 'busan', email: 'johseb@gmail' }, // 탈락
  { name: 'syleemomo', age: 9.23, city: 'seoul', email: 'syleemomo@nate.com' }, // 탈락
  { name: 'hannah', age: 41, city: 'daegu', email: 'hannah0923*gmail.com' }, // 탈락
  { name: 'shara', age: 37, city: 'seoul', email: 'shara@gmail.com' },
  { name: 'martin', age: -34, city: 'daegu', email: 'martin@gmail.com' }, // 탈락
  { name: 'gorgia', age: 39, city: 'seoul', email: 'gorgia@gmail.com' },
  { name: 'nana', age: 24, city: 'busan', email: 'nana@gmail.com' },
  { name: 'dannel', age: 19, city: 'seoul', email: 'dannel@gmail.com' },
]

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <Counter /> */}
        {/* <Cart /> */}
        {/* <PhotoGallery /> */}
        {users.map(value => <Users {...value} />)}
      </header>
    </div>
  );
}

export default App;
