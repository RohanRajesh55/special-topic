// Add event listener to navbar toggler
document.addEventListener("DOMContentLoaded", function () {
  const navbarToggler = document.querySelector(".navbar-toggler");
  navbarToggler.addEventListener("click", function () {
    const navbarCollapse = document.querySelector("#navbarCollapse");
    navbarCollapse.classList.toggle("show");
  });
});

// Add event listener to property form submit button
document.addEventListener("DOMContentLoaded", function () {
  const propertyForm = document.querySelector(".property-form");
  const submitButton = propertyForm.querySelector("button[type='submit']");

  submitButton.addEventListener("click", function (event) {
    event.preventDefault();
    // Add your form submission logic here
    console.log("Form submitted!");
  });
});
