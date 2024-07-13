const canvas = document.getElementById('patternCanvas');
const ctx = canvas.getContext('2d');

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function savePattern() {
    const dataUrl = canvas.toDataURL(); // Get image data as base64 URL
    localStorage.setItem('savedPattern', dataUrl); // Store in localStorage
}

function loadPattern() {
    const savedPattern = localStorage.getItem('savedPattern');
    if (savedPattern) {
        const img = new Image();
        img.onload = () => {
            ctx.drawImage(img, 0, 0);
        };
        img.src = savedPattern;
    } else {
        alert('No saved pattern found.');
    }
}

document.getElementById('clearCanvas').addEventListener('click', clearCanvas);
document.getElementById('savePattern').addEventListener('click', savePattern);
document.getElementById('loadPattern').addEventListener('click', loadPattern);

console.log('Pattern generator initialized.');
