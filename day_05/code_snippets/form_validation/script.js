// It is important to understand that
// functions are first class objects in JavaScript :)
// var validateForm = function(e) {}
function validateForm(e) {
  e.preventDefault();
  var name = document.getElementById("name-input").value;

  if (name === "" || hasNumber(name)) {
    alert("Name cannot be empty and cannot contain numbers");
  }
}

function hasNumber(textToCheck) {
  for (var i = 0; i < textToCheck.length; i++) {
    if ("0123456789".indexOf(textToCheck[i]) !== -1) {
      return true;
    }
  }

  return false;
}
