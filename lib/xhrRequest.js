xhrRequests = {};


xhrRequests.SoundRequest = function(url) {
    
    var soundRequest = new XMLHttpRequest();
    soundRequest.open('GET', url, true);
    soundRequest.responseType = 'arraybuffer';
    
    
	soundRequest.onload = function () {

		try {
			var context = new webkitAudioContext();

			var mainNode = context.createGainNode(0);
			mainNode.connect(context.destination);

			var clip = context.createBufferSource();

			context.decodeAudioData(soundRequest.response, function (buffer) {
				clip.buffer = buffer;
				clip.gain.value = 1.0;
				clip.connect(mainNode);
				clip.loop = false;
				clip.noteOn(0);
			}, function (data) {});
		}
		catch(e) {
			//console.warn('Web Audio API is not supported in this browser');
			console.log(e);
		}
	};

	soundRequest.send();
};

xhrRequests.JsonRequest = function (url) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.send();
	return JSON.parse(xhr.responseText);
};

xhrRequests.ImageRequest = function (url) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.responseType = "blob";
	xhr.send()
	var img = new Image();
	img.src = window.URL.createObjectURL(xhr.response);
	return img;
};

xhrRequests.GetRequest = function (url, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.onload = (callback === undefined)?null:callback;
	xhr.send();
	return xhr.response;
};

xhrRequests.PostRequest = function (url, requests, callback) {
	var xhr = new XMLHttpRequest();
	xhr.open("POST", url, true);
	xhr.onload = (callback === undefined)?null:callback;
	xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	var requestStr = "";
	for (var header in requests) {
		requestStr += (header+"="+requests[header].toString()+"&");
	}
	xhr.send(requestStr);
	return xhr.response;
}

xhrRequests.PlaySound = function (url, loop, id) {
	var elem = document.getElementById(id);
	elem.innerHTML = "<embed hidden='true' src='" + url + "' loop='" + loop + "' autostart='true'>";
}


