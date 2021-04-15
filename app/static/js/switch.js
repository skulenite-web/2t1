var sketches = ['ALARMING', 'BROS_BEFORE_FOES','BUBBLE_COURT','BUSINESS_CARDS','JUST_A_TREE'];
var sketches_display = ['ALARMING', 'BROS BEFORE FOES','BUBBLE COURT','BUSINESS CARDS','JUST A TREE'];
var index = 0;

function checkName(name) {
    return name == document.getElementById('sketch-dropdown').innerHTML;
}

function switchSketch(sketch, sketch_display) {
    if (sketch === 'next') {
        // Hide old sketch
        document.getElementById(sketches[index]).classList.toggle('d-none');

        // Update index
        index = index + 1;
        if (index === sketches.length) {
            index = 0;
        }
        
        // Show new sketch and update sketch title
        document.getElementById(sketches[index]).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = sketches_display[index];

    } else if (sketch === 'prev') {
        // Hide old sketch
        document.getElementById(sketches[index]).classList.toggle('d-none');
        console.log('hiding index == ', index);
        
        // Update index
        index = index - 1;
        if (index === -1) {
            index = sketches.length-1;
        }

        // Show new sketch and update sketch title
        document.getElementById(sketches[index]).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = sketches_display[index];

    } else {
        // Hide old sketch
        document.getElementById(sketches[index]).classList.toggle('d-none');

        // Show new sketch and update sketch title
        document.getElementById(sketch).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = sketch_display;

        // Update index
        index = sketches_display.findIndex(checkName);
    }
}
