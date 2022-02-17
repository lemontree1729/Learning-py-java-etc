import React from "react";

function Todo({ user, name, done, description }) {
    // html template(JSX)
    return (
        <>
            <h3>name: {name}</h3>
            <h4>done: {done ? "finished" : "ongoing"}</h4>
            <p>description: {description}</p>
        </>
    )

}

// class Todo extends Component {
//     // data
//     constructor(props) {
//         super(props)
//         this.state = {
//             name: 'cleaning',
//             done: false,
//             description: "cleaning my room in weekends"
//         }
//     }

//     // event handler function
//     changeTodoName = () => {
//         console.log(this)
//         this.setState({ name: "sleeping" })
//     }

//     render() {
//         const { name, done, description } = this.state
//         const { user } = this.props

//         // html template(JSX)
//         return (
//             <>
//                 <h3>name: {name}</h3>
//                 <h4>done: {done ? "finished" : "ongoing"}</h4>
//                 <p>description: {description}</p>
//                 <button type="button" onClick={this.changeTodoName}>change name</button>
//             </>
//         )
//     }
// }

export default Todo