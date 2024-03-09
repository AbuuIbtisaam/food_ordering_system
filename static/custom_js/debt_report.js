document.addEventListener("DOMContentLoaded", function() {
    const timePeriodSelect = document.getElementById("time_period");
    const customFields = document.getElementById("custom_fields");

    timePeriodSelect.addEventListener("change", function() 
    {
        const selectedOption = timePeriodSelect.options[timePeriodSelect.selectedIndex].value;
        customFields.style.display = selectedOption === "custom" ? "block" : "none";
    });
});