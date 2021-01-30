

function cleanData(array){

    var output = [];

    for(var i=0; i < array.length; i++){
        let a = array[i].split("-");
        a.shift();
        a.pop();
        output.push(a);
    }
    return output;
}

function getMonthlyExpense(fixed, variable){
    console.log("passou");
    console.log(fixed.length);


    //Get monthy on fixed
    var fixedSum = 0;
    for(var i=0; i < fixed.length; i++){
        fixedSum = fixedSum + parseFloat(fixed[i][0]);
        //console.log(fixed[i]);
    };

    console.log("passou", fixedSum);
    
    //Get monthly on var
    var variableSum = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0};
    for(var i=0; i < variable.length; i++){
        variableSum[parseInt(variable[i][3])] += + parseFloat(variable[i][0]);
    }
    return {
        "fixed": fixedSum,
        "variable": Object.values(variableSum)
    };
}




function graphClickEvent(event, array){
    console.log("teste");
    console.log("event: ", event);
    console.log("array", array);

}



document.addEventListener("DOMContentLoaded", function(){

    var fixedExpenses = cleanData(fixedExpensesRaw.split(","));
    var variableExpenses = cleanData(variableExpensesRaw.split(","));

    console.log("fix: ", fixedExpenses);
    console.log("var: ", variableExpenses);

    var expensesData = getMonthlyExpense(fixedExpenses, variableExpenses);

    console.log(expensesData);


    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
    
        // The data for our dataset
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [{
                label: 'Fixed Expense',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 255, 255)',
                data: Array(12).fill(expensesData.fixed)
            },
            {
                label: 'Variable Expense',
                backgroundColor: 'rgb(13, 109, 52)',
                borderColor: 'rgb(255, 255, 255)',
                data: expensesData.variable
            }
            

        ]
        },
    
        // Configuration options go here
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                  stacked: true,
                }],
                yAxes: [{
                  stacked: true
                }]
              },
            onClick: graphClickEvent
        }
    });
    
    chart.canvas.style.backgroundColor = 'rgba(255,255,255)';



});