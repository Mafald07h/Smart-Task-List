const tasksSuccess = document.getElementById("tasks_completed")
const tasksNotSuccess = document.getElementById("pendind_tasks")
const tesksEfficiency = document.getElementById("efficiency")

const btnChangeTheme = document.getElementById("changeTheme")
const bodyElement = document.querySelector("[data-body]")
const navbarDark = document.querySelector("[data-navbar]")
const titleDark = document.querySelector("[data-title]")
const subtextDark = document.querySelector("[data-subtext]")

btnChangeTheme.addEventListener("click", ()=> {
    bodyElement.classList.toggle("body-dark")
    navbarDark.classList.toggle("navbar__left-dark")
    titleDark.classList.toggle("title-dark")
    subtextDark.classList.toggle("subtext-dark")
})
