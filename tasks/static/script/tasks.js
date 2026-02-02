const btnAddTask = document.getElementById("addTasks")
const containerTasks = document.getElementById("container-tasks")

// Change Theme
const btnChangeTheme2 = document.getElementById("changeTheme")
const titleDark2 = document.querySelector("[data-title]")
const linkDark = document.querySelectorAll("[data-dashboard-link]")
const navbarLeftDark = document.querySelector("[data-navbar]")

btnChangeTheme2.addEventListener("click", ()=>{
    titleDark2.classList.toggle("title-dark")
    linkDark.forEach(link, ()=>{
        link.classList.toggle("dashboard__link-dark")
    })
    navbarLeftDark.classList.toggle("navbar__left-dark")
})

btnAddTask.addEventListener("click",()=>{
    containerTasks.classList.toggle("container-tasks-show")
})

