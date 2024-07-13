const canvas = document.getElementById('patternCanvas');
const context = canvas.getContext('2d');
let patternType = 'spirograph'; // Default pattern type
let patternColor = '#ff0000'; // Default pattern color
let patternSize = 100; // Default pattern size
let patternSpeed = 1; // Default pattern speed

function clearCanvas() {
    context.clearRect(0, 0, canvas.width, canvas.height);
}

function savePattern() {
    const dataUrl = canvas.toDataURL();
    localStorage.setItem('savedPattern', dataUrl);
}

function loadPattern() {
    const savedPattern = localStorage.getItem('savedPattern');
    if (savedPattern) {
        const img = new Image();
        img.onload = () => {
            context.drawImage(img, 0, 0);
        };
        img.src = savedPattern;
    } else {
        alert('No saved pattern found.');
    }
}

function generatePattern() {
    clearCanvas();
    context.strokeStyle = patternColor;
    context.lineWidth = 2;

    if (patternType === 'spirograph') {
        // Example Spirograph pattern
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const numCircles = 20;
        const angleIncrement = 0.1;
        const radiusIncrement = 2;

        context.beginPath();
        for (let i = 0; i < numCircles; i++) {
            const angle = i * angleIncrement * patternSpeed;
            const radius = patternSize * (i + 1) * radiusIncrement;

            const x = centerX + Math.cos(angle) * radius;
            const y = centerY + Math.sin(angle) * radius;

            if (i === 0) {
                context.moveTo(x, y);
            } else {
                context.lineTo(x, y);
            }
        }
        context.stroke();
        context.closePath();
    } else if (patternType === 'grid') {
        // Example grid pattern
        const gridSize = 20;
        const numColumns = Math.floor(canvas.width / gridSize);
        const numRows = Math.floor(canvas.height / gridSize);

        for (let i = 0; i < numColumns; i++) {
            for (let j = 0; j < numRows; j++) {
                context.fillRect(i * gridSize, j * gridSize, gridSize, gridSize);
            }
        }
    }
    // Add more pattern types here

}

// Event listeners
document.getElementById('clearCanvas').addEventListener('click', clearCanvas);
document.getElementById('savePattern').addEventListener('click', savePattern);
document.getElementById('loadPattern').addEventListener('click', loadPattern);
document.getElementById('generatePattern').addEventListener('click', generatePattern);

// Additional options
const sizeSlider = document.getElementById('patternSize');
sizeSlider.addEventListener('input', function() {
    patternSize = parseInt(this.value);
    generatePattern();
});

const speedSlider = document.getElementById('patternSpeed');
speedSlider.addEventListener('input', function() {
    patternSpeed = parseFloat(this.value);
    generatePattern();
});

const colorPicker = document.getElementById('patternColor');
colorPicker.addEventListener('input', function() {
    patternColor = this.value;
    generatePattern();
});

const typeSelector = document.getElementById('patternType');
typeSelector.addEventListener('change', function() {
    patternType = this.value;
    generatePattern();
});

console.log('Pattern generator initialized.');
