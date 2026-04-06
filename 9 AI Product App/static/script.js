function predict() {

    let data = {
        hours: document.getElementById("hours").value,
        attendance: document.getElementById("attendance").value,
        sleep: document.getElementById("sleep").value,
        assignments: document.getElementById("assignments").value,
        previous: document.getElementById("previous").value
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => {

        document.getElementById("status").innerText = res.status;
        document.getElementById("score").innerText = res.score;

        document.getElementById("risk").innerText = res.risk;
        document.getElementById("grade").innerText = res.grade;

        document.getElementById("bar").style.width = res.score + "%";

        drawChart(data);
    });
}

function drawChart(data){
    new Chart(document.getElementById("chart"), {
        type: 'bar',
        data: {
            labels: ["Hours","Attendance","Sleep","Assignments","Previous"],
            datasets: [{
                data: Object.values(data)
            }]
        }
    });
}