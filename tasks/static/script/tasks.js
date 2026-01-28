const btnAddTask = document.getElementById("addTasks")
const containerTasks = document.getElementById("container-tasks")

const btnChangeTheme = document.getElementById("changeTheme")
const titleDark = document.querySelector("[data-title]")
const linkDark = document.querySelectorAll("[data-dashboard-link]")

btnChangeTheme.addEventListener("click", ()=>{
    titleDark.classList.toggle("title-dark")
    linkDark.forEach(link, ()=>{
        link.classList.toggle("dashboard__link-dark")
    })
})

btnAddTask.addEventListener("click",()=>{
    containerTasks.classList.toggle("container-tasks-show")
})

