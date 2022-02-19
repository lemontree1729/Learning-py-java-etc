import { useState } from 'react'

function Cart() {
    const [cart, setCart] = useState<Array<string>>([])
    function addProduct() {
        const product = prompt("enter product name to add!")
        setCart(cart => product && !cart.includes(product) ? [...cart, product] : cart)
    }

    return (
        <>
            <button onClick={addProduct}>click to add product!</button>
            <h1>Products</h1>
            -----------------------------------
            {cart.map(product => <h3>{product}</h3>)}
        </>
    )
}

export default Cart