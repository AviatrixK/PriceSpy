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

document.getElementById("getstart").addEventListener('click', function(){
  window.location.href = '/main_page/index.html';
});
