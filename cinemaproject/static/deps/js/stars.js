document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.star');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const value = parseInt(this.getAttribute('data-value'));
            const ratingInput = document.getElementById('rating');
            ratingInput.value = value;

            // Убираем активный класс у всех звезд
            stars.forEach(s => s.classList.remove('active'));

            // Добавляем активный класс только кликнутой звезде и всем до нее
            for (let i = 0; i < value; i++) {
                stars[i].classList.add('active');
            }
        });
    });
});
