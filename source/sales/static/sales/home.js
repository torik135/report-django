const reportBtn = document.getElementById('report-btn')
const img = document.getElementById('img')

if (img) {
    reportBtn.classList.remove('hid')
}

// modal
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
})