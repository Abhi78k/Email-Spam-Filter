async function predict(){
  message = document.getElementById('message-input').value;
  const response = await fetch("http://127.0.0.1:8000/predict", {method: "POST", headers: {"Content-Type":"application/json"},
  body: JSON.stringify({message: message})}
  )
  const data =  await response.json();
  if (data.prediction==0){
    document.getElementById('result-text').innerText = "SPAM!!"
  }else{
    document.getElementById('result-text').innerText = "Normal mail"
  }
};