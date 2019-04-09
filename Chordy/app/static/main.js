var chords = [
    ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'], //C
    ['C#', 'D#m', 'Fm', 'F#', 'G#', 'A#m', 'Cdim'], //C#
    ['D', 'Em', 'F#m', 'G', 'A', 'Bm', 'C#dim'], //D
    ['D#', 'Fm', 'Gm', 'G#', 'A#', 'Cm', 'Ddim'], //D#
    ['E', 'F#m', 'G#m', 'A', 'B', 'C#m', 'D#dim'], //E
    ['F', 'Gm', 'Am', 'A#', 'C', 'Dm', 'Edim'], //F
    ['F#', 'G#m', 'A#m', 'B', 'C#', 'D#m', 'Fdim'], //F#
    ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'F#dim'], //G
    ['G#', 'A#m', 'Cm', 'C#', 'D#', 'Fm', 'Gdim'], //G#
    ['A', 'Bm', 'C#m', 'D', 'E', 'F#m', 'G#dim'], //A
    ['A#', 'Cm', 'Dm', 'D#', 'F', 'Gm', 'Adim'], //A#
    ['B', 'C#m', 'D#m', 'E', 'F#', 'G#m', 'A#dim'], //B
];

var chord1 = document.getElementById("chord1")
var chord2 = document.getElementById("chord2")
var chord3 = document.getElementById("chord3")
var chord4 = document.getElementById("chord4")

var num1 = document.getElementById("num1")
var num2 = document.getElementById("num2")
var num3 = document.getElementById("num3")
var num4 = document.getElementById("num4")

function generateProgression() {

    var key = document.getElementById("key")
    var sharp = document.getElementById("sharp").checked
    num1.value = Math.ceil(Math.random() * 7)
    num2.value = Math.ceil(Math.random() * 7)
    num3.value = Math.ceil(Math.random() * 7)
    num4.value = Math.ceil(Math.random() * 7)

    switch (key.value) {
        case "C":
            if (!sharp) {
                chord1.value = chords[0][num1.value-1]
                chord2.value = chords[0][num2.value-1]
                chord3.value = chords[0][num3.value-1]
                chord4.value = chords[0][num4.value-1]
            } else {
                chord1.value = chords[1][num1.value-1]
                chord2.value = chords[1][num2.value-1]
                chord3.value = chords[1][num3.value-1]
                chord4.value = chords[1][num4.value-1]
            }
            break;
        case "D":
            if (!sharp) {
                chord1.value = chords[2][num1.value-1]
                chord2.value = chords[2][num2.value-1]
                chord3.value = chords[2][num3.value-1]
                chord4.value = chords[2][num4.value-1]
            } else {
                chord1.value = chords[3][num1.value-1]
                chord2.value = chords[3][num2.value-1]
                chord3.value = chords[3][num3.value-1]
                chord4.value = chords[3][num4.value-1]
            }
            break;
        case "E":
            if (!sharp) {
                chord1.value = chords[4][num1.value-1]
                chord2.value = chords[4][num2.value-1]
                chord3.value = chords[4][num3.value-1]
                chord4.value = chords[4][num4.value-1]
            } else {
                chord1.value = chords[5][num1.value-1]
                chord2.value = chords[5][num2.value-1]
                chord3.value = chords[5][num3.value-1]
                chord4.value = chords[5][num4.value-1]
            }
            break;
        case "F":
            if (!sharp) {
                chord1.value = chords[5][num1.value-1]
                chord2.value = chords[5][num2.value-1]
                chord3.value = chords[5][num3.value-1]
                chord4.value = chords[5][num4.value-1]
            } else {
                chord1.value = chords[6][num1.value-1]
                chord2.value = chords[6][num2.value-1]
                chord3.value = chords[6][num3.value-1]
                chord4.value = chords[6][num4.value-1]
            }
            break;
        case "G":
            if (!sharp) {
                chord1.value = chords[7][num1.value-1]
                chord2.value = chords[7][num2.value-1]
                chord3.value = chords[7][num3.value-1]
                chord4.value = chords[7][num4.value-1]
            } else {
                chord1.value = chords[8][num1.value-1]
                chord2.value = chords[8][num2.value-1]
                chord3.value = chords[8][num3.value-1]
                chord4.value = chords[8][num4.value-1]
            }
            break;
        case "A":
            if (!sharp) {
                chord1.value = chords[9][num1.value-1]
                chord2.value = chords[9][num2.value-1]
                chord3.value = chords[9][num3.value-1]
                chord4.value = chords[9][num4.value-1]
            } else {
                chord1.value = chords[10][num1.value-1]
                chord2.value = chords[10][num2.value-1]
                chord3.value = chords[10][num3.value-1]
                chord4.value = chords[10][num4.value-1]
            }
            break;
        case "B":
            if (!sharp) {
                chord1.value = chords[11][num1.value-1]
                chord2.value = chords[11][num2.value-1]
                chord3.value = chords[11][num3.value-1]
                chord4.value = chords[11][num4.value-1]
            } else {
                chord1.value = chords[0][num1.value-1]
                chord2.value = chords[0][num2.value-1]
                chord3.value = chords[0][num3.value-1]
                chord4.value = chords[0][num4.value-1]
            }
            break;
    }
}