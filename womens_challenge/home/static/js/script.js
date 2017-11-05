  function openTab(evt, tabName, isGuide) {
    var i, tabcontent, tablinks;
    if(!isGuide){
      tabcontent = document.getElementsByClassName("tabcontent");
      tablinks = document.getElementsByClassName("tablink");
    }else{
      tabcontent = document.getElementsByClassName("guidecontent");
      tablinks = document.getElementsByClassName("guidelink");
    }
      for (i = 0; i < tabcontent.length; i++) {
          tabcontent[i].style.display = "none";
      }

      for (i = 0; i < tablinks.length; i++) {
          tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
      document.getElementById(tabName).style.display = "block";
      evt.currentTarget.className += " active";
      scroll(tabName);
  }
function scroll(tabName) {
  $("button").click(function() {
    $('html,body').animate({
        scrollTop: $("tabName").offset().top},
        'slow');
  });
}
