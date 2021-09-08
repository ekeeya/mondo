
function run_waitMe(){
$('#spinner-wrapper').waitMe({

effect: 'win8_linear',
text: 'Please wait ...',
bg: 'rgba(249,251,253,255)',
color: '#002b49',
maxSize: '20pt',
waitTime: -1,
source: '',
textPos: 'vertical',
fontSize: '',
onClose: function() {}

});
}

function hide_waitMe(){
    $('#spinner-wrapper').waitMe("hide");
}