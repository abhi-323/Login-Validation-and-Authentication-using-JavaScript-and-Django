
const login = document.querySelector("#submit");
    
    
    login.addEventListener("click" , (e) => {
        e.preventDefault();
        const username = document.querySelector("#username").value;
        const password = document.querySelector("#password").value;
        
        console.log(username);
        console.log(password);
        
        fetch(
            "http://127.0.0.1:8000/login" +
            `?username=${username}&password=${password}` 
            )
            .then((data) => data.text())
            .then((value) => {
                if(value=="success") {
                    alert("Login Successfull!!!");
                    window.location.href="home.html";
                }
                else  {
                        alert("Login Failed")
                    }  
                })
                .catch((e) => console.log(e));
                

            });
            

        
        // if(username.value == user && password.value == pass){
            //     document.write("You will be redirected to main page in 4 sec.");
            //     setTimeout(Redirect , 000);
            // }
            // else{
                //     alert("Login failed");
                // }
                
                // const Login = document.getElementById('submit');
                
                // Login.addEventListener("mouseenter" , () => {
                //     Login.style.backgroundColor = "grey";
                //     Login.style.color = "white";
                // });
                // Login.addEventListener("mouseout" , () => {
                //     Login.style.backgroundColor = "white";
                //     Login.style.color = "black";
                // });