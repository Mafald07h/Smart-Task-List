const tasksSuccess = document.getElementById("tasks_completed")
const tasksNotSuccess = document.getElementById("pendind_tasks")
const tesksEfficiency = document.getElementById("efficiency")

const btnChangeTheme = document.getElementById("changeTheme")
const bodyElement = document.querySelector("[data-body]")


btnChangeTheme.addEventListener("click", ()=> {
    bodyElement.classList.toggle("body-dark")
})
