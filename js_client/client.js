const contentContainer=document.getElementById("content-container")
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
            "Content-Type":"application/json"
        },
        body:JSON.stringify(loginObjectFormData)
    }
    fetch(loginEndPoint, options).then( //promise js thing 
        response=> {
            console.log(response)
            return response.json()
        }
    )
    .then(authData=>{
        handleAuthData(authData,getProductListData) //gets the tokens and calls the getProductlist func
    })
    .catch(err=>{
        console.log('err', err)
    })
}


function handleAuthData(authData, callback){ //function for storing tokens obtained after successful login
    localStorage.setItem('access',authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()  //essentially calls a func, if there is one
    }
}

function isTokenNotValid(jsonData){
    if (jsonData.code && jsonData.code==="token_not_valid"){
        //you can run a refresh token here, maybe
        alert("Please Login again")
    }
}

function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML+="<pre>"+JSON.stringify(data,null,4)+"</pre>"
    }
}

function getFetchOptions(method, body){
    return{
        method: method===null ? "GET" : method, //if?else
        headers:{
            "Content-Type":"application/json",
            "Authorization":`Bearer ${localStorage.getItem('access')}`
        },
        body:body? body:null //if?else
    }
}
function validateJWTToken() {
    // fetch
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint, options)
    .then(response=>{
        console.log(response.json())    
        response.json()
    })
    .then(x=> {
        // refresh token
    })
}
function getProductListData(){ //func to fetch product list from the api and write to 
    endpoint=`${baseEndPoint}/products/`
    const options=getFetchOptions() 
    fetch(endpoint,options)
    .then(response=>response.json())
    .then(data=>{
        writeToContainer(data)
    })
}

validateJWTToken()