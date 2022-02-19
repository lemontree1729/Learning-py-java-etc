import '../App.css';
import { useState } from 'react';

function Title() {
    const [title, setTitle] = useState<String>("before")
    function changeTitle() {
        setTitle("after")
    }
    return (
        <div className="App">
            <h1>: {title}</h1>
            <button type="button" onClick={changeTitle}>change title</button>
        </div>
    )
}

export default Title;