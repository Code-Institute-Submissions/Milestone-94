// function from stackoverflow
function truncateText(selector, maxLength) {
    let element = document.querySelector(selector),
        truncated = element.innerText;

    if (truncated.length > maxLength) {
        truncated = truncated.substr(0,maxLength) + '...';
    }
    return truncated;
}
//calling the truncateText function
document.querySelector('.card-text').innerText = truncateText('.card-text', 107);