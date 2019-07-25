var quotes = [
  {
    quote: "I solemnly promise that I won't talk in class.",
    author: "Vasudev"
  },
  {
    quote: "Once I see some homework, I stop not until it's done.",
    author: "Jegan"
  },
  { quote: "Phones are best when kept switched off.", author: "Ramya" },
  { quote: "I shall not leave the first bench empty.", author: "Poornima" },
  {
    quote: "Homework done today is better than homework done tomorrow.",
    author: "Alan"
  },

  {
    quote: "GitHub is my holy book.",
    author: "Dinesh"
  },

  {
    quote: "Frontend and backend makes the complete man/woman.",
    author: "Abhirath Mahipal"
  },

  {
    quote: "East or west homework is the best.",
    author: "Alan"
  }
];

function generateRandomQuote() {
  // get random quote from our list
  var randomQuote = quotes[Math.floor(Math.random() * quotes.length)];

  // fill box with the randomly generated quote
  var quoteP = document.getElementById("quote-text");
  var authorP = document.getElementById("quote-author");

  quoteP.innerText = randomQuote["quote"];
  authorP.innerText = randomQuote["author"];
}
