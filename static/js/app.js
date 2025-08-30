const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const body = document.querySelector("body");
const navLinks = navMenu.querySelectorAll("li");
const nav = document.querySelector("nav");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
  body.classList.toggle("no-scroll");
});

function closeMenu() {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
  body.classList.remove("no-scroll");
}

navLinks.forEach((link) => {
  link.addEventListener("click", closeMenu);
});

function handleScroll() {
  if (window.scrollY > 150) {
    nav.classList.add("sticky-nav");
  } else {
    nav.classList.remove("sticky-nav");
  }
}
window.addEventListener("scroll", handleScroll);

function initTypedText() {
  const options = {
    strings: [
      "Want to Estimate Your Income Tax,",
      "Deductions &amp; Exemptions ?",
      "Look No Further!",
    ],
    typeSpeed: 70,
    backSpeed: 50,
    backDelay: 1000,
    startDelay: 500,
    loop: true,
  };
  const typed = new Typed("#typed-text", options);
}

initTypedText();
