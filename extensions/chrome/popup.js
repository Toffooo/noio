document.addEventListener("DOMContentLoaded", () => {
    const sendLink = async () => {
        chrome.tabs.query(
            {currentWindow: true, active: true},
            tabs => {
                chrome.tabs.sendMessage(tabs[0].id, {
                    "API_ENDPOINT": "http://localhost:8000/api/v1/notices",
                    "title": tabs[0].title,
                    "link": tabs[0].url,
                    "tab": tabs[0]
                });
            }
        );
    }

    document.querySelector('button').addEventListener('click', sendLink, false);
}, false);