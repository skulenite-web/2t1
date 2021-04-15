var sketches = ['MEETING_OF_THE_MINDS', 'BROS_BEFORE_FOES', 'ALARMING', 'LETTER_BY_LETTER', 'BUBBLE_COURT', 'MOOOOOM', 'JUST_A_TREE', 'BUSINESS_CARDS']
var sketches_display = ['MEETING OF THE MINDS', 'BROS BEFORE FOES', 'ALARMING', 'LETTER BY LETTER', 'BUBBLE COURT', 'MOOOOOM', 'JUST A TREE', 'BUSINESS CARDS']
var index = 0;

var songs = ['A_SKULE_NITE_FROM_YOUR_COUCH', 'LIFE_IN_QUARANTINE', 'INVESTIGATION_489:_EIGHTEEN_PI_SQUARED', 'THATS_ENGINEERING_BABY']
var songs_display = ['A SKULE NITE (FROM YOUR COUCH)', 'LIFE IN QUARANTINE', 'INVESTIGATION 489: EIGHTEEN PI SQUARED', "THAT'S ENGINEERING, BABY!"]
var song_index = 0

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

function switchSong(song, song_display) {
    if (song === 'next') {
        // Hide old sketch
        document.getElementById(songs[song_index]).classList.toggle('d-none');

        // Update index
        song_index = song_index + 1;
        if (song_index === songs.length) {
            song_index = 0;
        }
        
        // Show new sketch and update sketch title
        document.getElementById(songs[song_index]).classList.toggle('d-none');
        document.getElementById('song-dropdown').innerHTML = songs_display[song_index];

    } else if (song === 'prev') {
        // Hide old sketch
        document.getElementById(songs[song_index]).classList.toggle('d-none');
        console.log('hiding index == ', song_index);
        
        // Update index
        song_index = song_index - 1;
        if (song_index === -1) {
            song_index = songs.length-1;
        }

        // Show new sketch and update sketch title
        document.getElementById(songs[song_index]).classList.toggle('d-none');
        document.getElementById('song-dropdown').innerHTML = songs_display[song_index];

    } else {
        // Hide old sketch
        document.getElementById(songs[song_index]).classList.toggle('d-none');

        // Show new sketch and update sketch title
        document.getElementById(song).classList.toggle('d-none');
        document.getElementById('song-dropdown').innerHTML = song_display;

        // Update index
        song_index = songs_display.findIndex(checkName);
    }
}
