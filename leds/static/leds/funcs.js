var currentColorButton = null;
var currentColorJSON = null;

function changeCurrentColor(elem, color_json) {
    var color = JSON.parse(color_json)[0].fields;
    var r = color.r;
    var g = color.g;
    var b = color.b;

    if(elem == currentColorButton){
        currentColorButton = null;
        currentColorJSON = null;
        elem.style.backgroundColor = "gray";
        console.log("no color button");
    } else {
        if (null != currentColorButton){
            currentColorButton.style.backgroundColor = "gray";
        }
        currentColorButton = elem;
        currentColorJSON = color;
        elem.style.backgroundColor = toRGB_rgb(color.r, color.g, color.b);

        console.log("new color button");
    }
}

function changeLEDColor(elem) {
    if(null == currentColorButton){
        // white
        elem.style.backgroundColor = toRGB_rgb(255, 255, 255);

        console.log("no color selected");
    } else {
        // color
        elem.style.backgroundColor = toRGB_json(currentColorJSON);

        console.log("change led color");
    }

    // check if LED color == selected color
}


function toRGB_json(color_json){
    ret = "rgb(" + color_json.r + ", " + color_json.g + ", " + color_json.b + ")";
    console.log(ret);
    return ret;
}

function toRGB_rgb(r, g, b){
    ret = "rgb(" + r.toString() + ", " + g.toString() + ", " + b.toString() + ")";
    return ret;
}
