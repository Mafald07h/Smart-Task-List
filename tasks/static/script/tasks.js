const btnAddTask = document.getElementById("addTasks")
const containerTasks = document.getElementById("container-tasks")

btnAddTask.addEventListener("click",()=>{
    containerTasks.classList.toggle("container-tasks-show")
})