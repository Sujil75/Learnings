const items = [
    "Welcome to our website",
    "Learn HTML CSS JavaScript",
    "Build amazing projects",
    "Create beautiful animations"
];

const display = document.getElementById('display');
let index = 0;

function TypeEachLetter(text) {
    crrText = '';
    crrIdx = 0;

    const typeInterval = setInterval(() => {
        crrText += text[crrIdx];
        display.textContent = crrText + '|';

        crrIdx++;

        if (crrIdx === text.length) {
            clearInterval(typeInterval);

            setTimeout(() => {
                const deleteInterval = setInterval(() => {
                    crrText = crrText.slice(0, -1);
                    display.textContent = crrText + '|';

                    if (crrText.length === 0) {
                        clearInterval(deleteInterval);

                        index = (index + 1) % items.length;

                        setTimeout(() => {
                            TypeEachLetter(items[index])
                        }, 1000)
                    };
                }, 100);
            }, 1000);
        };
    }, 100);
}

TypeEachLetter(items[index])