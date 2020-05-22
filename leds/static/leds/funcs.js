var currentColorButton = null;

function changeColor(elem, r, g, b) {

    if(elem == currentColorButton){
        elem.style.backgroundColor = "gray";
        currentColorButton = null;
        console.log("no color button");
    } else {
        if (null != currentColorButton){
            currentColorButton.style.backgroundColor = "gray";
        }
        currentColorButton = elem;
        color = toRGB(r, g, b);
        elem.style.backgroundColor = color;

        console.log("new color button");
    }
}

function toRGB(r, g, b){
    ret = "rgb(" + r.toString() + ", " + g.toString() + ", " + b.toString() + ")";
    return ret;
}
