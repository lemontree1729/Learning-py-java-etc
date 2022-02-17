import '../App.css'

function Book(probs) {
    return (
        <>
            <h1>Book Info</h1>
            {Object.entries(probs).map(([key, value]) => <h3>{key} - {value}</h3>)}
        </>
    )
}

export default Book