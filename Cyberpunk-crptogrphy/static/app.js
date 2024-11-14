async function hashText() {
    const text = document.getElementById("hash-text").value;
    const algorithm = document.getElementById("hash-algorithm").value;

    const response = await fetch('/hash/calculate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, algorithm })
    });
    const data = await response.json();
    document.getElementById("hash-result").textContent = data.result || "Error";
}

async function base64Encode() {
    const text = document.getElementById("base64-text").value;

    const response = await fetch('/base64/encode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const data = await response.json();
    document.getElementById("base64-result").textContent = data.result || "Error";
}

async function base64Decode() {
    const encodedText = document.getElementById("base64-text").value;

    const response = await fetch('/base64/decode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ encoded_text: encodedText })
    });
    const data = await response.json();
    document.getElementById("base64-result").textContent = data.result || "Error";
}
