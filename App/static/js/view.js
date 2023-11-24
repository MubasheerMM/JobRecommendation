
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

            if (document.querySelector('.email1').value.match(validRegex)) {
                        
                
                       
                    error = 0
                    console.log("");

                    } 
                else {

                    alert("Invalid email address!");
                    error = 1
                    document.querySelector('.email1').style.border = "2px solid red"

                }

            if(error == 0){
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
                    }
                    inputs[i].style.border = "2px solid red"
                    
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