import '../App.css';
import { useState } from 'react';

function Counter() {
    const [cnt, setCnt] = useState(0)
    function countNumber() {
        setCnt((cnt) => ++cnt)
    }
    return (
        <div className="App">
            <h1>Count: {cnt}</h1>
            <button type="button" onClick={countNumber}>change name</button>
        </div>
    )
}

export default Counter;