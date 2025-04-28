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


// let searchField = document.querySelector('#searchField');
// searchField.addEventListener('keydown', function(e){
//   if(e.key === 'Enter'){
//     searchTerm();
//   } 
// });

const visit = document.querySelectorAll('.onsite');

visit[0].addEventListener('click',function(){
  window.location.href = 'https://www.carwale.com/mahindra-cars/be-6/';
})
visit[1].addEventListener('click', function(){
  window.location.href = "https://www.youtube.com";
});

const arrow_dwn = document.querySelector('.drp');
const drop_down = document.querySelector('.drop-down');
const drp_list = document.querySelector('.drp_list')
const list_items = document.querySelectorAll('.drp_list li');
const ctxt = document.querySelector('.catxt')
const reload = document.querySelector('#reload_bttn');

reload.addEventListener('click',function(){
  reload.classList.add('reloadts');
});

drop_down.addEventListener('click', function(e) {
  e.stopPropagation();
  arrow_dwn.classList.toggle('rotate');
  drp_list.classList.toggle('show')
});

document.addEventListener('click', function(){
  arrow_dwn.classList.remove('rotate');
  drp_list.classList.remove('show')
});

list_items.forEach(function(item) {
  item.addEventListener('click', function() {
    ctxt.innerText = item.textContent;
    if (item.textContent.length > 5) {
      ctxt.style.fontSize = '1rem'
    } else {
      ctxt.style.fontSize = '1.4rem'
    }
  });
});