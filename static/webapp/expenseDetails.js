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


    checkboxIteration(); 


});