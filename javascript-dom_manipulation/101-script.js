document.addEventListener("DOMContentLoaded", () => {
    const translateButton = document.getElementById('btn_translate');
    const languageSelect = document.getElementById('language_code');
    const helloDiv = document.getElementById('hello');

    translateButton.addEventListener('click', async () => {
        const languageCode = languageSelect.value;
        if (languageCode) {
            try {
                const response = await fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                helloDiv.textContent = data.hello;
            } catch (error) {
                console.error('Error fetching translation:', error);
                helloDiv.textContent = 'Error fetching translation';
            }
        } else {
            helloDiv.textContent = 'Please select a language';
        }
    });
});
