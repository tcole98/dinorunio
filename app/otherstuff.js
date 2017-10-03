// if (hiddenscore < 9999 ) {
//     function send() {
//         var nicknamevalue = (document.getElementById("nickname").value);
//         var scorevalue = (document.getElementById("hiddenscore").value);
//         var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
//         xmlhttp.open("POST", "http://dinorun.io/create");
//         xmlhttp.setRequestHeader("Content-type", "application/json");
//         xmlhttp.send(JSON.stringify({'nickname': nicknamevalue, 'score': scorevalue}));
//         document.getElementById('inputbox').style.display = "none";
//         document.getElementById('submitted').style.display = "block";
//     }} else {
//     function noHack() {
//         alert('No Hacking Silly');
//     }
// }
//
// document.addEventListener('DOMContentLoaded', function () {
//   document.querySelector('button').addEventListener('click', send || noHack);
// });

    function send() {
        var nicknamevalue = (document.getElementById("nickname").value);
        var scorevalue = (document.getElementById("hiddenscore").value);
        var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
        xmlhttp.open("POST", "http://dinorun.io/create");
        xmlhttp.setRequestHeader("Content-type", "application/json");
        xmlhttp.send(JSON.stringify({'nickname': nicknamevalue, 'score': scorevalue}));
        document.getElementById('inputbox').style.display = "none";
        document.getElementById('submitted').style.display = "block";
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('button').addEventListener('click', send);
});
