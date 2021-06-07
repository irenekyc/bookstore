const book_slug = window.location.pathname.replace('/books/', "")
let currentBookInCart = false
let booksInCart = []

const init = ()=>{
    if (document.cookie){
        const book_store_cookie = document.cookie.split(";").filter(cookieItem => cookieItem.includes('book_store_cookie'))
        if (book_store_cookie.length > 0){
            const books = book_store_cookie[0].replace("book_store_cookie=", "")
            // get current books and convert to an array
            booksInCart = JSON.parse(books)
            if (booksInCart.includes(book_slug)){
                currentBookInCart = true
                loadText()
            } else{
                currentBookInCart = false
                loadText()
            }
        } 
    }
}
window.addEventListener('DOMContentLoaded', init)
const loadText = ()=>{
    if (currentBookInCart){
        return document.getElementById('cart-text').innerHTML="Remove from cart"
    } else{
        return document.getElementById('cart-text').innerHTML = 'Add to cart'
    }
}
const cartOnClick = () =>{
    if (currentBookInCart){
        // remove
        currentBookInCart = false
        booksInCart = booksInCart.filter(book => book != book_slug)
        document.cookie=`book_store_cookie=${JSON.stringify(booksInCart)}`
        loadText()
    } else{
        booksInCart.push(book_slug)
        document.cookie=`book_store_cookie=${JSON.stringify(booksInCart)}`
        currentBookInCart = true
        loadText()
    }
}