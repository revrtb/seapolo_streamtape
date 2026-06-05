var saCMHRycVyC1=`
<img src="${banner_image_ch0p}" class="uglyppl_ch0p" id="cover_ad" style="position: static;
    width: ${width_ch0p}px;
    height: ${height_ch0p}px;
    border: 0px solid gray;
    margin: 0;
    padding: 0;
    overflow: hidden;
    z-index: 999999;
    display: none;
  ">`;

var saCMHRycVyC2 = `<iframe
  id='iframe_ad_ch0p'
  src="https://seapolo.com/`;

var saCMHRycVyC3 =`" sandbox="allow-same-origin allow-scripts allow-forms"
  class="niceppl_ch0p"
  style="
    position: static;
    width: ${width_ch0p}%;
    height: ${height_ch0p}px;
    border: 0px solid gray;
    margin: 0;
    padding: 0;
    overflow: hidden;
    z-index: 999999;
  ">
</iframe>`;

function rFrx(do_load, code_str) {
  return new Promise(resolve => {

  if (do_load) {
    load_cap_ch0p = 0;
  }

  setTimeout(function() {
      el = document.getElementById('metaconfig_ch0p');
      el.insertAdjacentHTML('afterEnd', code_str);
  }, 100+load_cap_ch0p*1000);


 url = '';

  function myFunction() {
      window.open(url, '_blank');
  }


  setTimeout(function() {
    
    document.querySelectorAll('iframe[class="niceppl_ch0p"]').forEach(function(e) {
      url=e.src;
      if (do_load) {
        e.parentNode.removeChild(e);
      }
    });

  document.querySelectorAll('img[class="uglyppl_ch0p"]').forEach(function(e) {
      e.style.display = 'block';
      e.addEventListener('click', myFunction, false);
  });
  
  resolve('resolved');
  }, 100+(load_cap_ch0p+close_cap_ch0p)*1000);


    });
}

async function main(zap_codes) {
  for(let i=0; i<zap_codes.length; i++) {

      if ('' == banner_image_ch0p)  {
          saCMHRycVyC1='';
          document.querySelectorAll('img[class="uglyppl_ch0p"]').forEach(function(e) {
            e.parentNode.removeChild(e);
          });
      }

      var saCMHRycVyC = saCMHRycVyC1+saCMHRycVyC2+zap_codes[i]+saCMHRycVyC3;

      await rFrx(i==0, saCMHRycVyC);

  }

}

main(codes);

