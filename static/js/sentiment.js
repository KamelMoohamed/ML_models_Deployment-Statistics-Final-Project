$(document).ready(function () {
  // Init
  $(".image-section").hide();
  $(".loader").hide();
  $("#result").hide();

  // Upload Preview
  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imageUpload").change(function () {
    $(".image-section").show();
    $("#button1").show();
    $("#result").text("");
    $("#result").hide();
    readURL(this);
  });

  // Predict
  $("#ClassifierPredict").click(function () {
    var form_data = new FormData($("#upload-file")[0]);
    $(".loader").show();
    // Make prediction by calling api /predict
    $.ajax({
      type: "POST",
      url: "/sentiment_prediction",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        $("#result").fadeIn(600);
        $("#SenResults").text(data);
        console.log("Success!");
      },
    });
  });
});
