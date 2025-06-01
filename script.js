async function startTraining() {
  console.log("hihohoh");

  const lr = parseFloat(document.getElementById("lr").value);
  const epochs = parseInt(document.getElementById("epochs").value);
  const status = document.getElementById("status");
  const plot = document.getElementById("plot");

  status.innerText = "Training started...";
  plot.hidden = false;

  const response = await fetch("/train", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ learning_rate: lr, epochs: epochs }),
  });

  const data = await response.json();
  for (let i = 0; i < data.length; i++) {
    plot.src = data[i].image + "&t=" + new Date().getTime(); // avoid caching
    status.innerText = `Epoch: ${data[i].epoch} | Loss: ${data[i].loss.toFixed(
      4
    )}`;
    await new Promise((resolve) => setTimeout(resolve, 500));
  }

  status.innerText += "\n🎉 Training Complete!";
}
