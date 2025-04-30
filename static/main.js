const visit = document.querySelectorAll('.onsite');

visit[0].addEventListener('click',function(){
  window.location.href = 'https://www.carwale.com/mahindra-cars/be-6/';
})
visit[1].addEventListener('click', function(){
  window.location.href = "https://www.youtube.com";
});

function showSkeletonCards() {
  const container = document.getElementById("prod_cards");
  container.innerHTML = "";

  for (let i = 0; i < 6; i++) {
    container.innerHTML += `
      <div class="card skeleton">
        <div class="skeleton-img shimmer"></div>
        <div class="skeleton-title shimmer"></div>
        <div class="skeleton-line shimmer"></div>
        <div class="skeleton-line shimmer short"></div>
      </div>
    `;
  }
}

const infos = document.querySelectorAll('.prod_info');

infos.forEach(info => {
  if (info.textContent.length > 90) {
    infos.style.fontSize = 'small';
  }
});