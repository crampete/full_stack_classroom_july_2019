// It is important to understand that
// functions are first class objects in JavaScript :)
// var validateForm = function(e) {}
function validateForm(e) {
  // we prevent the form from getting submitted
  e.preventDefault();
  var name = document.getElementById("name-input").value;

  if (name === "" || hasNumber(name)) {
    alert("Name cannot be empty and cannot contain numbers");
  } else {
    alert("Success :)");
    // clear input box so that they can submit again
    document.getElementById("name-input").value = "";
  }
}

function hasNumber(textToCheck) {
  for (var i = 0; i < textToCheck.length; i++) {
    // https://stackoverflow.com/a/8935649/5698202
    // check if the character is a digit or not
    if ("0123456789".indexOf(textToCheck[i]) !== -1) {
      return true;
    }
  }

  return false;
}
