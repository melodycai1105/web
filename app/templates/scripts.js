function selectOnlyThis(id) {
    for (var i = 1;i <= 3; i++)
    {
        document.getElementById("Check" + i).checked = false;
    }
    document.getElementById(id).checked = true;
}

function selectOnlyOne(id) {
    for (var i = 1;i <= 4; i++)
    {
        document.getElementById("Sel" + i).checked = false;
    }
    document.getElementById(id).checked = true;
}