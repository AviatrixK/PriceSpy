gsap.to("#cards #bstr", {
  x: "80vw",
  rotate: 360,
  duration: 3,
  scrollTrigger: {
    trigger: "#cards",
    scroller: "body",
    start: "top 0%",
    end: "top -230%",
    scrub: 5,
    pin: true,
  },
});
//xxxxxxxxxxxxxxxxxxxx GSAP END FOR THE CARDS SECTION xxxxxxxxxxxxxxxxxxxxxxxxxxxx
const sign_in_btn = document.querySelector('#sign-in');
const sign_in_card = document.querySelector('.sign-in-card');
const ovrly_s = document.querySelector('.ovrly_s');
const email = document.querySelector('#email');
const otp = document.querySelector('#otp');
const send_otp = document.querySelector('#send_otp');
const verify = document.querySelector('#verify');
const auth_message = document.querySelector('#auth_message');

sign_in_btn.addEventListener('click', function () {
  sign_in_card.classList.remove('hide');
  ovrly_s.classList.remove('hide');
});

ovrly_s.addEventListener('click', function () {
  sign_in_card.classList.add('hide');
  ovrly_s.classList.add('hide');
})

email.addEventListener('input', function () {
  if (email.value.trim() !== '') {
    send_otp.disabled = false;
    send_otp.classList.remove('disabled');
    send_otp.classList.add('enabled');
  } else {
    send_otp.disabled = true;
    send_otp.classList.remove('enabled');
    send_otp.classList.add('disabled');
  }
});

otp.addEventListener('input', function () {
  if (otp.value.trim() !== '' && email.value.trim() != '') {
    verify.disabled = false;
    verify.classList.remove('disabled');
    verify.classList.add('enabled');
  } else {
    verify.disabled = true;
    verify.classList.remove('enabled');
    verify.classList.add('disabled');
  }
})

send_otp.addEventListener('click', function () {
  let mail = email.value;
  fetch("/send-otp", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: mail })
  })
    .then(response => {
      if (response.ok) {
        auth_message.innerText = "OTP sent! Check your email.";
      } else {
        auth_message.innerText = "Failed to send OTP.";
      }
    })
    .catch(error => console.log(error));
});


verify.addEventListener('click', function () {
  let mail = email.value;
  let otpValue = otp.value;
  fetch("/verify-otp", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email: mail, otp: otpValue })
  })
    .then(response => {
      if (response.status === 200) {
        auth_message.innerText = "OTP Verified Successfully!";
        sign_in_card.classList.add('hide');
        ovrly_s.classList.add('hide');
      } else if (response.status === 401) {
        auth_message.innerText = "Invalid OTP. Try again.";
      } else if (response.status === 410) {
        auth_message.innerText = "OTP Expired. Request a new one.";
      } else {
        auth_message.innerText = "Error verifying OTP.";
      }
    })
    .catch(error => console.log(error));
});


document.getElementById("getstart").addEventListener('click', function () {
  window.location.href = 'index.html';
});

