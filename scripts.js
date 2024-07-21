
document.addEventListener("DOMContentLoaded", function () {
    const editor = CodeMirror.fromTextArea(document.getElementById("editor), {
        mode: "text/x-c++src",
        lineNumbers: true
    });

    document.getElementById("execute").addEventListener("click", function () {
        const code = editor.getValue();
        fetch("/run_code", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ code })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").innerText = data.output;
        });
    });
});
