var order = ['ALARMING', 'BROS_BEFORE_FOES','BUBBLE_COURT','BUSINESS_CARDS','JUST_A_TREE'];
var index = 0;

function checkName(name) {
    return name == document.getElementById('sketch-dropdown').innerHTML;
}

function switchSketch(sketch) {
    if (sketch === 'next') {
        // Hide old sketch
        document.getElementById(order[index]).classList.toggle('d-none');

        // Update index
        index = index + 1;
        if (index === order.length) {
            index = 0;
        }
        
        // Show new sketch and update sketch title
        document.getElementById(order[index]).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = order[index];

    } else if (sketch === 'prev') {
        // Hide old sketch
        document.getElementById(order[index]).classList.toggle('d-none');
        console.log('hiding index == ', index);
        
        // Update index
        index = index - 1;
        if (index === -1) {
            index = order.length-1;
        }

        // Show new sketch and update sketch title
        document.getElementById(order[index]).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = order[index];

    } else {
        // Hide old sketch
        document.getElementById(order[index]).classList.toggle('d-none');

        console.log('trying to show sketch: ', sketch);
        // Show new sketch and update sketch title
        document.getElementById(sketch).classList.toggle('d-none');
        document.getElementById('sketch-dropdown').innerHTML = sketch;

        // Update index
        index = order.findIndex(checkName);
    }
}
