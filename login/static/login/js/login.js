const register = document.querySelectorAll(".form-register");
const card = document.querySelector(".flip-card");
const modalPassword = document.querySelector(".modal-message");

Array.from(register).forEach((r) => {
  r.addEventListener("click", (e) => {
    e.preventDefault();
    card.classList.toggle("flipped");
  });
});
