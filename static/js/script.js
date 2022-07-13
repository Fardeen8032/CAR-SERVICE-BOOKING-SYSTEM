const scrollbtn = document.getElementById("myBtn");

window.addEventListener("scroll", () => {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        scrollbtn.style.display = "block";
    } else {
        scrollbtn.style.display = "none";
    }
})
const Topfunct = () => {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}