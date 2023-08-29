-Sur la page web:
Quand mes Users viennent sur mon site web, ils cliquent sur User Input, 
ils sont dirigés vers la page web du modèle de leur(s) téléphone(s) à réparer, 
ils renseignent également sur la panne puis clique sur ENVOYER. Mais là aussi, 
ils peuvent cliquer sur le l'hyperlien qui renvoit à la page web des autres modèles de téléphone différent des modèles qui se sont afficheés quand ils ont fait la demande.
Là aussi, mes Users font la même procedure  pour m'emvoyer leur requête.

-Sur le serveur:
Le User entre son Prénom "fname" ou Nom "lname", leur sélection est reçue et stockée dans la base, puis un message lui est renvoyer pour confirmer l'enrégistrement;
Idem pour la sélection du modèle de téléphone à réparer
-Limit User Input to Only Alphabetic Letters in order to set an easy structures data form
The user input validation is an essential aspect of web development to ensure the integrity and security of the data.
-In this case, the question is about limiting user input to only alphabetic letters using Flask, a popular web framework for Python.
- To do this, I use a combination of client-side and server-side validation techniques.
*Client-Side Validation
Client-side validation is performed on the user's device before the data is sent to the server.
-It provides immediate feedback to the user and reduces unnecessary server requests.
-Then, I use JavaScript to validate the input on the client-side.
a) The JavaScript function to my useinput HTML file that will be triggered when the form is submitted,
b) I Modify the useinput(instead of "/userinput" it become for action form "/submit") HTML form to call the validateInput() function when submitted
*Server-Side Validation
Client-side validation can be bypassed, so it's crucial to perform server-side validation as well.
-Flask provides a convenient way to validate user input using the request object.
a) I add Import the request object from Flask on top of my flask app.py,
b) I use the request object to retrieve the user input and validate it on the server-side.
- For all:
.The submit() function is called when the form is submitted;
.After, It retrieves the value of the name input field using request.form.get('name');
.Then, The isalpha() method is used to check if the input contains only alphabetic letters. If not, an error message is returned to the user.
-With Flask, limiting user input to only alphabetic letters, involves both client-side and server-side validation:
.Using JavaScript, it provides immediate feedback to the user, on client-side validation;
.Using Flask, it ensures the integrity of the data, on server-side validation.
* These Instructions and techniques, help me creating a more robust and user-friendly web application.