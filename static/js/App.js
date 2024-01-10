const navbar = document.getElementById("navbar")

window.addEventListener("scroll", () => {
  if (window.scrollY > 20) {
    navbar.classList.add("fixed-top");
    navbar.classList.remove("hidden");
  } else {
    navbar.classList.add("hidden");
    setTimeout(() => navbar.classList.remove("fixed-top"), 300);
  }
})

