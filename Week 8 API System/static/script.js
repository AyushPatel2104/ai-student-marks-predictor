document.getElementById("predictionForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const loader = document.getElementById("loader");
    const resultDiv = document.getElementById("result");

    loader.style.display = "block";
    resultDiv.innerHTML = "";

    try {
        const data = {
            age: +document.getElementById("age").value,
            study_hours: +document.getElementById("study_hours").value,
            sleep_hours: +document.getElementById("sleep_hours").value,
            attendance: +document.getElementById("attendance").value,
            assignments: +document.getElementById("assignments").value,
            previous_score: +document.getElementById("previous_score").value
        };

        const response = await fetch("/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const result = await response.json();

        loader.style.display = "none";

        if (result.error) {
            resultDiv.innerHTML = `<p style="color:red;">❌ Error: ${result.error}</p>`;
            return;
        }

        resultDiv.innerHTML = `
            <h3>📊 Performance: ${result.performance}</h3>
            <h4>⚠️ Risk Level: ${result.risk_level}</h4>
            <h4>📈 Score: ${result.predicted_score}</h4>
            <p>🧠 ${result.description}</p>
            <p>💡 ${result.suggestion}</p>
            <p>📌 ${result.tips}</p>
        `;

    } catch (err) {
        loader.style.display = "none";
        resultDiv.innerHTML = `<p style="color:red;">❌ Something went wrong!</p>`;
    }
});

/* 🔥 3D EFFECT */

const card = document.getElementById("card");

document.addEventListener("mousemove", (e) => {
    let x = (window.innerWidth / 2 - e.pageX) / 25;
    let y = (window.innerHeight / 2 - e.pageY) / 25;
    card.style.transform = `rotateY(${x}deg) rotateX(${y}deg)`;
});