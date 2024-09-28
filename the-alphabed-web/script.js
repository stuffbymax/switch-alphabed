function shiftLetter(letter, shift) {
    const code = letter.charCodeAt(0);
    let base = (code >= 65 && code <= 90) ? 65 : (code >= 97 && code <= 122) ? 97 : null;

    if (base !== null) {
        return String.fromCharCode(((code - base + shift) % 26) + base);
    } else {
        return letter;  // Non-alphabetic characters are not shifted
    }
}

function encodeMessage(message, shift) {
    return message.split('').map(char => shiftLetter(char, shift)).join('');
}

function encode() {
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = encodeMessage(message, shift);
    document.getElementById('result').textContent = `Encoded: ${result}`;
}

function decode() {
    const message = document.getElementById('message').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = encodeMessage(message, -shift);
    document.getElementById('result').textContent = `Decoded: ${result}`;
}
