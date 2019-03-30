function generateProgression() {

    var chord1 = document.getElementById("chord1")
    var chord2 = document.getElementById("chord2")
    var chord3 = document.getElementById("chord3")
    var chord4 = document.getElementById("chord4")
    
    var num1 = document.getElementById("num1")
    var num2 = document.getElementById("num2")
    var num3 = document.getElementById("num3")
    var num4 = document.getElementById("num4")

    var key = document.getElementById("key")
    var scale = document.getElementById("scale-major").checked

    num1.value = Math.ceil(Math.random() * 7)
    num2.value = Math.ceil(Math.random() * 7)
    num3.value = Math.ceil(Math.random() * 7)
    num4.value = Math.ceil(Math.random() * 7)

    switch (key) {
        case A:
            break;
        case B:
            break;
        case C:
            break;
        case D:
            break;
        case E:
            break;
        case F:
            break;
        case G:
            break;
    }
}