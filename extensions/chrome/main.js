chrome.runtime.onMessage.addListener(async request => {
    await fetch(request.API_ENDPOINT, {
        method: "POST",
        body: JSON.stringify({"name": request.title, "link": request.link})
    })
    .then(res => res.json())
    .then(res => res.status == 201 ? console.log("Success") : console.log("Fail"))
    .catch(err => console.error(err));
})