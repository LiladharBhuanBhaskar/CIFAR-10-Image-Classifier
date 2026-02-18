function previewImage() {
  const input = document.getElementById("imageInput");
  const preview = document.getElementById("preview");

  if (!input.files.length) {
    preview.style.display = "none";
    return;
  }

  const reader = new FileReader();
  reader.onload = e => {
    preview.src = e.target.result;
    preview.style.display = "block";
  };

  reader.readAsDataURL(input.files[0]);
}

async function predict() {
  const input = document.getElementById("imageInput");
  const result = document.getElementById("result");

  if (!input.files.length) {
    result.innerText = "Please upload an image.";
    return;
  }

  const formData = new FormData();
  formData.append("file", input.files[0]);

  result.innerText = "Predicting...";

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    result.innerText =
      `Prediction: ${data.class} | Confidence: ${(data.confidence * 100).toFixed(2)}%`;

  } catch (err) {
    result.innerText = "Server error. Try again.";
  }
}
document.getElementById("imageInput").addEventListener("change", previewImage);
document.getElementById("predictButton").addEventListener("click", predict);