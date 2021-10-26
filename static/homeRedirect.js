let timer = 6; // seconds

function redirect() {

    if (timer <=0) window.location = "/"; // redirects to index
    else timer--; setTimeout("redirect()", 1000) // sleeps 1 sec and decrements the timer

}
