document.addEventListener('DOMContentLoaded', () => {
    const nextBtn = document.getElementById('next-btn');

    const getCards = () => [...document.querySelectorAll('.flashcard')];

    const showCard = (index) => {
        const cards = getCards();
        if (!cards.length) return;

        // Нормализуем индекс (поддержка отрицательных и переполнения)
        index = ((index % cards.length) + cards.length) % cards.length;

        cards.forEach((card, i) => {
            const isActive = i === index;
            card.classList.toggle('active', isActive);
            if (!isActive) card.classList.remove('flipped');
        });
    };

    // Переворот карточки по клику
    getCards().forEach(card => {
        card.addEventListener('click', () => card.classList.toggle('flipped'));
    });

    // Кнопка "следующая"
    nextBtn?.addEventListener('click', () => {
        const cards = getCards();
        if (!cards.length) return;

        if (cards.length === 1) {
            cards[0].classList.remove('flipped');
            return;
        }

        const current = cards.findIndex(c => c.classList.contains('active'));
        showCard(current + 1);
    });

    // Формы действий (удалить / выучено)
    document.querySelectorAll('.action-form').forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const card = form.closest('.flashcard');
            if (!card) return;

            const response = await fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
            });

            if (!response.ok) return;

            const action = form.dataset.action;

            if (action === 'delete') {
                const cards = getCards();
                const index = cards.indexOf(card);
                card.remove();

                const remaining = getCards();
                if (remaining.length) {
                    showCard(Math.min(index, remaining.length - 1));
                } else {
                    nextBtn?.closest('.card-controls')?.remove();
                }
                return;
            }

            if (action === 'learned') {
                const data = await response.json();
                card.querySelectorAll('.btn-learned').forEach(btn => {
                    btn.classList.toggle('is-learned', !!data.is_learned);
                    btn.title = data.is_learned ? 'Marked as learned' : 'Mark as learned';
                });
            }
        });
    });
});