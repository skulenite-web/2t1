function fetchpost() {
    // Get data
    let data = new URLSearchParams();
    data.append('name', document.getElementById('name').value);
    data.append('uoft', document.getElementById('uoft').value);
    data.append('comment', document.getElementById('comment').value);
    
    // Submit request
    var endpoint = document.getElementById('form-submit-url-endpoint').value;
    fetch(endpoint, {
        method: 'post',
        body: data
    })
    .then(function (response) {
        return response.text();
    })
    .then(function (text) {
        if (text === 'SUCCESS') {
            document.getElementById('form-results-box').innerHTML = "Your review has been submitted! We'll review it and it will appear on the site shortly.";
            document.getElementById('form-results-box').style.opacity = 1;
        } else {
            document.getElementById('form-results-box').innerHTML = "That didn't work. Try resubmitting, and make sure you fill out your name and a comment.";
            document.getElementById('form-results-box').style.opacity = 1;
        }
    })
    .catch(function (error) {
        console.log(error);
    });

    // Clear boxes
    document.getElementById('comment-form').reset();

    return false;
}
