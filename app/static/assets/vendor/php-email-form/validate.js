const textarea = document.getElementById("message");
textarea.addEventListener("keyup", (e) => {
  textarea.style.height = "auto";
  let scHeight = e.target.scrollHeight;
  textarea.style.height = `${scHeight}px `;
});

function sendMail() {
  var params = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value,
    
  };

  const serviseId = "service_ey7xz1l";
  const templateId = "template_rlk6i0c";

  emailjs
    .send(serviseId, templateId, params)
    .then((res) => {
      document.getElementById("name").value = "";
      document.getElementById("email").value = "";
      document.getElementById("message").value = "";
      console.log(res);
      alert("Habaringiz muvofaqiyatli jo'natildi");
    })
    .catch((err) => console.log(err));
}
