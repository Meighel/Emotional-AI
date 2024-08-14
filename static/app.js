document.getElementById("emotion-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const emotion = document.getElementById("emotion").value;
    const userInput = document.getElementById("user-input").value;

    const responseContainer = document.getElementById("response-text");
    responseContainer.textContent = "Processing...";

    const response = await fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ emotion: emotion, user_input: userInput }),
    });

    const data = await response.json();
    responseContainer.textContent = data.response;
});
