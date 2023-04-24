const input = document.querySelector("#search");
input.addEventListener('keyDown', function(event) {
    if(event.key == "Enter") {
        document.querySelector("form").submit();
    }
})