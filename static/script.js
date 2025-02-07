/* $(document).ready(function() {
    $("#click-me").mouseenter(function() {
        $("th").slideToggle("slow");
    });
    $("#click-me").mouseleave(function() {
        $("th").slideToggle("slow");
    });
});
*/

document.getElementById("jobAdForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const title = document.getElementById("jobTitle").value;
    const description = document.getElementById("jobDescription").value;

    const response = await fetch("http://127.0.0.1:8000/jobad-generator.html", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, description }),
    });

    const data = await response.json();
    document.getElementById("jobAdOutput").innerText = data.generatedText || "Something went wrong.";
});