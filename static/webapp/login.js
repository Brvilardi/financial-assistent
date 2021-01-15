
function eyeOpened(element){
    return element.dataset.status === "opened";
}

function eyeClosed(element){
    return element.dataset.status === "closed";
}

function getImgUrl(img){

    var url = img.src.split("/");
    url.pop();
    return url.join("/") + "/";
}

document.addEventListener('DOMContentLoaded', function() {
    var lock = document.getElementById("lock");
    var passwordInput = document.getElementById("password");
    var imgUrl = getImgUrl(lock);

    var eyeOpenedUrl = imgUrl + "eyeOpen.svg";
    var eyeClosedUrl = imgUrl + "eyeClose.svg";
    
    lock.addEventListener('click', function (){
        if (eyeOpened(lock)){
            lock.dataset.status = "closed";
            lock.src = eyeClosedUrl;
            passwordInput.type = "password";
        }
        else{
            lock.dataset.status = "opened";
            lock.src = eyeOpenedUrl;
            passwordInput.type = "text";            
        }
    })
 }, false);