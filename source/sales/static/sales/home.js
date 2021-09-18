const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

if (img) {
    reportBtn.classList.remove('hid')
}