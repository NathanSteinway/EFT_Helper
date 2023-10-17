const calibreBtns = document.getElementsByClassName('myButton');

for (var i = 0; i < calibreBtns.length; i++) {
    calibreBtns[i].addEventListener('click', function (event) {

        let name = event.target.value

        fetch('https://api.tarkov.dev/graphql', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({
                query: `{
                            items(name: "${name}") {
                                id
                                name
                                shortName
                            }
                        }`
            })
        })
            .then(r => r.json())
            .then(data => console.log('data returned:', data));
    });
}
