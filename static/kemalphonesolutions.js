request.responseType = "json";

$(document).ready(function(){
  $('input[name="modele"]').click(function(){ 
    $('input[name="modele"]').not(this).prop('checked', false);
  });
});

function validateUserinput() {
  var fname = document.getElementById('fname').value;
  var regex = /[a-zA-Z_ ]*+$/;
  
  if (!regex.test(fname)) {
    alert('Please enter only alphabetic letters.');
    return false;
  }
  
  return true;
}

// const fname = userinput instanceof objectType

// const lname =  String();
 
// if (fname instanceof String) {
//   return true;
// } else {
//   alert("Valide userinput required");
// }

// function typeof() {
//   return /^[a-zA-Z_ ]*$/;
// }
  
//   const userinput = validfname(fname);{
//     return true;
//   }
  
  


//RegExp(/^\p{L}/,'u').test(str)

// function userinput() {
//   var fname = window.prompt("Your value Please:");
//   return fname;
// }
// Main:
// -continue while the user wants to convert something
// -Check which conversion
// -Get the value
// -Display the result
 
// while(userinput()) {
//   var fname = String
//   var conversionType = guessTypeconversion();
//   var conversionValue = askValue();
//   var resultMessage = "The result is ";
//   var result = 0;

//   if (conversionType == "gn$") {
//   resultMessage += gn$ToCHF(Number(conversionValue)).toString();
//   } else if (conversionType== "celsius") {
//           resultMessage += celsiusToFarenheit(Number(conversionValue)).toString();
      
//   } else if (conversionType == "liters") {
//           resultMessage += litersToGallons(Number(conversionValue)).toString();
      
//   } else {(resultMessage == "Sorry. I can't do this coversion.");
  
//   }
//      console.log(fname);
//   }

// function validate(){
//   const userinput = /^[a-zA-Z_ ]*$/,  fname = document.getElementById('fname')
//   if (!fname.match(/^[a-zA-Z_ ]*$/))
//        {
//            //Your logice will be here.
//            return true;
//        }
//        else{
//            alert("Valide userinput required");
//        }
//   }

// function alpha(){
//  var fName = /^[a-zA-Z]+$/,  fname = document.getElementById('fname')
//  if(fName.value.match(/^[a-zA-Z]+$/)) 
//   {
//     redirect ('lname');
//    return true;
//   }
// else
//   { 
//    alert("Enter a valide First name!"); 
//    return false; 
//   }
//   }


// function includeHTML(){
//     var z, i, elmnt, file, xhttp;
//             /*loop through a collection of all HTML elements:*/
//     z = document.getElementsByTagName("*");
//         for (i = 0; i < z.length; i++) {
//             elmnt = z[i];
//               /*search for elements with a certain attribute:*/
//             file = elmnt.getAttribute("w3-include-html");
//             console.log(file)
//               if (file) {
//                 /*make an HTTP request using the attribute value as the file name:*/
//                 xhttp = new XMLHttpRequest();
//                 xhttp.onreadystatechange = function() {
//                   if (this.readyState == 4) {
//                     if (this.status == 200) {elmnt.innerHTML = this.responseText;}
//                     if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
//                     /*remove the attribute, and call this function once more:*/
//                     elmnt.removeAttribute("w3-include-html");
//                     includeHTML();
//                   }
//                 }
//                 xhttp.open("GET", file, true);
//                 xhttp.send();
//                 /*exit the function:*/
//                 return;
//               }
//             }
//           }

// var mo = new Object();
// mo.lname ="dmc";
// mo.fname="alias";
        
// var m = showModalDialog("alertuser.html", mo, "status=no; scroll=no; help=no; unadorned=yes");
        
// if(m==true){
//     alert("Valide input.");
// }else{
//     alert("Invalide input.");
//         }

// function isalpha() {
      
//    userinputs = seeuser(), userinput = "fname";
    
//     if userinput  != ("fname").isalpha()
//       flash('Enter a correct first name!')
                
//                 if ("fname").isalpha() == False;
//                     flash('Enter a correct first name!')
        
    
//                   }
       
//         return isalpha([userinput.isalpha() for userinput in userinputs])

// var fname = document.getElementById("fname").value;
// submitOK = "true";

// if (fname.length > 10) {
//   alert("The name may have no more than 10 characters");
//   submitOK = "false";
// }

// showUserinput: function() 
// {
//    formatString(useinput) = 'fname'; {
//     return `${fname} is correct ${this.userinput}`
//   }
//   for (let i = 0; i < this.friends.length; i++) {
//     console.log(formatString(this.friends[i]));
//   }
// }

// function validate(userinput)
// {
//  var fname = /^[a-zA-Z]+$/, userinput = fname;
//  if((userinput.value.match(fname))) 
//   {
//    return true;
//   }
// else
//   { 
//    alert("Only letters accepted"); 
//    return false; 
//   }
//   }

// function validate() 
// {
//   const userinput = document.getElementById('fname'),
//   fname = userinput
//   if((!userinput.value.match(/[^a-zA-Z]+$/, "")))
// {
//   return false;
// }

// else
// { 
 
// return true; 
// }
// }

// function validate(){
//   var name = document.getElementById('fname').value;
//   var fname = /$*^[a-zA-Z_ ]*$/  
//   if (fname.match(/$*^[a-zA-Z_ ]*$/))
//        {
//            //Your logice will be here.
//            redirect.box('lname');
//        }
//        else{
//            alert("Valide userinput required");
//        }
//   }

// $(document).ready(function(){
//   $("input[type='text']").keypress(function(event){
//       var fname = event.which;
//       if(!(fname = /$^[a-zA-Z_ ]*$/ && inputValue == Text=={})) {
//         return false 
          
//       }
//       else{
//                  alert("Please enter only alphabets");
//                }
//   });
// });

// var name = prompt('Enter name');

// if(fname === /[^a-zA-Z_]/ || fname == "") {
//   alert("name is empty!");
// } else if (/[^a-zA-Z_]/i.test(fname)){
//   alert("name is not valid!");
// } else {
//   alert("name is valid!");
// }

// function validate(){
//   var name = document.getElementById('fname').value;
//   if(name.match(/$^[a-zA-Z_ ]*$/)) 
//        {
//            //Your logice will be here.
//            alert("It's valid");
//        }
//        else{
//            alert("Please enter only alphabets");
//        }
//   }


//  function validate(){
//   const fname = document.getElementById('fname'), fname = userinput
//         if ("fname".match(/^[a-zA-Z_ ]*$/))
//         {
//         return true;
//         }
//           else{

//           return false;
//           }

// } 

// isValidRadius(fname); {
//   const fname = /^[a-zA-Z_ ]*$/
//   if (fname.match(/^[a-zA-Z_ ]*$/))
//          {
//              //Your logice will be here.
//              return true;
//          }
//          else{
//              alert("Valide userinput required");
//          }

//   return !!(fname.match(fname))
//         }



const hamburgerToggler = document.querySelector(".hamburger")
const navLinksContainer = document.querySelector(".navlinks-container");

const toggleNav = () => {
    hamburgerToggler.classList.toggle("open")

    const ariaToggler = hamburgerToggler.getAttribute("aria-expanded") === "true" ? "false" : "true";
    hamburgerToggler.setAttribute("aria-expanded", ariaToggler)

    navLinksContainer.classList.toggle("open")

}
hamburgerToggler.addEventListener("click", toggleNav) 