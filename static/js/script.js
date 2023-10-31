const aside = document.getElementById("aside")
function addTodo() {
    aside.style.bottom = 0;
}
function cancelAside() {
    aside.style.bottom = 100 + 'vh';
}