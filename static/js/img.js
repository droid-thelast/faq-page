    ImageArray = new Array();
    ImageArray[0] = 'bwala-faq.jpeg';
    ImageArray[1] = 'bwala-faq-3.jpeg';
    ImageArray[2] = 'bwala-faq-2.jpeg';


function getRandomImage() {
    var num = Math.floor( Math.random() * 4);
    var img = ImageArray[num];
    document.getElementById("randImage").innerHTML = ('<img src="' + '' + img + '" width="100%">')

}