
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
    <label for="duration"> Forever</label><br>
`;

//categorie 
let variableForm = `

    <label for="categorie">Categorie: </label>
    <input name="categorie" type="text" placeholder="Your's expense Categorie">
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
    })

})