const tasksSuccess = document.getElementById("tasks_completed")
const tasksNotSuccess = document.getElementById("pendind_tasks")
const tesksEfficiency = document.getElementById("efficiency")

const btnChangeTheme = document.getElementById("changeTheme")
const bodyElement = document.querySelector("[data-body]")
const navbarDark = document.querySelector("[data-navbar]")
const titleDark = document.querySelector("[data-title]")
const subtextDark = document.querySelector("[data-subtext]")
const dashboardLink = document.querySelectorAll("[data-dashboard-link]")
const itemDashboard = document.querySelectorAll("[data-item]")

btnChangeTheme.addEventListener("click", ()=> {
    bodyElement.classList.toggle("body-dark")
    navbarDark.classList.toggle("navbar__left-dark")
    titleDark.classList.toggle("title-dark")

    dashboardLink.forEach(link => {
        link.classList.toggle("dashboard__link-dark")
    })

    subtextDark.classList.toggle("subtext-dark")

    itemDashboard.forEach(item => {
        item.classList.toggle("item-dark")
    })
})
