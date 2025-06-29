const visit = document.querySelectorAll('.onsite');

visit[0].addEventListener('click',function(){
  window.open('https://www.carwale.com/mahindra-cars/be-6/','_blank');
})
visit[1].addEventListener('click', function(){
  window.open("https://g.co/kgs/Lmj8VqL", '_blank');
});
visit[2].addEventListener('click', function(){
  window.open ("https://www.snapdeal.com/product/apeiron-stainless-steel-sipper-water/631147052901?supc=SDL514737760&utm_source=earth&utm_medium=631147052901_207_5_166&vendorCode=S554f5&isSellerPage=true&fv=true&utm_source=earth_shopping&utm_campaign=snapdeal_video_account_standard_sc_roas_7d_ftu_050224&utm_medium=&utm_term=689956125051_160018390273_{bidstrategy}&gad_source=1&gbraid=0AAAAADv2ynTBHzn8cdiAgQDxxyYfQbKGD&gclid=Cj0KCQjwt8zABhDKARIsAHXuD7bio-txE3m6t28Jl5HiCp7lY78xykW5Uj02BZXcsdD_816ljNgB6hoaAs_9EALw_wcB", '_blank');
});
visit[3].addEventListener('click', function(){
  window.open ("https://www.shopclues.com/odoky-multi-color-cotton-half-sleeve-t-shirt-151346207.html", '_blank');
});
visit[4].addEventListener('click', function(){
  window.open ("https://ondcstore.snapdeal.com/product/sneakers-for-men/1165334353", '_blank');
});
visit[5].addEventListener('click', function(){
  window.open ("https://www.snapdeal.com/product/da-tasche-green-polyester-backpack/630519334580", '_blank');
});

function showLoader() {
  const container = document.getElementById("prod_cards");
  container.innerHTML = "";

  for (let i = 0; i < 6; i++) {
    container.innerHTML += `
      <div class="card skeleton">
        <div class="skeleton-img shimmer"></div>
        <div class="skeleton-title shimmer"></div>
        <div class="skeleton-line shimmer"></div>
        <div class="skeleton-line shimmer short"></div>
        <div class="skeleton-button shimmer"></div>
      </div>
    `;
  }
}
