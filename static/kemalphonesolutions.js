          $(document).ready(function(){
            $('input[name="modele"]').click(function(){ 
                $('input[name="modele"]').not(this).prop('checked', false);
            });
        });

const hamburgerToggler = document.querySelector(".hamburger")
const navLinksContainer = document.querySelector(".navlinks-container");

const toggleNav = () => {
    hamburgerToggler.classList.toggle("open")

    const ariaToggler = hamburgerToggler.getAttribute("aria-expanded") === "true" ? "false" : "true";
    hamburgerToggler.setAttribute("aria-expanded", ariaToggler)

    navLinksContainer.classList.toggle("open")

}
hamburgerToggler.addEventListener("click", toggleNav)