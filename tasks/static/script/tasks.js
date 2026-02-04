const btnAddTask = document.getElementById("addTasks")
const containerTasks = document.getElementById("container-tasks")

// Change Theme
const btnChangeTheme2 = document.getElementById("changeTheme")
const titleDark2 = document.querySelector("[data-title]")
const linkDark = document.querySelectorAll("[data-dashboard-link]")
const navbarLeftDark = document.querySelector("[data-navbar]")
const nameColumnDark = document.querySelectorAll("[data-name-column]")
const formDark = document.querySelector("[data-form-dark]")

btnChangeTheme2.addEventListener("click", ()=>{
    titleDark2.classList.toggle("title-dark2")
    linkDark.forEach(link, ()=>{
        link.classList.toggle("dashboard__link-dark")
    })
    navbarLeftDark.classList.toggle("navbar__left-dark")

    nameColumnDark.forEach(column, ()=> {
        column.classList.toggle("column-dark")
    })

    formDark.classList.toggle("container-tasks-show-dark")
})

btnAddTask.addEventListener("click",()=>{
    containerTasks.classList.toggle("container-tasks-show")
})

