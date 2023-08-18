          $(document).ready(function(){
            $('input[name="modele"]').click(function(){ 
                $('input[name="modele"]').not(this).prop('checked', false);
            });
        });

function includeHTML(){
    var z, i, elmnt, file, xhttp;
            /*loop through a collection of all HTML elements:*/
    z = document.getElementsByTagName("*");
        for (i = 0; i < z.length; i++) {
            elmnt = z[i];
              /*search for elements with a certain attribute:*/
            file = elmnt.getAttribute("w3-include-html");
            console.log(file)
              if (file) {
                /*make an HTTP request using the attribute value as the file name:*/
                xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function() {
                  if (this.readyState == 4) {
                    if (this.status == 200) {elmnt.innerHTML = this.responseText;}
                    if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
                    /*remove the attribute, and call this function once more:*/
                    elmnt.removeAttribute("w3-include-html");
                    includeHTML();
                  }
                }
                xhttp.open("GET", file, true);
                xhttp.send();
                /*exit the function:*/
                return;
              }
            }
          }

var mo = new Object();
mo.lname ="dmc";
mo.fname="alias";
        
var m = showModalDialog("alertuser.html", mo, "status=no; scroll=no; help=no; unadorned=yes");
        
if(m==true){
    alert("Valide input.");
}else{
    alert("Invalide input.");
        }

const hamburgerToggler = document.querySelector(".hamburger")
const navLinksContainer = document.querySelector(".navlinks-container");

const toggleNav = () => {
    hamburgerToggler.classList.toggle("open")

    const ariaToggler = hamburgerToggler.getAttribute("aria-expanded") === "true" ? "false" : "true";
    hamburgerToggler.setAttribute("aria-expanded", ariaToggler)

    navLinksContainer.classList.toggle("open")

}
hamburgerToggler.addEventListener("click", toggleNav)