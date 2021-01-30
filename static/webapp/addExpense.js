
// paymentDay description
let fixedForm = `

    <label for="paymentDay">Payment day: </label>
    <input name="paymentDay" type="text" placeholder="Day of the mounth you pay">

    <br><br>

    <label for="description">description: </label>
    <textarea name="description" placeholder="Your's expense description"></textarea>

    <br><br>

    <label for="duration">Duration in months:</label>
    <input type="number" id="duration" name="duration" min="1">

    <input type="checkbox" id="durationForever" name="duration" value="-1">
    <label for="duration"> Forever</label>
    
    <br><br>
    
    <div>
        <label for="warnViaEmail">Remember me via email: </label>
        <input type="checkbox" id="warnViaEmail" name="warnViaEmail" checked>
    </div>

    <div>
        <label for="warnViaSMS">Remember me via SMS: </label>
        <input type="checkbox" id="warnViaSMS" name="warnViaSMS" checked>
    </div>
    <br><br>
`;

//categorie 
let variableForm = `

    <label for="categorie">Categorie: </label>
    <input name="categorie" type="text" placeholder="Your's expense Categorie">
    <br><br>
`

var expenseForm = {
    "fixed": fixedForm,
    "variable": variableForm
};

function checkboxIteration(){
    var durationInput = document.getElementById("duration");
    var durationForever = document.getElementById("durationForever");
    durationForever.addEventListener('change', function(){
    
        if (this.checked){
            durationInput.disabled = true;
            durationInput.setAttribute("type", "hidden");
        }
        else{
            durationInput.disabled = false;
            durationInput.setAttribute("type", "number");

        }
    });
}


document.addEventListener('DOMContentLoaded', function() {
    var type = document.getElementById("expenseType");
    var form = document.getElementById("specificForm");

    if (type.value === "variable" || type.value === "fixed"){
        form.innerHTML = expenseForm[type.value];
    } 
    

    type.addEventListener('change', function(){       
        form.innerHTML = expenseForm[type.value];   
        if (type.value === "fixed"){
            console.log("entrou")
            checkboxIteration();  

        }
    });

    var today = document.getElementById("today");
    today.onchange = function () {
        let date = document.getElementById("date");
        if (today.checked === true){
            date.disabled = true;
            date.value = null;
        }
        else{
            date.disabled = false;
        }
    };

})