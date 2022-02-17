import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
// practice1 here
import Practice from './practice1/Practice'
import reportWebVitals from './reportWebVitals';
import { BrowserRouter, Route, Routes, Link } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/practice1">About Us</Link>
      </li>
      <li>
        <Link to="/contact">
          Contact Us
        </Link>
      </li>
      <Routes>
        <Route exact path="/" component={App} />
        <Route exact path="/practice1" component={Practice({ num: 1 })} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode >,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
