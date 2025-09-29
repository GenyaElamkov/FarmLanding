    document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.getElementById('farmCarousel');
    const modal = new bootstrap.Modal(document.getElementById('imageModal'));

    // Открытие модального окна при клике на изображение в карусели
    carousel.addEventListener('click', function(e) {
        if (e.target.classList.contains('d-block')) {
            const imgSrc = e.target.src;
            const imgAlt = e.target.alt;

            document.getElementById('modalImage').src = imgSrc;
            document.getElementById('imageModalLabel').textContent = imgAlt;
            modal.show();
        }
    });

    // Подсветка активной миниатюры
    carousel.addEventListener('slid.bs.carousel', function(e) {
        const thumbnails = document.querySelectorAll('.img-thumbnail');
        thumbnails.forEach((thumb, index) => {
            thumb.classList.toggle('active', index === e.to);
        });
    });
});