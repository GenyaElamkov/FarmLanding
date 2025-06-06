    $(document).ready(function() {
        // Показ/скрытие кнопки "Наверх"
        function toggleBackToTop() {
            if (window.pageYOffset > 300) {
                document.querySelector('.back-to-top').classList.add('active');
            } else {
                document.querySelector('.back-to-top').classList.remove('active');
            }
        }

        // Изменение навбара при прокрутке
        function navbarOnScroll() {
            if (window.scrollY > 50) {
                document.querySelector('.navbar').classList.add('scrolled');
            } else {
                document.querySelector('.navbar').classList.remove('scrolled');
            }
        }

        // Обработчики событий
        window.addEventListener('scroll', () => {
            toggleBackToTop();
            navbarOnScroll();
        });

        // Плавная прокрутка для всех ссылок
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });

        // Инициализация анимации при загрузке
        toggleBackToTop();
        navbarOnScroll();
    });
