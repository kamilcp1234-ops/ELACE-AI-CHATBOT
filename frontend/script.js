const chatContainer = document.getElementById("chat-messages");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const loadingIndicator = document.getElementById("loading-indicator");


function scrollToBottom() {
    chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: "smooth"
    });
}


async function handleSendMessage(event) {

    if (event) {
        event.preventDefault();
    }

    const question = userInput.value.trim();

    if (!question) {
        return;
    }

    // Show user message
    appendUserMessage(question);

    // Clear input
    userInput.value = "";

    // Show Thinking...
    showLoading(true);

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/ask?query=${encodeURIComponent(question)}`
        );

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();

        const answerText =
            data.answer ||
            "Sorry, I could not find enough information to answer that question.";

        // Hide Thinking...
        showLoading(false);

        // Show AI answer
        appendAiMessage(answerText);

    } catch (error) {

        console.error("API Error:", error);

        showLoading(false);

        appendAiMessage(
            "Sorry, I couldn't get a response right now. Please try again."
        );
    }

    userInput.focus();
}


function appendUserMessage(text) {

    const wrapper = document.createElement("div");

    wrapper.className = "flex justify-end";

    const bubble = document.createElement("div");

    bubble.className =
        "max-w-[85%] bg-slate-900 text-white rounded-2xl rounded-tr-sm px-4 py-2.5 text-sm leading-relaxed shadow-xs";

    bubble.textContent = text;

    wrapper.appendChild(bubble);

    chatContainer.insertBefore(
        wrapper,
        loadingIndicator
    );

    scrollToBottom();
}


function appendAiMessage(text) {

    const wrapper = document.createElement("div");

    wrapper.className =
        "flex items-start gap-2.5";

    // AI avatar
    const avatar = document.createElement("div");

    avatar.className =
        "w-7 h-7 rounded-lg bg-sky-100 text-sky-700 flex items-center justify-center flex-shrink-0 text-xs font-bold mt-0.5 border border-sky-200/70 select-none";

    avatar.textContent = "AI";


    // AI message box
    const card = document.createElement("div");

    card.className =
        "message-content max-w-[85%] bg-white text-slate-800 border border-slate-200/80 rounded-2xl rounded-tl-sm px-4 py-3 text-sm leading-relaxed shadow-xs";


    // Convert Markdown to proper HTML
    if (typeof marked !== "undefined") {
        card.innerHTML = marked.parse(text);
    } else {
        card.textContent = text;
    }


    wrapper.appendChild(avatar);
    wrapper.appendChild(card);


    chatContainer.insertBefore(
        wrapper,
        loadingIndicator
    );

    scrollToBottom();
}


function showLoading(show) {

    if (show) {

        loadingIndicator.classList.remove("hidden");

        sendButton.disabled = true;

    } else {

        loadingIndicator.classList.add("hidden");

        sendButton.disabled = false;
    }

    scrollToBottom();
}


// Send button
sendButton.addEventListener("click", function(event) {

    event.preventDefault();

    handleSendMessage(event);

});


// Form submit
chatForm.addEventListener("submit", function(event) {

    event.preventDefault();

    handleSendMessage(event);

});


