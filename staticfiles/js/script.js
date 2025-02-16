document.addEventListener("DOMContentLoaded", function () {
    // باز و بسته کردن فیلتر در موبایل
    document.querySelector(".open-filter").addEventListener("click", function () {
        document.querySelector(".filter-container").style.display = "flex";
    });

    document.querySelector(".close-filter").addEventListener("click", function () {
        document.querySelector(".filter-container").style.display = "none";
    });

    // مدیریت باز و بسته شدن کشویی‌ها
    document.querySelectorAll(".dropdown").forEach(function (dropdown) {
        dropdown.addEventListener("click", function () {
            let menu = this.querySelector(".dropdown-menu");
            let isOpen = menu.style.display === "block";
            document.querySelectorAll(".dropdown-menu").forEach(m => m.style.display = "none");
            menu.style.display = isOpen ? "none" : "block";
        });
    });
});