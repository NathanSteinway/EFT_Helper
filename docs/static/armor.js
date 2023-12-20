document.querySelectorAll('.armorClass').forEach(button => {
    button.addEventListener('click', function(event) {
        const armorLvl = event.target.value;

        let chart = document.querySelector('.armor-box')

        chart.style.visibility = 'visible';

        console.log(armorLvl)

        document.querySelectorAll('tbody tr').forEach(row => {
            row.style.display = 'none';
        });

        document.querySelectorAll(`tbody tr[data-armor="${armorLvl}"]`).forEach(row => {
            row.style.display = '';
        });
    })
})