document.querySelectorAll('.caliberBtn').forEach(button => {
    button.addEventListener('click', function(event) {
        const caliber = event.target.value;

        console.log(caliber)

        document.querySelectorAll('tbody tr').forEach(row => {
            row.style.display = 'none';
        });

        document.querySelectorAll(`tbody tr[data-caliber="${caliber}"]`).forEach(row => {
            row.style.display = '';
        });
    })
})