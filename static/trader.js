document.querySelectorAll('.traderBtn').forEach(button => {
    button.addEventListener('click', function(event) {
        const trader = event.target.value;

        console.log(trader)

        document.querySelectorAll('tbody tr').forEach(row => {
            row.style.display = 'none';
        });

        document.querySelectorAll(`tbody tr[data-quests="${trader}"]`).forEach(row => {
            row.style.display = '';
        });
    })
})