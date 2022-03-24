const loginForm= document.getElementById("login-form")

const baseEndPoint= "http://localhost:8000/api"

if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndPoint=`${baseEndPoint}/token/` //backticks used for string substitution

    let loginFormData= new FormData(loginForm) //FormData is an inbuilt func to get the form data from a form
    let loginObjectFormData= Object.fromEntries(loginFormData)
    let bodyString=JSON.stringify(loginObjectFormData)
    const options={
        method:"POST",
        headers: {
            "ContentType":"application/json"
        },
        body:JSON.stringify(loginObjectFormData)
    }
    fetch(loginEndPoint, options).then(
        response=> {
            console.log(response)
            return response.json()
        }
    )
    .then(x=>{
        console.log(x)
    })
    .catch(err=>{
        console.log('err', err)
    })
}