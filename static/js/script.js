document.addEventListener('DOMContentLoaded', () => {
    const nextBtn = document.getElementById('next-btn');

    const getCards = () => Array.from(document.querySelectorAll('.flashcard'));

    const showCard = (index) => {
        const cards = getCards();
        if (!cards.length) return;

        const nextIndex = ((index % cards.length) + cards.length) % cards.length;
        cards.forEach((card, i) => {
            const isActive = i === nextIndex;
            card.classList.toggle('active', isActive);
            if (!isActive) card.classList.remove('flipped');
        });
    };

    getCards().forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });
    });

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const cards = getCards();
            if (!cards.length) return;

            if (cards.length === 1) {
                cards[0].classList.remove('flipped');
                return;
            }

            const currentIndex = cards.findIndex(card => card.classList.contains('active'));
            showCard(currentIndex + 1);
        });
    }

    document.querySelectorAll('.action-form').forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const action = form.dataset.action;
            const card = form.closest('.flashcard');
            const response = await fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
            });

            if (!response.ok || !card) return;

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
                    btn.classList.toggle('is-learned', Boolean(data.is_learned));
                    btn.title = data.is_learned ? 'Marked as learned' : 'Mark as learned';
                });
            }
        });
    });
});


