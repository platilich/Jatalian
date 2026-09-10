// 1. Клик по карточке — переворачиваем её
document.querySelectorAll('.flashcard').forEach(card => {
    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });
});

// 2. Клик по кнопке — переключаем на следующую карточку
const nextBtn = document.getElementById('next-btn');
if (nextBtn) {
    nextBtn.addEventListener('click', () => {
        const cards = document.querySelectorAll('.flashcard');
        let activeIndex = -1;

        cards.forEach((card, index) => {
            if (card.classList.contains('active')) {
                activeIndex = index;
            }
        });

        if (activeIndex !== -1) {
            // Убираем показ и переворот с текущей карточки
            cards[activeIndex].classList.remove('active', 'flipped');

            // Показываем следующую по кругу
            const nextIndex = (activeIndex + 1) % cards.length;
            cards[nextIndex].classList.add('active');
        }
    });
}