const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid_feedback"); 
const emailField = document.querySelector("#emailField");
const passwordField = document.querySelector("#passwordField"); // Corrected selector
const emailFeedBackArea = document.querySelector(".emailFeedBackArea");
const showPasswordBtn = document.querySelector(".showpassWordToggle");
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');
const showpassWordToggle = document.querySelector(".showpassWordToggle");

const handleToggleInput = (e) => {
    if (showPasswordBtn.textContent === 'Show') {
        showPasswordBtn.textContent = 'Hide';  
        passwordField.setAttribute('type', "text");

    } else {
        showPasswordBtn.textContent = 'Show';  
        passwordField.setAttribute('type', "password");
    }
};

showpassWordToggle.addEventListener('click', handleToggleInput);


emailField.addEventListener('keyup',(e)=>{
    const emailVal = e.target.value; 

    emailField.classList.remove('is-invalid');
    emailFeedBackArea.style.display="none";

    if(emailVal.length > 0){
        fetch('/authentication/validate-email',{
            body: JSON.stringify({email : emailVal}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data',data);
            if(data.email_error){
                emailField.classList.add('is-invalid');
                feedBackArea.style.display="block";
                emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`;
            }
        });
    }
})




usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
     
    
    
    usernameField.classList.remove('is-invalid');
    feedBackArea.style.display="none";

    if(usernameVal.length > 0){
        fetch('/authentication/validate-username',{
            body: JSON.stringify({username : usernameVal}),
            method:"POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data',data);
            
            if(data.username_error){
                usernameField.classList.add('is-invalid');
                feedBackArea.style.display="block";
                feedBackArea.innerHTML=`<p>${data.username_error}</p>`;
            }
        });
    }
});
