$(document).ready(function () {

    // 1. Text Animation (Textillate) - Purana code
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" }
    });

    // 2. Mic Button Click Event
    // Jab aap mic par click karenge, ye Python ke 'allCommands' function ko trigger karega
    $("#MicBtn").click(function () {
        // UI par feedback dene ke liye text change karein
        $(".animate-text").text("Listening...");
        
        // Eel ke zariye Python function call
        eel.allCommands()(); 
    });

    // 3. Enter Key support for Chatbox
    // Agar aap type karke 'Enter' dabayein toh bhi Jarvis respond kare
    $("#chatbox").keypress(function (e) {
        if (e.which == 13) {
            let text = $("#chatbox").val();
            if (text.trim() !== "") {
                eel.allCommands(text)(); // Text input ke saath function call
                $("#chatbox").val(""); // Input clear karein
            }
        }
    });

});

// 4. Python se Messages Receive karna
// Ye function Python (main.py) call karega UI par text dikhane ke liye
eel.expose(displayMessage);
function displayMessage(message) {
    // Textillate animation ko update karne ke liye
    $(".animate-text").text(message);
    
    // Agar aap chahte hain ki text hile (animate ho) toh ye line use karein:
    $('.text').textillate('start');
}