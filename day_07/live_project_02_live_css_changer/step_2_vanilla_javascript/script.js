var targetDiv = document.getElementById("target");

function changeTargetHeight() {
  targetDiv.style.height = document.getElementsByName("height")[0].value;
  console.log("Changed height");
}

function changeTargetWidth() {
  targetDiv.style.width = document.getElementsByName("width")[0].value;
  console.log("Changed width");
}

function changeTargetBGColour() {
  targetDiv.style.backgroundColor = document.getElementsByName(
    "background-color"
  )[0].value;
  console.log("Changed background colour");
}
