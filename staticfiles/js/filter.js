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

// نمایش/مخفی کردن فیلترها در موبایل
document.addEventListener("DOMContentLoaded", function () {
    const filterBtn = document.getElementById("filter-btn");
    const searchBox = document.getElementById("search-box");
    const closeBtn = document.querySelector(".filter-close"); // دکمه بستن فیلترها
    const applyFiltersBtn = document.getElementById("applyFilters"); // دکمه اعمال فیلترها

    if (filterBtn && searchBox) {
        filterBtn.addEventListener("click", function () {
            searchBox.classList.add("active"); // نمایش تمام‌صفحه فیلترها
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            searchBox.classList.remove("active"); // بستن فیلترها
        });
    }

    if (applyFiltersBtn) {
        applyFiltersBtn.addEventListener("click", function () {
            searchBox.classList.remove("active"); // بستن پس از اعمال فیلتر
        });
    }
});