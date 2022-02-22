import '../App.css';
import { useState } from 'react';

interface users {
    name: string,
    age: number,
    email: string
}

function Users(probs: users) {
    function validate(probs: users): boolean {
        if (probs.age < 0 || !Number.isInteger(probs.age))
            return false
        if (!probs.email.includes("@") || !probs.email.endsWith(".com"))
            return false
        return true
    }
    if (validate(probs))
        return (
            <>
                <h1>
                    {probs.name}
                </h1>
            </>
        )
    else
        return (<></>
        )
}

export default Users