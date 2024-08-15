const imageInput = document.getElementById('id_image');
const imageEvent = document.getElementById('img-event');

imageInput.addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            imageEvent.src = e.target.result;
            imageEvent.style.display = 'block';
        }

        reader.readAsDataURL(file);
    } else {
        imageEvent.src = '';
        imageEvent.style.display = 'none';
    }
});