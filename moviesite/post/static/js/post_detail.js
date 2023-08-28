document.addEventListener("DOMContentLoaded", function () {
  var button = document.getElementById("comment-open-button");
  var div = document.getElementById("comment-form-outercontainer");

  var isDivVisible = false;

  button.addEventListener("click", function () {
    if (isDivVisible) {
      div.style.display = "none";
    } else {
      div.style.display = "block";
    }
    isDivVisible = !isDivVisible;
  });
});
