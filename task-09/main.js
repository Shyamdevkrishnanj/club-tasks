function myFunction(form) {
    var isLogin = false;
    var store = {
        "shyam": 1234, "sdkrish@gmail.com": 111
    };
    var name =form.uname.value;
    var password=form.psw.value;

    if (name in store) {
        if (store[name] == password) {
           isLogin = true;          
        }
        else {
            alert("Login Failed");
        }
    }
        
    if(isLogin){

        window.location.href = "index.html";

        alert("Login successful");
    }
}

