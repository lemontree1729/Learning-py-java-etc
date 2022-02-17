import React from 'react'

const Person = ({ name, age }) => {
    // const name = "learning react"
    // const age = "9"
    return (
        <>
            <h3>{name}</h3>
            <h3>{age}</h3>
        </>
    )
}

export default Person