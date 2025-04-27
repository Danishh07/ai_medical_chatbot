const API_URL = "http://127.0.0.1:8000/chat"; // Local API endpoint
const session_id = "user_" + Math.floor(Math.random() * 1000); // Temporary user session

// Toggle chatbot UI
function toggleChat() {
    const chatWidget = document.querySelector(".chatbot-widget");
    const chatButton = document.querySelector(".chatbot-button");

    if (chatWidget.style.display === "none" || chatWidget.style.display === "") {
        chatWidget.style.display = "block"; // Show chatbot
        chatButton.style.display = "none"; // Hide chat icon
    } else {
        chatWidget.style.display = "none"; // Hide chatbot
        chatButton.style.display = "block"; // Show chat icon again
    }
}

// Append message to chatbox
function appendMessage(role, text) {
    const chatBox = document.getElementById("chatBox");
    const msg = document.createElement("div");

    // Apply different classes for user and bot messages
    msg.classList.add(role === "You" ? "user-message" : "bot-message");

    msg.innerHTML = `<strong>${role}:</strong> ${text}`;
    chatBox.appendChild(msg);
    
    // Ensure the chat scrolls to the latest message
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Send message to backend
async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim(); 

    if (!text) return;

    appendMessage("You", text);
    input.value = ""; // Clear input field

    try {
        const res = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" }, 
            body: JSON.stringify({ session_id, query: text }),
        });

        const data = await res.json(); 
        appendMessage("Bot", data.response);
    } catch (err) {
        appendMessage("Bot", "Oops! Something went wrong.");
    }
}

// Attach event listener to "Send" button
document.getElementById("sendBtn").addEventListener("click", sendMessage);

// Allow sending message on pressing 'Enter'
document.getElementById("userInput").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // ⛔ Stop form from submitting
        sendMessage();
    }
});

