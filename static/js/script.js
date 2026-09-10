document.addEventListener('DOMContentLoaded', () => {
    // 1. Клик по карточке — переворачиваем её
    const cards = document.querySelectorAll('.flashcard');
    cards.forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });
    });

    // 2. Клик по кнопке Next Word — строго последовательное переключение
    const nextBtn = document.getElementById('next-btn');
    if (nextBtn && cards.length > 0) {
        let currentIndex = 0;

        nextBtn.addEventListener('click', () => {
            // Если карточка всего одна, просто переворачиваем её обратно на переднюю сторону
            if (cards.length === 1) {
                cards[0].classList.remove('flipped');
                return;
            }

            // Убираем активность и переворот с текущей карточки
            cards[currentIndex].classList.remove('active', 'flipped');

            // Переходим к следующему индексу по порядку
            currentIndex = (currentIndex + 1) % cards.length;

            // Показываем новую карточку
            cards[currentIndex].classList.add('active');
        });
    }
});


