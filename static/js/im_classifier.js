$(document).ready(function () {
  // Init
  $(".image-section").hide();
  $(".loader").hide();
  $("#result").hide();

  // Upload Preview
  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $("#imagePreview").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        $("#imagePreview").hide();
        $("#imagePreview").fadeIn(650);
      };

      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imageUpload").change(function () {
    // $(".image-section").show();
    $("#ImageButton").show();
    $("#imageResults").text("");
    $("#imageResults").hide();
    readURL(this);
  });

  // Predict
  $("#ImageButton").click(function () {
    var form_data = new FormData($("#upload-image")[0]);
    // Show loading animation
    $(".loader").show();
    // Make prediction by calling api /predict
    $.ajax({
      type: "POST",
      url: "/image_prediction",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        $(".loader").hide();
        $("#imageResults").fadeIn(600);
        $("#imageResults").show();
        $("#imageResults").text(data);
      },
    });
  });
});
