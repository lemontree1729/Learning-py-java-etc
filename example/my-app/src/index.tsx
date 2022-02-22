import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

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


ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
