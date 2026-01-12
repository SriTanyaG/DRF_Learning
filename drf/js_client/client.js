const loginForm = document.getElementById('login-form');
const baseEndpoint = 'http://localhost:8000/api';
if (loginForm) {
    // handle this login form
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    console.log(event)
    event.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);    //helps us get the form data using that function
    let loginObjectData = Object.fromEntries(loginFormData.entries());  //converts form data to object
    console.log(loginObjectData);
    const options = {
        "meathod": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(loginObjectData)
    }
    fetch(loginEndpoint, options)  // requests.posts

    .then(reponse =>{
        console.log(response)
        return response.json()
    })
    .then(x=>{
        console.log(x)
    })
    .catch(err=>{
        console.log(err)
    })
}