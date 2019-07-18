(function() {
  // 'use-strict'

  function deleteTodo(e) {
    e.toElement.parentNode.parentNode.removeChild(e.toElement.parentNode);
  }

  function addTodo(e) {
    // ensuring that you do not submit the form
    // as it triggers a page refresh
    e.preventDefault();
    var todoText = document.getElementById("new-todo").value;

    // check if there are non white space (space, tab, newline)
    // characters in the input box as well
    if (todoText.replace(/\s/g, "").length !== 0) {
      var newLi = document.createElement("li");
      var text = document.createTextNode(todoText);
      newLi.appendChild(text);

      var newSpanTick = document.createElement("span");
      var spanTick = document.createTextNode("✓");
      newSpanTick.appendChild(spanTick);
      newSpanTick.addEventListener("click", deleteTodo);

      newLi.appendChild(newSpanTick);

      // Finally adding the new todo we just created
      document.getElementById("pending-todo-ul").appendChild(newLi);

      // emptying input box
      document.getElementById("new-todo").value = "";
    }
  }

  document.getElementById("add-todo").addEventListener("click", addTodo);
})();
