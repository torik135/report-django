const reportBtn = document.getElementById('report-btn')
const img1 = document.getElementById('img')
const modalBody = document.getElementById('modal1')

if (img1) {
    reportBtn.classList.remove('hid')
}

reportBtn.addEventListener('click', () => {
    console.log('report btn')
    img.setAttribute('width', '90%')
    modalBody.prepend(img1)
})

// modal
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
})

