
// paymentDay description
let fixedForm = `

    <label for="paymentDay">Payment day: </label>
    <input name="paymentDay" type="text" placeholder="Day of the mounth you pay">

    <br><br>

    <label for="description">description: </label>
    <textarea name="description" form="form_id" placeholder="Your's expense description"></textarea>
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


document.addEventListener('DOMContentLoaded', function() {
    var type = document.getElementById("expenseType");
    var form = document.getElementById("specificForm");

    if (type.value === "variable" || type.value === "fixed"){
        form.innerHTML = expenseForm[type.value];
    } 

    type.addEventListener('change', function(){       
        form.innerHTML = expenseForm[type.value];   
    })

})