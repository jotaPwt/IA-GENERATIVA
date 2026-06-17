function calculateTime() {
    const initial = parseFloat(document.getElementById('initial-investment').value);
    const monthly = parseFloat(document.getElementById('monthly-investment').value);
    const target = parseFloat(document.getElementById('target-value').value);
    const annualRate = parseFloat(document.getElementById('annual-rate').value);

    if (isNaN(initial) || isNaN(monthly) || isNaN(target) || isNaN(annualRate)) {
        alert("Por favor, preencha todos os parâmetros quantitativos.");
        return;
    }

    const monthlyRate = (Math.pow(1 + (annualRate / 100)), 1/12) - 1; // Taxa mensal equivalente
    let currentBalance = initial;
    let months = 0;

    // Proteção contra loops infinitos caso a taxa e aportes sejam zero
    if (monthly <= 0 && annualRate <= 0 && initial < target) {
        document.getElementById('result-text').innerText = "Alvo inalcançável com os parâmetros atuais.";
        return;
    }

    while (currentBalance < target) {
        currentBalance += monthly;
        currentBalance *= (1 + (annualRate / 100) / 12); // Aproximação linear mensal juros compostos
        months++;
        
        // Limite de salvaguarda (100 anos)
        if (months > 1200) break;
    }

    const years = (months / 12).toFixed(1);
    const resultDisplay = document.getElementById('result-display');
    const resultText = document.getElementById('result-text');

    resultDisplay.classList.remove('hidden');
    
    if (months > 1200) {
        resultText.innerText = `Prazo superior a 100 anos. Considere aumentar os aportes ou reavaliar a taxa.`;
    } else {
        resultText.innerHTML = `Para atingir o objetivo de <span style="color:#39ff14">$${target.toLocaleString()}</span>:<br><br>
        Tempo estimado: <span style="color:#8a2be2">${months} meses</span> (~${years} anos).<br>
        Aporte total investido: $${(initial + (monthly * months)).toLocaleString()}`;
    }
}