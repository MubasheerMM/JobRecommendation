
function showLogin(){
    document.querySelector('.login-wrapper').style.display = "flex"
    document.querySelector('.signup-wrapper').style.display = "none"
}

function showSignup(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "flex"
    document.querySelector('.box1').style.display = "flex"
    document.querySelector('.box2').style.display = "none"
}

function closeLogin(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "none"
}

function closeSignup(){
    document.querySelector('.login-wrapper').style.display = "none"
    document.querySelector('.signup-wrapper').style.display = "none"
}

function showNext(){
    try{
        document.querySelector('.footer').style.position = "relative"

        document.querySelector('.footer').style.marginTop = "180px"
    }
    catch{
        console.log("");
    }
    var inputs = document.querySelectorAll('.inp')
            var error = 0;
            for(var i = 0;i<inputs.length;i++){
                if(inputs[i].value == ''){
                    error = 1
                    console.log("false");
                    alert('please fill the fields')
                    inputs[i].style.border = "2px solid red"
                    break
                }
                else{
                    inputs[i].style.border = "1px solid rgb(226, 226, 226)"
                    error = 0
                }

                

            }

            var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

            var email = 0
            if (document.querySelector('.email1').value.match(validRegex)) {
                        
                
                       
                    error = 0
                    email = 0
                    console.log("");

            } 
            else {

                    alert("Invalid email address!");
                    error = 1
                    email = 1
                    document.querySelector('.email1').style.border = "2px solid red"

            }
            try
            {
            if(document.querySelector('.pass1').value != document.querySelector('.pass2').value){
                alert("Passwords dosent match")
                error = 1
            }

            else if(document.querySelector('.pass1').value.length < 7){
                alert("Password length should be greater than 7")
                error = 1
            }
            else if(document.querySelector('.pass1').value.search(/[A-Z]/) < 0){
                alert("Your password needs an uppercase letter")
                error = 1
            }

            else{
                error = 0
            }
            }
            catch{
                console.log("1");
            }

            if(error == 0 && email == 0){
                document.querySelector('.box2').style.display = "flex"
                document.querySelector('.box1').style.display = "none"
            }

            
}


function showNext2(){
    try{
        document.querySelector('.footer').style.position = "relative"

        document.querySelector('.footer').style.marginTop = "180px"
    }
    catch{
        console.log("");
    }
    var inputs = document.querySelectorAll('.inp')
            var error = 0;
            for(var i = 0;i<inputs.length;i++){
                if(inputs[i].value == ''){
                    error = 1
                    console.log("false");
                    alert('please fill the fields')
                    inputs[i].style.border = "2px solid red"
                    break
                }
                else{
                    inputs[i].style.border = "1px solid rgb(226, 226, 226)"
                    error = 0
                }

                

            }

            var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

            var email = 0
            if (document.querySelector('.email1').value.match(validRegex)) {
                        
                
                       
                    
                    email = 0
                    console.log("");

            } 
            else {

                    alert("Invalid email address!");
                    
                    email = 1
                    document.querySelector('.email1').style.border = "2px solid red"

            }
            try
            {
            if(document.querySelector('.pass1').value.length < 7){
                alert("Password length should be greater than 7")
                error = 1
            }
            else if(document.querySelector('.pass1').value.search(/[A-Z]/) < 0){
                alert("Your password needs an uppercase letter")
                error = 1
            }

            else{
                error = 0
            }
            }
            catch{
                console.log("1");
            }

            if(error == 0 && email == 0){
                document.querySelector('.box2').style.display = "flex"
                document.querySelector('.box1').style.display = "none"
            }

            
}

function showNext1(){
    

    var inputs = document.querySelectorAll('.inp3')
            var error = 0;
            var displayed = 0
            for(var i = 0;i<inputs.length;i++){
                if(inputs[i].value == ''){
                    error = 1
                    console.log("false");
                    if(displayed == 0){
                        displayed = 1
                        alert('please fill the fields')
                        error = 1
                    }
                    inputs[i].style.border = "2px solid red"
                    break
                }
                else{
                    inputs[i].style.border = "1px solid rgb(226, 226, 226)"
                    error = 0
                }

                

            }

            

            if(error == 0){
                document.querySelector('.box5').style.display = "flex"
                document.querySelector('.box4').style.display = "none"
            }

            
}

function showPrevious(){
    document.querySelector('.box1').style.display = "flex"
    document.querySelector('.box2').style.display = "none"
    document.querySelector('.footer').style.position = "fixed"
}

function showPrevious1(){
    document.querySelector('.box4').style.display = "flex"
    document.querySelector('.box5').style.display = "none"
}


function setProfilePic(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            // document.querySelector('.profile-pic').style.display = "flex"
            // document.querySelector('.profile-pic-name').textContent = input.value.replace("C:\\fakepath\\","")
            $('.profile-pic')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }

    document.querySelector('.chooseImg').style.backgroundColor ="#06af50"
    document.querySelector('.chooseImg').style.color ="#fff"
    document.querySelector('.chooseImg').style.border ="2px soild #06af50"
}

function showGig(){
    document.querySelector('.gig-wrapper').style.display = "flex"
    document.querySelector('.box4').style.display = "flex"
    // document.querySelector('.box2').style.display = "none"
}

function closeGig(){
    document.querySelector('.gig-wrapper').style.display = "none"
    document.querySelector('.box4').style.display = "none"
    document.querySelector('.box5').style.display = "none"
    // document.querySelector('.box2').style.display = "none"
}


function showMenu(){
    if(document.querySelector('.menuOpen').value == "0"){
        document.querySelector('.menu-wrap').style.display = "flex"
        document.querySelector('.menuOpen').value = "1"
        document.querySelector('.mbtn').innerHTML = '<ion-icon name="close"></ion-icon>'
    }
    else{
        document.querySelector('.menu-wrap').style.display = "none"
        document.querySelector('.menuOpen').value = "0"
        document.querySelector('.mbtn').innerHTML = '<ion-icon name="menu-outline"></ion-icon>'
    }
}