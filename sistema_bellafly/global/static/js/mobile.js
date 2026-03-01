
window.addEventListener("scroll", function () {
    const header = document.querySelector("header");
    if (window.scrollY > 50) {
        header.classList.add("header-shrink");
    } else {
        header.classList.remove("header-shrink");
    }
});

function toggleMobileMenu() {
    document.querySelector(".nav").classList.toggle("active");
}
