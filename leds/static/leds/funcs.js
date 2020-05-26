var currentColorButton = null;
var R = 0;
var G = 0;
var B = 0;

function changeCurrentColor(elem, r, g, b) {

    if(elem == currentColorButton){
        elem.style.backgroundColor = "gray";
        currentColorButton = null;
        console.log("no color button");
    } else {
        if (null != currentColorButton){
            currentColorButton.style.backgroundColor = "gray";
        }
        currentColorButton = elem;
        R = r;
        G = g;
        B = b;
        color = toRGB(r, g, b);
        elem.style.backgroundColor = color;

        console.log("new color button");
    }
}

function changeLEDColor(elem) {
    elem.style.backgroundColor = toRGB(R, G, B);
    console.log("change led color")
}

function toRGB(r, g, b){
    ret = "rgb(" + r.toString() + ", " + g.toString() + ", " + b.toString() + ")";
    return ret;
}
