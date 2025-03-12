/* $(document).ready(function() {
    $("#click-me").mouseenter(function() {
        $("th").slideToggle("slow");
    });
    $("#click-me").mouseleave(function() {
        $("th").slideToggle("slow");
    });
});
*/

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("jobAdForm").addEventListener("submit", async function(event) {
        event.preventDefault();  // Förhindrar att formuläret laddar om sidan

        const jobTitle = document.getElementById("jobTitle").value;
        const jobDescription = document.getElementById("jobDescription").value;

        if (!jobTitle || !jobDescription) {
            alert("Please fill in both Job Title and Job Description.");
            return;
        }

        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ jobTitle, jobDescription })
            });

            const result = await response.json();

            if (response.ok) {
                document.getElementById("generatedJobAd").innerText = result.jobAd;
            } else {
                document.getElementById("generatedJobAd").innerText = "Error: " + result.error;
            }
        } catch (error) {
            console.error("Error:", error);
            document.getElementById("generatedJobAd").innerText = "Failed to fetch response.";
        }
    });
});
