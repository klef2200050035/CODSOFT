document.addEventListener('DOMContentLoaded', function() {
    const quoteContainer = document.getElementById('quote-container');
    const quoteText = document.getElementById('quote');
    const authorText = document.getElementById('author');
    const newQuoteButton = document.getElementById('new-quote');
    const shareQuoteButton = document.getElementById('share-quote');
    const saveFavoriteButton = document.getElementById('save-favorite');
    const favoritesList = document.getElementById('favorites-list');

    const quotes = [
        { text: "The best way to get started is to quit talking and begin doing.", author: "Walt Disney" },
        { text: "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.", author: "Winston Churchill" },
        { text: "Don't let yesterday take up too much of today.", author: "Will Rogers" },
        // Add more quotes as desired
    ];

    let favorites = JSON.parse(localStorage.getItem('favorites')) || [];

    function getRandomQuote() {
        const randomIndex = Math.floor(Math.random() * quotes.length);
        return quotes[randomIndex];
    }

    function displayQuote(quote) {
        quoteText.textContent = quote.text;
        authorText.textContent = quote.author ? `- ${quote.author}` : '- Unknown';
    }

    function loadFavorites() {
        favoritesList.innerHTML = '';
        favorites.forEach(favorite => {
            const li = document.createElement('li');
            li.textContent = `${favorite.text} ${favorite.author ? '- ' + favorite.author : '- Unknown'}`;
            favoritesList.appendChild(li);
        });
    }

    function saveFavorite() {
        const currentQuote = {
            text: quoteText.textContent,
            author: authorText.textContent.replace('- ', '')
        };
        favorites.push(currentQuote);
        localStorage.setItem('favorites', JSON.stringify(favorites));
        loadFavorites();
    }

    function shareQuote() {
        const currentQuote = `${quoteText.textContent} ${authorText.textContent}`;
        if (navigator.share) {
            navigator.share({
                title: 'Inspiring Quote',
                text: currentQuote
            }).catch(error => console.log('Error sharing', error));
        } else {
            alert('Sharing not supported on this browser.');
        }
    }

    newQuoteButton.addEventListener('click', () => displayQuote(getRandomQuote()));
    shareQuoteButton.addEventListener('click', shareQuote);
    saveFavoriteButton.addEventListener('click', saveFavorite);

    // Display a random quote on load
    displayQuote(getRandomQuote());
    loadFavorites();
});
