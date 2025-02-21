alert("فایل script.js با موفقیت لود شد!");
alert("JavaScript Loaded!"); // بررسی لود شدن جاوااسکریپت

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

function closeFilters() {
    document.getElementById("search-box").style.display = "none";
}
// نمایش/مخفی کردن فیلترها در موبایل
document.addEventListener("DOMContentLoaded", function () {
    try {
        const filterBtn = document.getElementById("filter-btn");
        const searchBox = document.getElementById("search-box");
        const closeBtn = document.querySelector(".filter-close");   // دکمه بستن فیلترها
        const applyFiltersBtn = document.getElementById("applyFilters");  // دکمه اعمال فیلترها


        if (filterBtn && searchBox) {
            filterBtn.addEventListener("click", function () {
                searchBox.style.display = "flex";   // نمایش کادر جستجو
                searchBox.classList.add("active");
            });
        }

        if (closeBtn) {
            closeBtn.addEventListener("click", function () {
                searchBox.classList.remove("active");  // بستن فیلترها
                searchBox.style.display = "none";   // اضافه کردن نمایش بلاک
            });
        }

        if (applyFiltersBtn) {
            applyFiltersBtn.addEventListener("click", function () {
                searchBox.classList.remove("active");  // بستن پس از اعمال فیلتر
                searchBox.style.display = "none";  // اضافه کردن نمایش بلاک
            });
        }

         // عملکرد آکاردئون
        var acc = document.getElementsByClassName("accordion");
        for (var i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function () {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                panel.style.display = (panel.style.display === "block") ? "none" : "block";
            });
        }

        var specialButtons = document.getElementsByClassName("special-button");
        for (var i = 0; i < specialButtons.length; i++) {
            specialButtons[i].addEventListener("click", function () {
                this.classList.toggle("active");
                var panel = this.nextElementSibling;
                panel.style.display = (panel.style.display === "block") ? "none" : "block";
            });
        }

         // اسکریپت مربوط به اسلایدر
        const slider = document.querySelector(".slider");
        const slides = document.querySelectorAll(".slide");

        if (!slider || slides.length === 0) {
            alert("Slider elements not found!");
            console.error("Slider elements not found!");
            return;
        }

        console.log("Slider found, total slides:", slides.length);

        let index = 0;
        let totalSlides = slides.length;
        let slideWidth = slides[0].offsetWidth + 20; // فرض بر این است که 20 پیکسل فاصله بین اسلایدهاست

        function moveSlider() {
            index++;
            slider.style.transition = "transform 0.5s ease-in-out";
            slider.style.transform = `translateX(-${index * slideWidth}px)`;

            if (index >= totalSlides) {
                setTimeout(() => {
                    slider.style.transition = "none";
                    slider.style.transform = `translateX(0px)`;
                    index = 0;
                }, 500);
            }
        }

        function startSlider() {
            console.log("Slider started");
            slideInterval = setInterval(moveSlider, 3000);
        }

        function stopSlider() {
            console.log("Slider stopped");
            clearInterval(slideInterval);
        }

        slider.addEventListener("mouseenter", stopSlider);
        slider.addEventListener("mouseleave", startSlider);

        startSlider();
    } catch (error) {
        console.error("Error in script:", error);
    }
});

