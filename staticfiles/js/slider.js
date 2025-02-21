document.addEventListener("DOMContentLoaded", function () {
    try {
        alert("JavaScript Loaded!"); // بررسی لود شدن جاوااسکریپت

        const slider = document.querySelector(".slider");
        let slides = document.querySelectorAll(".slide");

        if (!slider || slides.length === 0) {
            alert("Slider elements not found!");
            console.error("Slider elements not found!");
            return;
        }

        console.log("Slider found, total slides:", slides.length);

        let index = 0;
        let totalSlides = slides.length;
        let slideInterval;

        // ایجاد کپی از اسلایدهای اول برای چرخش بی‌نهایت
        for (let i = 0; i < 3; i++) {  
            let clone = slides[i].cloneNode(true);
            slider.appendChild(clone);
        }

        // به‌روزرسانی لیست اسلایدها بعد از اضافه شدن کپی‌ها
        slides = document.querySelectorAll(".slide");

        // تابع تنظیم دکمه‌های آکاردئون
        function setupAccordion() {
            document.querySelectorAll(".special-button").forEach(button => {
                button.removeEventListener("click", toggleAccordion); // حذف رویداد قبلی برای جلوگیری از تداخل
                button.addEventListener("click", toggleAccordion);
            });
        }

        // تابع تغییر نمایش پنل جزئیات
        function toggleAccordion(event) {
            const button = event.target;
            const panel = button.nextElementSibling;
            button.classList.toggle("active");
            panel.style.display = (panel.style.display === "block") ? "none" : "block";
        }

        function moveSlider() {
            index++;
            slider.style.transition = "transform 0.5s ease-in-out";
            slider.style.transform = `translateX(-${index * (slides[0].offsetWidth + 20)}px)`;

            if (index >= totalSlides) {
                setTimeout(() => {
                    slider.style.transition = "none";
                    slider.style.transform = "translateX(0px)";
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

        // تنظیم دکمه‌های آکاردئونی بعد از لود صفحه و اضافه شدن اسلایدهای جدید
        setupAccordion();

    } catch (error) {
        console.error("Error in slider script:", error);
    }
});