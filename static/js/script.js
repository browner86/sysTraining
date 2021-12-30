
// Get the container element
var topicsContainer = document.getElementById("left-nav");
console.log(topicsContainer);
// Get all buttons with class="btn" inside the container
var btns = topicsContainer.getElementsByClassName("nav-link");
console.log(btns);
// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("active");
      console.log(current);
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
      console.log();
    });
  } 

  // function addSelectId()

  // function copyToClipboard(text) {
  //   /* Get the text field */
  //   var copyText = text;
  
  //   /* Select the text field */
  //   copyText.select();
  //   copyText.setSelectionRange(0, 99999); /* For mobile devices */
  
  //   /* Copy the text inside the text field */
  //   document.execCommand("copy");
  
  //   /* Alert the copied text */
  //   alert("Copied the text: " + copyText.value);
  // } 