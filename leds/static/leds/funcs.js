var currentColorButton = null;
var R = 0;
var G = 0;
var B = 0;

function changeCurrentColor(elem, color_json) {
    var color = JSON.parse(color_json)[0].fields;
    var r = color.r;
    var g = color.g;
    var b = color.b;

    if(elem == currentColorButton){
        currentColorButton = null;
        elem.style.backgroundColor = "gray";
        R = 0;
        G = 0;
        B = 0;
        console.log("no color button");
    } else {
        if (null != currentColorButton){
            currentColorButton.style.backgroundColor = "gray";
        }
        currentColorButton = elem;
        R = r;
        G = g;
        B = b;
        elem.style.backgroundColor = toRGB_rgb(r, g, b);

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
        elem.style.backgroundColor = toRGB_rgb(R, G, B);

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
