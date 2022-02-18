import React from 'react';

class Person extends React.Component {
    state = {
        name: "sunrise",
        age: 23,
        friends: [
            "victoria",
            "daniel",
            "hanna"
        ]
    }
    displayInfo = () => {
        alert(`INFO:\n${JSON.stringify(this.state)}`)
    }

    render() {
        return (
            <>
                <button onClick={this.displayInfo}>Info</button>
            </>
        )
    }
}

export default Person;