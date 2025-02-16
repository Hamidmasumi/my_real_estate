alert("فایل script.js با موفقیت لود شد!");
function toggleDropdown(dropdownId) {
    var dropdown = document.getElementById(dropdownId);
    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}

function closeDropdown(dropdownId) {
    document.getElementById(dropdownId).style.display = "none";
}
