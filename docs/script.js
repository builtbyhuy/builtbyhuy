document.querySelectorAll("[data-comparison]").forEach(function (comparison) {
  var buttons = comparison.querySelectorAll("[data-version]");
  var image = comparison.querySelector("[data-comparison-image]");
  var caption = comparison.querySelector("[data-comparison-caption]");
  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      var after = button.dataset.version === "after";
      buttons.forEach(function (item) {
        item.setAttribute("aria-pressed", String(item === button));
      });
      image.src = after ? image.dataset.after : image.dataset.before;
      image.alt = after
        ? "FIELDNOTE after: a large architectural image, clear heading and enquiry action."
        : "FIELDNOTE before: the deliberately flawed baseline with dense navigation and competing information.";
      caption.textContent = after
        ? "After · the running responsive example"
        : "Before · a deliberately flawed comparison fixture";
    });
  });
});
