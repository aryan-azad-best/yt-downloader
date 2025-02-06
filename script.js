function downloadVideo() {
    let url = document.getElementById("url").value;
    let format = document.getElementById("format").value;
    let status = document.getElementById("status");

    if (!url) {
        status.innerHTML = "Please enter a YouTube URL!";
        return;
    }

    status.innerHTML = "Downloading...";

    fetch(`https://your-app.onrender.com/download?url=${encodeURIComponent(url)}&format=${format}`)
        .then(response => response.json())
        .then(data => {
            if (data.file) {
                status.innerHTML = `<a href="downloads/${data.file}" download>Click here to download</a>`;
            } else {
                status.innerHTML = "Download failed.";
            }
        })
        .catch(error => {
            status.innerHTML = "Error: " + error;
        });
}
