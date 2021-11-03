/*
     Toggle Navgation Links Function
*/
let openMenu = document.querySelector(".toggle-menu");
let links = document.querySelector(".nav-bar");
let closeButton = document.querySelector(".nav-bar .close");

openMenu.addEventListener("click", openLinks);
closeButton.addEventListener("click", closeLinks);

function openLinks() {
  links.classList.add("active");
}
function closeLinks() {
  links.classList.remove("active");
}

/*
  Close Navgation Links Aftre Clicking A   Link Function
*/
let navLink = document.querySelectorAll("#nav-bar a");

navLink.forEach((link) => {
  link.addEventListener("click", function () {
    closeLinks();
  });
});

/*
    Toggle Accordings Function
 */
let questions = document.querySelectorAll(".question .question-header");

questions.forEach((question) => {
  question.addEventListener("click", showAnswer);
});

function showAnswer() {
  let getParent = this.closest(".question");
  let getAnswetDiv = getParent.querySelector(".question-content");
  let getAnswetDivHeight = getAnswetDiv.scrollHeight;

  getParent.classList.toggle("active");
  if (getParent.classList.contains("active")) {
    getAnswetDiv.style.height = getAnswetDivHeight + "px";
    console.log(getAnswetDivHeight);
  } else {
    getAnswetDiv.style.height = 0;
  }
}