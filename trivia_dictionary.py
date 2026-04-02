""" Trivia dictionary, sorted by category, and difficulty. """

trivia_categories = {
    "Animals": {
        "easy": [{
            "question": "What is the largest land animal?",
            "choices": ["Asian Elephant", "Hippopotamus", "African Elephant", "White Rhinoceros"], 
            "correct_answer": "African Elephant",
            "points": 1
        }, 
            {
            "question": "What is the fastest land animal?",
            "choices": ["Cheetah", "Lion", "Greyhound", "Pronghorn"],
            "correct_answer": "Cheetah",
            "points": 1
        },
            {
            "question": "How many legs does a spider have?",
            "choices": ["6", "8", "10", "12"],
            "correct_answer": "8",
            "points": 1
        },
            {
            "question": "What is a group of lions called?",
            "choices": ["Herd", "Pack", "Pride", "Flock"],
            "correct_answer": "Pride",
            "points": 1
        },
            {
            "question": "Which animal is known for its black and white stripes?",
            "choices": ["Cheetah", "Giraffe", "Leopard", "Zebra"],
            "correct_answer": "Zebra",
            "points": 1
        }],
        "medium": [{
            "question": "Which bird is best known for mimicking human speech?",
            "choices": ["Crow", "Parrot", "Pigeon", "Starling"], 
            "correct_answer": "Parrot",
            "points": 2
        }, 
            {
            "question": "What is the largest species of shark?",
            "choices": ["Bull Shark", "Great White Shark", "Hammerhead Shark", "Whale Shark"],
            "correct_answer": "Whale Shark",
            "points": 2
        },
            {
            "question": "Which mammal lays eggs?",
            "choices": ["Bat", "Dolphin", "Platypus", "Seal"],
            "correct_answer": "Platypus",
            "points": 2
        },
            {
            "question": "How many hearts does an octopus have?",
            "choices": ["1", "3", "2", "4"],
            "correct_answer": "3",
            "points": 2
        },
            {
            "question": "What is the tallest living animal?",
            "choices": ["African Elephant", "Hippopotamus", "Giraffe", "Polar Bear"],
            "correct_answer": "Giraffe",
            "points": 2
        }], 
        "hard": [{
            "question": "What is the only marsupial native to North America?",
            "choices": ["Kangaroo", "Koala", "Opossum", "Wombat"], 
            "correct_answer": "Opossum",
            "points": 3
        }, 
            {
            "question": "What is the scientific name for the domestic cat?",
            "choices": ["Felis catus", "Felis leo", "Felis pardus", "Felis tigris"],
            "correct_answer": "Felis catus",
            "points": 3
        },
            {
            "question": "Which bird has the largest wingspan?",
            "choices": ["Andean Condor", "Wandering Albatross", "California Condor", "Dalmatian Pelican"],
            "correct_answer": "Wandering Albatross",
            "points": 3
        },
            {
            "question": "What is the only venomous primate?",
            "choices": ["Aye-aye", "Tarsier", "Tree Shrew", "Slow Loris"],
            "correct_answer": "Slow Loris",
            "points": 3
        },
            {
            "question": "How many chromosomes does a dog have?",
            "choices": ["46", "52", "78", "84"],
            "correct_answer": "78",
            "points": 3
        }],
    }, 
    "Art": {
        "easy": [{
            "question": "Who painted the Mona Lisa?",
            "choices": ["Donatello", "Leonardo da Vinci", "Michelangelo", "Raphael"], 
            "correct_answer": "Leonardo da Vinci",
            "points": 1
        }, 
            {
            "question": "What are the three primary colors?",
            "choices": ["Red, Blue, Yellow", "Red, Green, Blue", "Red, White, Blue", "Orange, Green, Purple"],
            "correct_answer": "Red, Blue, Yellow",
            "points": 1
        },
            {
            "question": "Which artist is famous for cutting off part of his own ear?",
            "choices": ["Claude Monet", "Pablo Picasso", "Paul Gauguin", "Vincent van Gogh"],
            "correct_answer": "Vincent van Gogh",
            "points": 1
        },
            {
            "question": "What is the art of folding paper into shapes called?",
            "choices": ["Calligraphy", "Ikebana", "Origami", "Sumi-e"],
            "correct_answer": "Origami",
            "points": 1
        },
            {
            "question": "Which country is famous for the art style of Impressionism?",
            "choices": ["Germany", "France", "Italy", "Spain"],
            "correct_answer": "France",
            "points": 1
        }],
        "medium": [{
            "question": "Which art movement did Pablo Picasso help to found?",
            "choices": ["Baroque", "Cubism", "Impressionism", "Surrealism"], 
            "correct_answer": "Cubism",
            "points": 2
        }, 
            {
            "question": "What painting technique uses small dots of color?",
            "choices": ["Fresco", "Impasto", "Pointillism", "Watercolor"],
            "correct_answer": "Pointillism",
            "points": 2
        },
            {
            "question": "Which artist painted the Sistine Chapel ceiling?",
            "choices": ["Botticelli", "Donatello", "Leonardo da Vinci", "Michelangelo"],
            "correct_answer": "Michelangelo",
            "points": 2
        },
            {
            "question": "What nationality was artist Frida Kahlo?",
            "choices": ["Mexican", "Argentine", "Brazilian", "Spanish"],
            "correct_answer": "Mexican",
            "points": 2
        },
            {
            "question": "Which art movement is Salvador Dali associated with?",
            "choices": ["Dadaism", "Expressionism", "Surrealism", "Impressionism"],
            "correct_answer": "Surrealism",
            "points": 2
        }],
        "hard": [{
            "question": "Which Dutch artist painted 'The Night Watch'?",
            "choices": ["Jan Steen", "Johannes Vermeer", "Pieter Bruegel", "Rembrandt van Rijn"], 
            "correct_answer": "Rembrandt van Rijn",
            "points": 3
        }, 
            {
            "question": "What is the technique of applying thick paint to canvas called?",
            "choices": ["Chiaroscuro", "Fresco", "Impasto", "Sfumato"],
            "correct_answer": "Impasto",
            "points": 3
        },
            {
            "question": "Which artist created the sculpture 'The Thinker'?",
            "choices": ["Auguste Rodin", "Donatello", "Gian Lorenzo Bernini", "Michelangelo"],
            "correct_answer": "Auguste Rodin",
            "points": 3
        },
            {
            "question": "What does 'chiaroscuro' refer to in art?",
            "choices": ["A type of fresco technique", "The contrast of light and shadow", "Bold use of primary colors", "The use of geometric shapes"],
            "correct_answer": "The contrast of light and shadow",
            "points": 3
        },
            {
            "question": "Which movement did artists Wassily Kandinsky and Franz Marc co-found?",
            "choices": ["Blue Rider", "Cubism", "De Stijl", "Fauvism"],
            "correct_answer": "Blue Rider",
            "points": 3
        }],
    }, 
    "Astronomy & Space": {
        "easy": [{
            "question": "What planet is known as the Red Planet?",
            "choices": ["Jupiter", "Mars", "Mercury", "Venus"], 
            "correct_answer": "Mars",
            "points": 1
        }, 
            {
            "question": "How many planets are in our solar system?",
            "choices": ["7", "10", "8", "9"],
            "correct_answer": "8",
            "points": 1
        },
            {
            "question": "What is the closest star to Earth?",
            "choices": ["Betelgeuse", "Proxima Centauri", "Sirius", "The Sun"],
            "correct_answer": "The Sun",
            "points": 1
        },
            {
            "question": "What do you call a shooting star?",
            "choices": ["Asteroid", "Comet", "Meteor", "Nebula"],
            "correct_answer": "Meteor",
            "points": 1
        },
            {
            "question": "Which planet is known for its rings?",
            "choices": ["Saturn", "Jupiter", "Neptune", "Uranus"],
            "correct_answer": "Saturn",
            "points": 1
        }],
        "medium": [{
            "question": "Which galaxy contains the Earth?",
            "choices": ["Andromeda", "Milky Way", "Triangulum", "Whirlpool"], 
            "correct_answer": "Milky Way",
            "points": 2
        }, 
            {
            "question": "What is the name of NASA's most famous space telescope?",
            "choices": ["Chandra", "James Webb", "Spitzer", "Hubble"],
            "correct_answer": "Hubble",
            "points": 2
        },
            {
            "question": "Who was the first human to walk on the moon?",
            "choices": ["Buzz Aldrin", "John Glenn", "Neil Armstrong", "Yuri Gagarin"],
            "correct_answer": "Neil Armstrong",
            "points": 2
        },
            {
            "question": "What is a light year a measure of?",
            "choices": ["Distance", "Brightness of stars", "Time", "Speed of light"],
            "correct_answer": "Distance",
            "points": 2
        },
            {
            "question": "What is the largest planet in our solar system?",
            "choices": ["Saturn", "Neptune", "Jupiter", "Uranus"],
            "correct_answer": "Jupiter",
            "points": 2
        }],
        "hard": [{
            "question": "What is the name of the boundary around a black hole beyond which nothing can escape?",
            "choices": ["Ergosphere", "Event Horizon", "Photon Sphere", "Singularity"], 
            "correct_answer": "Event Horizon",
            "points": 3
        }, 
            {
            "question": "What is the name of the supermassive black hole at the center of the Milky Way?",
            "choices": ["Cygnus X-1", "M87", "Sagittarius A*", "TON 618"],
            "correct_answer": "Sagittarius A*",
            "points": 3
        },
            {
            "question": "What is the Chandrasekhar limit?",
            "choices": ["Minimum mass for a black hole", "Speed at which galaxies expand", "Maximum brightness of a supernova", "Maximum mass of a stable white dwarf"],
            "correct_answer": "Maximum mass of a stable white dwarf",
            "points": 3
        },
            {
            "question": "What phenomenon causes the redshift of distant galaxies?",
            "choices": ["Black hole gravity", "Cosmic radiation", "Expansion of the universe", "Solar wind"],
            "correct_answer": "Expansion of the universe",
            "points": 3
        },
            {
            "question": "What is the Kuiper Belt?",
            "choices": ["A band of asteroids between Mars and Jupiter", "A region of icy bodies beyond Neptune", "The outer edge of the solar system", "The region around a black hole"],
            "correct_answer": "A region of icy bodies beyond Neptune",
            "points": 3
        }],
    }, 
    "Business & Economics": {
        "easy": [{
            "question": "What does 'GDP' stand for?",
            "choices": ["Gross Domestic Product", "General Domestic Product", "Global Domestic Product", "Gross Domestic Price"], 
            "correct_answer": "Gross Domestic Product",
            "points": 1
        }, 
            {
            "question": "What does 'CEO' stand for?",
            "choices": ["Central Executive Officer", "Chief Executive Officer", "Chief External Officer", "Corporate Executive Operator"],
            "correct_answer": "Chief Executive Officer",
            "points": 1
        },
            {
            "question": "What is the name for the money a business makes after expenses?",
            "choices": ["Revenue", "Assets", "Turnover", "Profit"],
            "correct_answer": "Profit",
            "points": 1
        },
            {
            "question": "What does 'stock' represent in a company?",
            "choices": ["A company's debt", "A company's inventory", "Ownership shares in a company", "The company's annual revenue"],
            "correct_answer": "Ownership shares in a company",
            "points": 1
        },
            {
            "question": "What is the world's largest stock exchange?",
            "choices": ["London Stock Exchange", "New York Stock Exchange", "NASDAQ", "Tokyo Stock Exchange"],
            "correct_answer": "New York Stock Exchange",
            "points": 1
        }],
        "medium": [{
            "question": "What term describes a market dominated by a single seller?",
            "choices": ["Monopoly", "Monopsony", "Oligopoly", "Perfect Competition"], 
            "correct_answer": "Monopoly",
            "points": 2
        }, 
            {
            "question": "What does 'IPO' stand for?",
            "choices": ["Initial Private Offering", "Initial Public Offering", "International Purchase Order", "Investment Portfolio Option"],
            "correct_answer": "Initial Public Offering",
            "points": 2
        },
            {
            "question": "What economic term describes a period of two consecutive quarters of negative GDP growth?",
            "choices": ["Depression", "Deflation", "Recession", "Stagflation"],
            "correct_answer": "Recession",
            "points": 2
        },
            {
            "question": "Which of these is an example of a fixed cost?",
            "choices": ["Rent", "Electricity bills", "Raw materials", "Sales commissions"],
            "correct_answer": "Rent",
            "points": 2
        },
            {
            "question": "What is 'supply and demand'?",
            "choices": ["A government pricing strategy", "A model describing price determination in a market", "A stock market trading technique", "An accounting principle"],
            "correct_answer": "A model describing price determination in a market",
            "points": 2
        }],
        "hard": [{
            "question": "Economically, what is 'inflation'?",
            "choices": ["A decrease in overall price levels", "A one-time increase in a single commodity's price", "A sustained general increase in prices and fall in purchasing power", "Government-imposed price controls"], 
            "correct_answer": "A sustained general increase in prices and fall in purchasing power",
            "points": 3
        }, 
            {
            "question": "What is the 'invisible hand' concept in economics associated with?",
            "choices": ["John Maynard Keynes", "Karl Marx", "Milton Friedman", "Adam Smith"],
            "correct_answer": "Adam Smith",
            "points": 3
        },
            {
            "question": "What does 'quantitative easing' involve?",
            "choices": ["Central bank buying securities to increase money supply", "Government cutting taxes to stimulate growth", "Raising interest rates to reduce inflation", "Reducing government spending to balance budget"],
            "correct_answer": "Central bank buying securities to increase money supply",
            "points": 3
        },
            {
            "question": "What is the 'Nash Equilibrium' in game theory?",
            "choices": ["A market with perfect competition", "A outcome where no player benefits from changing strategy unilaterally", "The point where supply meets demand", "When all players cooperate for maximum gain"],
            "correct_answer": "A outcome where no player benefits from changing strategy unilaterally",
            "points": 3
        },
            {
            "question": "What is 'stagflation'?",
            "choices": ["High growth with low inflation", "Low growth with deflation", "Rapid economic expansion", "Stagnant growth combined with high inflation"],
            "correct_answer": "Stagnant growth combined with high inflation",
            "points": 3
        }],
    }, 
    "Famous Quotes": {
        "easy": [{
            "question": "Who said 'I have a dream'?",
            "choices": ["Malcolm X", "Martin Luther King Jr.", "Nelson Mandela", "Rosa Parks"], 
            "correct_answer": "Martin Luther King Jr.",
            "points": 1
        }, 
            {
            "question": "Who said 'To be, or not to be'?",
            "choices": ["Christopher Marlowe", "John Milton", "William Shakespeare", "William Wordsworth"],
            "correct_answer": "William Shakespeare",
            "points": 1
        },
            {
            "question": "Who is credited with saying 'I think, therefore I am'?",
            "choices": ["Aristotle", "Plato", "Socrates", "René Descartes"],
            "correct_answer": "René Descartes",
            "points": 1
        },
            {
            "question": "Who said 'The only thing we have to fear is fear itself'?",
            "choices": ["Franklin D. Roosevelt", "Abraham Lincoln", "John F. Kennedy", "Winston Churchill"],
            "correct_answer": "Franklin D. Roosevelt",
            "points": 1
        },
            {
            "question": "Who said 'Float like a butterfly, sting like a bee'?",
            "choices": ["Joe Frazier", "Muhammad Ali", "Rocky Marciano", "Sugar Ray Leonard"],
            "correct_answer": "Muhammad Ali",
            "points": 1
        }],
        "medium": [{
            "question": "Who said 'In the middle of difficulty lies opportunity'?",
            "choices": ["Albert Einstein", "Isaac Newton", "Marie Curie", "Nikola Tesla"],
            "correct_answer": "Albert Einstein",
            "points": 2
        }, 
            {
            "question": "Who said 'That's one small step for man, one giant leap for mankind'?",
            "choices": ["Buzz Aldrin", "John Glenn", "Neil Armstrong", "Yuri Gagarin"],
            "correct_answer": "Neil Armstrong",
            "points": 2
        },
            {
            "question": "Who wrote 'In the beginning was the Word'?",
            "choices": ["Isaiah", "John", "Luke", "Matthew"],
            "correct_answer": "John",
            "points": 2
        },
            {
            "question": "Who said 'Give me liberty, or give me death'?",
            "choices": ["Benjamin Franklin", "George Washington", "Patrick Henry", "Thomas Jefferson"],
            "correct_answer": "Patrick Henry",
            "points": 2
        },
            {
            "question": "Who said 'The ends justify the means'?",
            "choices": ["Karl Marx", "Machiavelli", "Napoleon Bonaparte", "Voltaire"],
            "correct_answer": "Machiavelli",
            "points": 2
        }],
        "hard": [{
            "question": "Which U.S. President said 'Speak softly and carry a big stick'?",
            "choices": ["Franklin D. Roosevelt", "Harry S. Truman", "Theodore Roosevelt", "Woodrow Wilson"], 
            "correct_answer": "Theodore Roosevelt",
            "points": 3          
        }, 
            {
            "question": "Who said 'Well-behaved women seldom make history'?",
            "choices": ["Laurel Thatcher Ulrich", "Betty Friedan", "Gloria Steinem", "Simone de Beauvoir"],
            "correct_answer": "Laurel Thatcher Ulrich",
            "points": 3
        },
            {
            "question": "Who said 'The reports of my death are greatly exaggerated'?",
            "choices": ["Benjamin Disraeli", "Mark Twain", "Oscar Wilde", "Winston Churchill"],
            "correct_answer": "Mark Twain",
            "points": 3
        },
            {
            "question": "Who wrote 'No man is an island, entire of itself'?",
            "choices": ["Francis Bacon", "John Donne", "John Milton", "William Shakespeare"],
            "correct_answer": "John Donne",
            "points": 3
        },
            {
            "question": "Who said 'Injustice anywhere is a threat to justice everywhere'?",
            "choices": ["Cesar Chavez", "Malcolm X", "Martin Luther King Jr.", "Nelson Mandela"],
            "correct_answer": "Martin Luther King Jr.",
            "points": 3
        }],
    },
    "Food & Drink": {
        "easy": [{
            "question": "Sushi originated in which country?",
            "choices": ["China", "Japan", "Korea", "Thailand"], 
            "correct_answer": "Japan",
            "points": 1
        }, 
            {
            "question": "What is the main ingredient in guacamole?",
            "choices": ["Avocado", "Mango", "Tomato", "Tomatillo"],
            "correct_answer": "Avocado",
            "points": 1
        },
            {
            "question": "Which fruit is known as the 'king of fruits' in Southeast Asia?",
            "choices": ["Jackfruit", "Mango", "Papaya", "Durian"],
            "correct_answer": "Durian",
            "points": 1
        },
            {
            "question": "What type of pastry is used to make a croissant?",
            "choices": ["Choux", "Filo", "Puff", "Shortcrust"],
            "correct_answer": "Puff",
            "points": 1
        },
            {
            "question": "Which country is the largest producer of coffee?",
            "choices": ["Colombia", "Ethiopia", "Brazil", "Vietnam"],
            "correct_answer": "Brazil",
            "points": 1
        }],
        "medium": [{
            "question": "Which cheese is traditionally used on a Greek salad?",
            "choices": ["Cheddar", "Feta", "Gouda", "Mozzarella"], 
            "correct_answer": "Feta",
            "points": 2
        }, 
            {
            "question": "What is the primary ingredient in hummus?",
            "choices": ["Black beans", "Lentils", "White beans", "Chickpeas"],
            "correct_answer": "Chickpeas",
            "points": 2
        },
            {
            "question": "Which Italian city is credited with inventing pizza?",
            "choices": ["Florence", "Milan", "Naples", "Rome"],
            "correct_answer": "Naples",
            "points": 2
        },
            {
            "question": "What gives red wine its color?",
            "choices": ["Added coloring", "Grape juice concentrate", "Grape skins", "Oak barrel aging"],
            "correct_answer": "Grape skins",
            "points": 2
        },
            {
            "question": "What is 'Wagyu' famous for?",
            "choices": ["Being a type of highly marbled beef", "Being a Japanese rice dish", "Being an expensive seafood", "Being a rare Japanese mushroom"],
            "correct_answer": "Being a type of highly marbled beef",
            "points": 2
        }],
        "hard": [{
            "question": "What chemical compound is primarily responsible for the heat in chili peppers?",
            "choices": ["Allyl isothiocyanate", "Capsaicin", "Curcumin", "Piperine"], 
            "correct_answer": "Capsaicin",
            "points": 3
        }, 
            {
            "question": "What is the Scoville scale used to measure?",
            "choices": ["Acidity in wine", "Bitterness in coffee", "Saltiness in cheese", "Spiciness of chili peppers"],
            "correct_answer": "Spiciness of chili peppers",
            "points": 3
        },
            {
            "question": "Which enzyme found in pineapple can break down proteins?",
            "choices": ["Amylase", "Bromelain", "Lactase", "Papain"],
            "correct_answer": "Bromelain",
            "points": 3
        },
            {
            "question": "What is the traditional base spirit in a classic Negroni cocktail?",
            "choices": ["Gin", "Rum", "Tequila", "Vodka"],
            "correct_answer": "Gin",
            "points": 3
        },
            {
            "question": "Which country of origin does the cheese Manchego come from?",
            "choices": ["France", "Italy", "Portugal", "Spain"],
            "correct_answer": "Spain",
            "points": 3
        }],
    }, 
    "Games": {
        "easy": [{
            "question": "Which chess piece moves in an L-shape?",
            "choices": ["Bishop", "Knight", "Queen", "Rook"], 
            "correct_answer": "Knight",
            "points": 1
        },
            {
            "question": "How many squares are on a standard chessboard?",
            "choices": ["32", "48", "64", "72"],
            "correct_answer": "64",
            "points": 1
        },
            {
            "question": "In Monopoly, what is the most expensive property?",
            "choices": ["Boardwalk", "Mayfair", "Park Place", "Park Lane"],
            "correct_answer": "Boardwalk",
            "points": 1
        },
            {
            "question": "How many dots are on a standard die?",
            "choices": ["18", "20", "21", "24"],
            "correct_answer": "21",
            "points": 1
        },
            {
            "question": "In which card game do players try to get a hand value of 21?",
            "choices": ["Baccarat", "Blackjack", "Poker", "Rummy"],
            "correct_answer": "Blackjack",
            "points": 1
        }],
        "medium": [{
            "question": "How many tiles are in a standard English-language Scrabble set?",
            "choices": ["96", "98", "100", "104"], 
            "correct_answer": "100",
            "points": 2
        }, 
            {
            "question": "In chess, which piece can only move diagonally?",
            "choices": ["Bishop", "King", "Pawn", "Rook"],
            "correct_answer": "Bishop",
            "points": 2
        },
            {
            "question": "What is the maximum score in a single game of ten-pin bowling?",
            "choices": ["250", "200", "350", "300"],
            "correct_answer": "300",
            "points": 2
        },
            {
            "question": "In poker, what hand beats a flush?",
            "choices": ["Straight", "Two Pair", "Full House", "Three of a Kind"],
            "correct_answer": "Full House",
            "points": 2
        },
            {
            "question": "How many cards are in a standard deck excluding jokers?",
            "choices": ["48", "52", "50", "54"],
            "correct_answer": "52",
            "points": 2
        }],
        "hard": [{
            "question": "In contract bridge, how many tricks are there in one hand?",
            "choices": ["10", "12", "13", "16"], 
            "correct_answer": "13",
            "points": 3
        }, 
            {
            "question": "In which game would you use a 'Sicilian Defense'?",
            "choices": ["Backgammon", "Chess", "Checkers", "Go"],
            "correct_answer": "Chess",
            "points": 3
        },
            {
            "question": "How many points is the letter 'Q' worth in Scrabble?",
            "choices": ["8", "12", "15", "10"],
            "correct_answer": "10",
            "points": 3
        },
            {
            "question": "In the board game Risk, how many territories are there?",
            "choices": ["36", "40", "42", "48"],
            "correct_answer": "42",
            "points": 3
        },
            {
            "question": "What is the name of the highest ranking hand in poker?",
            "choices": ["Four of a Kind", "Royal Flush", "Straight Flush", "Full House"],
            "correct_answer": "Royal Flush",
            "points": 3
        }],
    },
    "General Knowledge": {
        "easy": [{
            "question": "What color do you get by mixing red and blue paint?",
            "choices": ["Brown", "Green", "Orange", "Purple"], 
            "correct_answer": "Purple",
            "points": 1
        }, 
            {
            "question": "How many sides does a hexagon have?",
            "choices": ["5", "6", "7", "8"],
            "correct_answer": "6",
            "points": 1
        },
            {
            "question": "What is the capital of France?",
            "choices": ["Paris", "Berlin", "London", "Madrid"],
            "correct_answer": "Paris",
            "points": 1
        },
            {
            "question": "How many hours are in a day?",
            "choices": ["12", "20", "24", "48"],
            "correct_answer": "24",
            "points": 1
        },
            {
            "question": "What is the largest ocean on Earth?",
            "choices": ["Arctic", "Atlantic", "Indian", "Pacific"],
            "correct_answer": "Pacific",
            "points": 1
        }],
        "medium": [{
            "question": "What is H2O commonly known as?",
            "choices": ["Alcohol", "Hydrogen peroxide", "Salt", "Water"], 
            "correct_answer": "Water",
            "points": 2
        }, 
            {
            "question": "What is the square root of 144?",
            "choices": ["10", "11", "12", "14"],
            "correct_answer": "12",
            "points": 2
        },
            {
            "question": "How many bones are in the adult human body?",
            "choices": ["206", "196", "186", "216"],
            "correct_answer": "206",
            "points": 2
        },
            {
            "question": "What is the chemical symbol for gold?",
            "choices": ["Ag", "Au", "Fe", "Gd"],
            "correct_answer": "Au",
            "points": 2
        },
            {
            "question": "Which planet is closest to the Sun?",
            "choices": ["Earth", "Mercury", "Mars", "Venus"],
            "correct_answer": "Mercury",
            "points": 2
        }],
        "hard": [{
            "question": "What is the SI unit of force?",
            "choices": ["Joule", "Newton", "Pascal", "Watt"], 
            "correct_answer": "Newton",
            "points": 3
        }, 
            {
            "question": "What is the speed of light in a vacuum in km/s?",
            "choices": ["200,000", "310,000", "250,000", "299,792"],
            "correct_answer": "299,792",
            "points": 3
        },
            {
            "question": "What is the only number that is twice the sum of its digits?",
            "choices": ["10", "12", "18", "20"],
            "correct_answer": "18",
            "points": 3
        },
            {
            "question": "What is the most abundant gas in Earth's atmosphere?",
            "choices": ["Nitrogen", "Carbon Dioxide", "Oxygen", "Water Vapor"],
            "correct_answer": "Nitrogen",
            "points": 3
        },
            {
            "question": "How many prime numbers are there between 1 and 20?",
            "choices": ["6", "7", "8", "9"],
            "correct_answer": "8",
            "points": 3
        }],
    },
    "Geography": {
        "easy": [{
            "question": "On which continent is Egypt primarily located?",
            "choices": ["Africa", "Asia", "Europe", "South America"], 
            "correct_answer": "Africa",
            "points": 1
        }, 
            {
            "question": "What is the largest country in the world by area?",
            "choices": ["Canada", "China", "Russia", "United States"],
            "correct_answer": "Russia",
            "points": 1
        },
            {
            "question": "Which country has the largest population in the world?",
            "choices": ["Brazil", "India", "China", "United States"],
            "correct_answer": "India",
            "points": 1
        },
            {
            "question": "What is the smallest country in the world?",
            "choices": ["Liechtenstein", "Monaco", "San Marino", "Vatican City"],
            "correct_answer": "Vatican City",
            "points": 1
        },
            {
            "question": "Which continent is the largest by area?",
            "choices": ["Africa", "Antarctica", "Asia", "North America"],
            "correct_answer": "Asia",
            "points": 1
        }],
        "medium": [{
            "question": "What is the capital city of Canada?",
            "choices": ["Montreal", "Ottawa", "Toronto", "Vancouver"], 
            "correct_answer": "Ottawa",
            "points": 2
        }, 
            {
            "question": "What is the capital of Australia?",
            "choices": ["Brisbane", "Melbourne", "Sydney", "Canberra"],
            "correct_answer": "Canberra",
            "points": 2
        },
            {
            "question": "Through how many countries does the Amazon River flow?",
            "choices": ["5", "7", "9", "11"],
            "correct_answer": "9",
            "points": 2
        },
            {
            "question": "What is the tallest mountain in the world?",
            "choices": ["K2", "Kangchenjunga", "Lhotse", "Mount Everest"],
            "correct_answer": "Mount Everest",
            "points": 2
        },
            {
            "question": "Which African country has the most pyramids?",
            "choices": ["Sudan", "Egypt", "Ethiopia", "Libya"],
            "correct_answer": "Sudan",
            "points": 2
        }],
        "hard": [{
            "question": "Which mountain range forms a traditional boundary between Europe and Asia?",
            "choices": ["Alps", "Carpathians", "Pyrenees", "Ural Mountains"], 
            "correct_answer": "Ural Mountains",
            "points": 3
        }, 
            {
            "question": "What is the deepest lake in the world?",
            "choices": ["Caspian Sea", "Lake Baikal", "Lake Superior", "Lake Tanganyika"],
            "correct_answer": "Lake Baikal",
            "points": 3
        },
            {
            "question": "Which country has the most natural lakes?",
            "choices": ["Canada", "Brazil", "Finland", "Russia"],
            "correct_answer": "Canada",
            "points": 3
        },
            {
            "question": "What is the name of the world's largest desert?",
            "choices": ["Arabian Desert", "Gobi Desert", "Antarctic Desert", "Sahara Desert"],
            "correct_answer": "Antarctic Desert",
            "points": 3
        },
            {
            "question": "Which is the only sea with no coastline?",
            "choices": ["Caspian Sea", "Red Sea", "Sargasso Sea", "Yellow Sea"],
            "correct_answer": "Sargasso Sea",
            "points": 3
        }],
    }, 
    "Health & Medicine": {
        "easy": [{
            "question": "Which vitamin is primarily produced in skin after sunlight exposure?",
            "choices": ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], 
            "correct_answer": "Vitamin D",
            "points": 1
        }, 
            {
            "question": "How many chambers does the human heart have?",
            "choices": ["2", "3", "4", "5"],
            "correct_answer": "4",
            "points": 1
        },
            {
            "question": "What is the normal resting heart rate range for adults in beats per minute?",
            "choices": ["40-60", "60-100", "80-120", "100-140"],
            "correct_answer": "60-100",
            "points": 1
        },
            {
            "question": "Which organ produces insulin?",
            "choices": ["Pancreas", "Kidney", "Liver", "Spleen"],
            "correct_answer": "Pancreas",
            "points": 1
        },
            {
            "question": "What does 'BMI' stand for?",
            "choices": ["Basic Metabolic Index", "Blood Mass Indicator", "Body Mass Index", "Bone Mineral Index"],
            "correct_answer": "Body Mass Index",
            "points": 1
        }],
        "medium": [{
            "question": "Which organ filters blood and produces urine?",
            "choices": ["Kidneys", "Liver", "Lungs", "Pancreas"], 
            "correct_answer": "Kidneys",
            "points": 2
        }, 
            {
            "question": "What is the most common blood type?",
            "choices": ["A positive", "AB positive", "B positive", "O positive"],
            "correct_answer": "O positive",
            "points": 2
        },
            {
            "question": "Which vitamin is essential for blood clotting?",
            "choices": ["Vitamin A", "Vitamin K", "Vitamin C", "Vitamin E"],
            "correct_answer": "Vitamin K",
            "points": 2
        },
            {
            "question": "What is the medical term for high blood pressure?",
            "choices": ["Hypertension", "Hypotension", "Tachycardia", "Thrombosis"],
            "correct_answer": "Hypertension",
            "points": 2
        },
            {
            "question": "How many teeth does a typical adult human have?",
            "choices": ["28", "30", "32", "34"],
            "correct_answer": "32",
            "points": 2
        }],
        "hard": [{
            "question": "What is the commonly cited average normal human body temperature in degrees Celsius?",
            "choices": ["34°C", "35°C", "37°C", "39°C"], 
            "correct_answer": "37°C",
            "points": 3
        }, 
            {
            "question": "What is the largest organ in the human body?",
            "choices": ["Brain", "Intestines", "Liver", "Skin"],
            "correct_answer": "Skin",
            "points": 3
        },
            {
            "question": "Which part of the brain controls balance and coordination?",
            "choices": ["Cerebellum", "Cerebrum", "Hippocampus", "Medulla"],
            "correct_answer": "Cerebellum",
            "points": 3
        },
            {
            "question": "What is the name of the protein that carries oxygen in red blood cells?",
            "choices": ["Albumin", "Fibrinogen", "Hemoglobin", "Myoglobin"],
            "correct_answer": "Hemoglobin",
            "points": 3
        },
            {
            "question": "What is the medical term for the surgical removal of the appendix?",
            "choices": ["Appendectomy", "Appendicitis", "Laparoscopy", "Laparotomy"],
            "correct_answer": "Appendectomy",
            "points": 3
        }],
    }, 
    "History": {
        "easy": [{
            "question": "In what year did World War II end?",
            "choices": ["1918", "1939", "1945", "1963"], 
            "correct_answer": "1945",
            "points": 1
        }, 
            {
            "question": "Who was the first President of the United States?",
            "choices": ["George Washington", "Abraham Lincoln", "Benjamin Franklin", "Thomas Jefferson"],
            "correct_answer": "George Washington",
            "points": 1
        },
            {
            "question": "In what year did the Titanic sink?",
            "choices": ["1905", "1908", "1912", "1918"],
            "correct_answer": "1912",
            "points": 1
        },
            {
            "question": "Which ancient wonder was located in Alexandria, Egypt?",
            "choices": ["Colossus of Rhodes", "Great Pyramid", "Statue of Zeus", "Lighthouse of Alexandria"],
            "correct_answer": "Lighthouse of Alexandria",
            "points": 1
        },
            {
            "question": "Who invented the telephone?",
            "choices": ["Alexander Graham Bell", "Nikola Tesla", "Samuel Morse", "Thomas Edison"],
            "correct_answer": "Alexander Graham Bell",
            "points": 1
        }],
        "medium": [{
            "question": "Which empire was founded and led by Genghis Khan?",
            "choices": ["Byzantine Empire", "Mongol Empire", "Ottoman Empire", "Roman Empire"], 
            "correct_answer": "Mongol Empire",
            "points": 2
        }, 
            {
            "question": "In which year did the Berlin Wall fall?",
            "choices": ["1985", "1987", "1989", "1991"],
            "correct_answer": "1989",
            "points": 2
        },
            {
            "question": "Who was the first woman to win a Nobel Prize?",
            "choices": ["Florence Nightingale", "Mother Teresa", "Rosalind Franklin", "Marie Curie"],
            "correct_answer": "Marie Curie",
            "points": 2
        },
            {
            "question": "Which civilization built Machu Picchu?",
            "choices": ["Inca", "Aztec", "Maya", "Olmec"],
            "correct_answer": "Inca",
            "points": 2
        },
            {
            "question": "What was the name of the first artificial satellite launched into space?",
            "choices": ["Apollo 1", "Explorer 1", "Sputnik 1", "Vostok 1"],
            "correct_answer": "Sputnik 1",
            "points": 2
        }],
        "hard": [{
            "question": "Which treaty formally ended World War I?",
            "choices": ["Treaty of Paris", "Treaty of Tordesillas", "Treaty of Utrecht", "Treaty of Versailles"], 
            "correct_answer": "Treaty of Versailles",
            "points": 3
        }, 
            {
            "question": "Which battle ended Napoleon's rule in 1815?",
            "choices": ["Battle of Austerlitz", "Battle of Waterloo", "Battle of Borodino", "Battle of Trafalgar"],
            "correct_answer": "Battle of Waterloo",
            "points": 3
        },
            {
            "question": "What was the name of the first European to reach India by sea?",
            "choices": ["Christopher Columbus", "Ferdinand Magellan", "Vasco da Gama", "Amerigo Vespucci"],
            "correct_answer": "Vasco da Gama",
            "points": 3
        },
            {
            "question": "Which ancient Egyptian queen was known for her relationships with Julius Caesar and Mark Antony?",
            "choices": ["Cleopatra", "Hatshepsut", "Nefertiti", "Nefertari"],
            "correct_answer": "Cleopatra",
            "points": 3
        },
            {
            "question": "What year was the Magna Carta signed?",
            "choices": ["1066", "1215", "1348", "1492"],
            "correct_answer": "1215",
            "points": 3
        }],
    },
    "Literature": {
        "easy": [{
            "question": "Who wrote '1984'?",
            "choices": ["Aldous Huxley", "C.S. Lewis", "George Orwell", "J.R.R. Tolkien"], 
            "correct_answer": "George Orwell",
            "points": 1
        }, 
            {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["Charles Dickens", "Jane Austen", "John Keats", "William Shakespeare"],
            "correct_answer": "William Shakespeare",
            "points": 1
        },
            {
            "question": "What is the name of the wizard school in Harry Potter?",
            "choices": ["Durmstrang", "Hogwarts", "Ilvermorny", "Beauxbatons"],
            "correct_answer": "Hogwarts",
            "points": 1
        },
            {
            "question": "Who wrote 'The Adventures of Tom Sawyer'?",
            "choices": ["Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "Walt Whitman"],
            "correct_answer": "Mark Twain",
            "points": 1
        },
            {
            "question": "What is the first book of the Bible?",
            "choices": ["Exodus", "Genesis", "Leviticus", "Numbers"],
            "correct_answer": "Genesis",
            "points": 1
        }],
        "medium": [{
            "question": "Which novel begins with 'Call me Ishmael'?",
            "choices": ["Heart of Darkness", "Moby-Dick", "The Old Man and the Sea", "Treasure Island"], 
            "correct_answer": "Moby-Dick",
            "points": 2
        }, 
            {
            "question": "In which Dickens novel does the character Ebenezer Scrooge appear?",
            "choices": ["A Tale of Two Cities", "A Christmas Carol", "David Copperfield", "Oliver Twist"],
            "correct_answer": "A Christmas Carol",
            "points": 2
        },
            {
            "question": "Who wrote 'Pride and Prejudice'?",
            "choices": ["Charlotte Bronte", "Emily Bronte", "Jane Austen", "Mary Shelley"],
            "correct_answer": "Jane Austen",
            "points": 2
        },
            {
            "question": "Which Shakespeare play features the character Iago?",
            "choices": ["Hamlet", "King Lear", "Macbeth", "Othello"],
            "correct_answer": "Othello",
            "points": 2
        },
            {
            "question": "Who wrote 'The Great Gatsby'?",
            "choices": ["Ernest Hemingway", "John Steinbeck", "F. Scott Fitzgerald", "William Faulkner"],
            "correct_answer": "F. Scott Fitzgerald",
            "points": 2
        }],
        "hard": [{
            "question": "Who wrote 'One Hundred Years of Solitude'?",
            "choices": ["Gabriel García Márquez", "Isabel Allende", "Jorge Luis Borges", "Mario Vargas Llosa"], 
            "correct_answer": "Gabriel García Márquez",
            "points": 3
        }, 
            {
            "question": "Which author wrote 'Ulysses'?",
            "choices": ["D.H. Lawrence", "Samuel Beckett", "Virginia Woolf", "James Joyce"],
            "correct_answer": "James Joyce",
            "points": 3
        },
            {
            "question": "Who wrote 'Crime and Punishment'?",
            "choices": ["Anton Chekhov", "Leo Tolstoy", "Fyodor Dostoevsky", "Nikolai Gogol"],
            "correct_answer": "Fyodor Dostoevsky",
            "points": 3
        },
            {
            "question": "What is the name of the fictional detective created by Arthur Conan Doyle?",
            "choices": ["Hercule Poirot", "Miss Marple", "Philip Marlowe", "Sherlock Holmes"],
            "correct_answer": "Sherlock Holmes",
            "points": 3
        },
            {
            "question": "Which poet wrote 'The Waste Land'?",
            "choices": ["Ezra Pound", "T.S. Eliot", "W.B. Yeats", "Wallace Stevens"],
            "correct_answer": "T.S. Eliot",
            "points": 3
        }],
    }, 
    "Movies": {
        "easy": [{
            "question": "Who directed 'Jurassic Park'?",
            "choices": ["George Lucas", "James Cameron", "Ridley Scott", "Steven Spielberg"], 
            "correct_answer": "Steven Spielberg",
            "points": 1
        }, 
            {
            "question": "Which animated film features a character named Simba?",
            "choices": ["Bambi", "The Lion King", "Dumbo", "The Jungle Book"],
            "correct_answer": "The Lion King",
            "points": 1
        },
            {
            "question": "What is the name of the toy cowboy in Toy Story?",
            "choices": ["Buzz", "Rex", "Woody", "Zurg"],
            "correct_answer": "Woody",
            "points": 1
        },
            {
            "question": "Which film features the quote 'You can't handle the truth'?",
            "choices": ["A Few Good Men", "Good Will Hunting", "The Shawshank Redemption", "Top Gun"],
            "correct_answer": "A Few Good Men",
            "points": 1
        },
            {
            "question": "What 1994 film stars Tom Hanks as a man with a low IQ who witnesses historic events?",
            "choices": ["Forrest Gump", "Cast Away", "Philadelphia", "Saving Private Ryan"],
            "correct_answer": "Forrest Gump",
            "points": 1
        }],
        "medium": [{
            "question": "Which film franchise features the quote 'May the Force be with you'?",
            "choices": ["Avatar", "Star Trek", "Star Wars", "The Matrix"], 
            "correct_answer": "Star Wars",
            "points": 2
        }, 
            {
            "question": "Who directed the film 'Schindler's List'?",
            "choices": ["Francis Ford Coppola", "Martin Scorsese", "Ridley Scott", "Steven Spielberg"],
            "correct_answer": "Steven Spielberg",
            "points": 2
        },
            {
            "question": "Which film won the first ever Academy Award for Best Picture?",
            "choices": ["Wings", "All Quiet on the Western Front", "Broadway Melody", "The Jazz Singer"],
            "correct_answer": "Wings",
            "points": 2
        },
            {
            "question": "In 'The Godfather', who plays Don Vito Corleone?",
            "choices": ["Al Pacino", "James Caan", "Marlon Brando", "Robert De Niro"],
            "correct_answer": "Marlon Brando",
            "points": 2
        },
            {
            "question": "Which film series features the character Indiana Jones?",
            "choices": ["James Bond", "Raiders of the Lost Ark", "Mission Impossible", "The Mummy"],
            "correct_answer": "Raiders of the Lost Ark",
            "points": 2
        }],
        "hard": [{
            "question": "Which actor portrayed the Joker in 'The Dark Knight' (2008)?",
            "choices": ["Heath Ledger", "Jack Nicholson", "Jared Leto", "Joaquin Phoenix"], 
            "correct_answer": "Heath Ledger",
            "points": 3
        }, 
            {
            "question": "Which director is known for films like '2001: A Space Odyssey' and 'The Shining'?",
            "choices": ["Alfred Hitchcock", "Stanley Kubrick", "Martin Scorsese", "Ridley Scott"],
            "correct_answer": "Stanley Kubrick",
            "points": 3
        },
            {
            "question": "What was the first feature-length animated film ever released?",
            "choices": ["Bambi", "Cinderella", "Snow White and the Seven Dwarfs", "Fantasia"],
            "correct_answer": "Snow White and the Seven Dwarfs",
            "points": 3
        },
            {
            "question": "Which film holds the record for most Academy Award wins with 11 Oscars?",
            "choices": ["Ben-Hur", "The Lord of the Rings: The Return of the King", "Titanic", "All of the above"],
            "correct_answer": "All of the above",
            "points": 3
        },
            {
            "question": "Who composed the iconic score for 'Star Wars'?",
            "choices": ["Bernard Herrmann", "Hans Zimmer", "John Williams", "Ennio Morricone"],
            "correct_answer": "John Williams",
            "points": 3
        }],
    },
    "Music": {
        "easy": [{
            "question": "Who is commonly called the 'King of Pop'?",
            "choices": ["Elvis Presley", "Madonna", "Michael Jackson", "Prince"], 
            "correct_answer": "Michael Jackson",
            "points": 1
        }, 
            {
            "question": "How many strings does a standard guitar have?",
            "choices": ["6", "4", "5", "7"],
            "correct_answer": "6",
            "points": 1
        },
            {
            "question": "Which band performed 'Bohemian Rhapsody'?",
            "choices": ["Led Zeppelin", "Queen", "The Beatles", "The Rolling Stones"],
            "correct_answer": "Queen",
            "points": 1
        },
            {
            "question": "What instrument does a pianist play?",
            "choices": ["Guitar", "Trumpet", "Violin", "Piano"],
            "correct_answer": "Piano",
            "points": 1
        },
            {
            "question": "Which pop star is known as 'The Material Girl'?",
            "choices": ["Beyoncé", "Britney Spears", "Madonna", "Whitney Houston"],
            "correct_answer": "Madonna",
            "points": 1
        }],
        "medium": [{
            "question": "What is the musical term for gradually getting louder?",
            "choices": ["Crescendo", "Diminuendo", "Legato", "Staccato"], 
            "correct_answer": "Crescendo",
            "points": 2
        }, 
            {
            "question": "How many symphonies did Beethoven compose?",
            "choices": ["7", "8", "9", "10"],
            "correct_answer": "9",
            "points": 2
        },
            {
            "question": "Which band released the album 'Abbey Road'?",
            "choices": ["Led Zeppelin", "The Beatles", "Pink Floyd", "The Rolling Stones"],
            "correct_answer": "The Beatles",
            "points": 2
        },
            {
            "question": "What nationality was composer Frédéric Chopin?",
            "choices": ["Austrian", "Polish", "French", "German"],
            "correct_answer": "Polish",
            "points": 2
        },
            {
            "question": "Which singer is known as the 'Queen of Soul'?",
            "choices": ["Diana Ross", "Ella Fitzgerald", "Nina Simone", "Aretha Franklin"],
            "correct_answer": "Aretha Franklin",
            "points": 2
        }],
        "hard": [{
            "question": "Which composer wrote the 'Moonlight Sonata'?",
            "choices": ["Franz Schubert", "Johannes Brahms", "Ludwig van Beethoven", "Wolfgang Amadeus Mozart"], 
            "correct_answer": "Ludwig van Beethoven",
            "points": 3
        }, 
            {
            "question": "What is the name of the scale that uses all twelve pitches of the chromatic scale?",
            "choices": ["Diatonic scale", "Major scale", "Minor scale", "Twelve-tone scale"],
            "correct_answer": "Twelve-tone scale",
            "points": 3
        },
            {
            "question": "Which composer wrote 'The Four Seasons'?",
            "choices": ["Antonio Vivaldi", "George Frideric Handel", "Johann Sebastian Bach", "Wolfgang Amadeus Mozart"],
            "correct_answer": "Antonio Vivaldi",
            "points": 3
        },
            {
            "question": "What does 'fortissimo' mean in musical notation?",
            "choices": ["Very fast", "Very loud", "Very slow", "Very soft"],
            "correct_answer": "Very loud",
            "points": 3
        },
            {
            "question": "Which jazz musician was known as 'Satchmo'?",
            "choices": ["Charlie Parker", "Duke Ellington", "Louis Armstrong", "Miles Davis"],
            "correct_answer": "Louis Armstrong",
            "points": 3
        }],
    },
    "Mythology": {
        "easy": [{
            "question": "In Greek mythology, who is king of the gods?",
            "choices": ["Apollo", "Hades", "Poseidon", "Zeus"], 
            "correct_answer": "Zeus",
            "points": 1
        }, 
            {
            "question": "In Greek mythology, who is the god of the sea?",
            "choices": ["Apollo", "Ares", "Hades", "Poseidon"],
            "correct_answer": "Poseidon",
            "points": 1
        },
            {
            "question": "What is the name of the winged horse in Greek mythology?",
            "choices": ["Centaur", "Chimera", "Pegasus", "Unicorn"],
            "correct_answer": "Pegasus",
            "points": 1
        },
            {
            "question": "In Norse mythology, who is the god of thunder?",
            "choices": ["Thor", "Loki", "Odin", "Tyr"],
            "correct_answer": "Thor",
            "points": 1
        },
            {
            "question": "In Egyptian mythology, who is the god of the sun?",
            "choices": ["Anubis", "Ra", "Osiris", "Set"],
            "correct_answer": "Ra",
            "points": 1
        }],
        "medium": [{
            "question": "In Norse mythology, what is the name of the world tree?",
            "choices": ["Asgard", "Midgard", "Valhalla", "Yggdrasil"], 
            "correct_answer": "Yggdrasil",
            "points": 2
        }, 
            {
            "question": "In Greek mythology, who flew too close to the sun?",
            "choices": ["Daedalus", "Icarus", "Narcissus", "Perseus"],
            "correct_answer": "Icarus",
            "points": 2
        },
            {
            "question": "What is the name of the ship Jason sailed in search of the Golden Fleece?",
            "choices": ["Odyssey", "Penelope", "Argo", "Trireme"],
            "correct_answer": "Argo",
            "points": 2
        },
            {
            "question": "In Roman mythology, what is the equivalent of the Greek god Zeus?",
            "choices": ["Jupiter", "Mars", "Mercury", "Neptune"],
            "correct_answer": "Jupiter",
            "points": 2
        },
            {
            "question": "Who was the Greek goddess of wisdom?",
            "choices": ["Aphrodite", "Artemis", "Athena", "Hera"],
            "correct_answer": "Athena",
            "points": 2
        }],
        "hard": [{
            "question": "Which Greek mythological creature has a lion's head, goat's body, and serpent's tail?",
            "choices": ["Cerberus", "Chimera", "Hydra", "Sphinx"], 
            "correct_answer": "Chimera",
            "points": 3
        }, 
            {
            "question": "In Greek mythology, what was the name of the river of forgetfulness in the underworld?",
            "choices": ["Acheron", "Phlegethon", "Styx", "Lethe"],
            "correct_answer": "Lethe",
            "points": 3
        },
            {
            "question": "Who was the Norse god of mischief?",
            "choices": ["Baldur", "Freyr", "Loki", "Tyr"],
            "correct_answer": "Loki",
            "points": 3
        },
            {
            "question": "In Greek mythology, what is the name of the three-headed dog that guards the underworld?",
            "choices": ["Cerberus", "Chimera", "Hydra", "Orthrus"],
            "correct_answer": "Cerberus",
            "points": 3
        },
            {
            "question": "In Egyptian mythology, what did Anubis weigh against a feather to judge the dead?",
            "choices": ["The brain", "The liver", "The heart", "The soul"],
            "correct_answer": "The heart",
            "points": 3
        }],
    },
    "Pop Culture": {
        "easy": [{
            "question": "Which streaming platform produced 'Stranger Things'?",
            "choices": ["Amazon Prime Video", "Disney+", "Hulu", "Netflix"], 
            "correct_answer": "Netflix",
            "points": 1
        },
            {
            "question": "Which social media platform is known for short video content and the 'For You Page'?",
            "choices": ["Instagram", "Snapchat", "TikTok", "YouTube"],
            "correct_answer": "TikTok",
            "points": 1
        },
            {
            "question": "What is the name of the fictional kingdom in the movie 'Frozen'?",
            "choices": ["Arendelle", "Eldorado", "Narnia", "Neverland"],
            "correct_answer": "Arendelle",
            "points": 1
        },
            {
            "question": "Which superhero is known as the 'Man of Steel'?",
            "choices": ["Batman", "Iron Man", "Spider-Man", "Superman"],
            "correct_answer": "Superman",
            "points": 1
        },
            {
            "question": "What color is the Teletubby named Tinky Winky?",
            "choices": ["Green", "Purple", "Red", "Yellow"],
            "correct_answer": "Purple",
            "points": 1
        }],
        "medium": [{
            "question": "Which social media platform originally limited posts to 280 characters?",
            "choices": ["Facebook", "Instagram", "TikTok", "Twitter"], 
            "correct_answer": "Twitter",
            "points": 2
        }, 
            {
            "question": "Which boy band sang 'I Want It That Way'?",
            "choices": ["Backstreet Boys", "NSYNC", "New Kids on the Block", "One Direction"],
            "correct_answer": "Backstreet Boys",
            "points": 2
        },
            {
            "question": "What is the name of the coffee shop in the TV show 'Friends'?",
            "choices": ["Coffee Bean", "Java Hut", "Central Perk", "The Percolator"],
            "correct_answer": "Central Perk",
            "points": 2
        },
            {
            "question": "Which artist released the album 'Thriller' in 1982?",
            "choices": ["David Bowie", "Madonna", "Michael Jackson", "Prince"],
            "correct_answer": "Michael Jackson",
            "points": 2
        },
            {
            "question": "What is the highest-grossing film of all time worldwide?",
            "choices": ["Avengers: Endgame", "Avatar", "Star Wars: The Force Awakens", "Titanic"],
            "correct_answer": "Avatar",
            "points": 2
        }],
        "hard": [{
            "question": "Which artist released the album 'Lemonade' in 2016?",
            "choices": ["Adele", "Beyoncé", "Rihanna", "Taylor Swift"], 
            "correct_answer": "Beyoncé",
            "points": 3
        }, 
            {
            "question": "Which video game franchise features a character named Master Chief?",
            "choices": ["Call of Duty", "Destiny", "Gears of War", "Halo"],
            "correct_answer": "Halo",
            "points": 3
        },
            {
            "question": "What year did the first iPhone launch?",
            "choices": ["2005", "2006", "2007", "2008"],
            "correct_answer": "2007",
            "points": 3
        },
            {
            "question": "Which fashion designer is credited with popularizing the little black dress?",
            "choices": ["Coco Chanel", "Christian Dior", "Gianni Versace", "Yves Saint Laurent"],
            "correct_answer": "Coco Chanel",
            "points": 3
        },
            {
            "question": "What was the best-selling video game console of all time?",
            "choices": ["Nintendo DS", "PlayStation 2", "PlayStation 4", "Wii"],
            "correct_answer": "PlayStation 2",
            "points": 3
        }],
    },
    "Science": {
        "easy": [{
            "question": "What gas do plants primarily absorb for photosynthesis?",
            "choices": ["Carbon dioxide", "Hydrogen", "Nitrogen", "Oxygen"], 
            "correct_answer": "Carbon dioxide",
            "points": 1
        }, 
            {
            "question": "What force keeps planets in orbit around the sun?",
            "choices": ["Electromagnetism", "Friction", "Gravity", "Nuclear force"],
            "correct_answer": "Gravity",
            "points": 1
        },
            {
            "question": "What is the center of an atom called?",
            "choices": ["Electron", "Neutron", "Proton", "Nucleus"],
            "correct_answer": "Nucleus",
            "points": 1
        },
            {
            "question": "How many colors are in a rainbow?",
            "choices": ["5", "7", "6", "8"],
            "correct_answer": "7",
            "points": 1
        },
            {
            "question": "What is the process by which water turns into vapor?",
            "choices": ["Condensation", "Evaporation", "Precipitation", "Transpiration"],
            "correct_answer": "Evaporation",
            "points": 1
        }],
        "medium": [{
            "question": "What is the chemical formula for common table salt?",
            "choices": ["CaCl2", "KCl", "Na2CO3", "NaCl"], 
            "correct_answer": "NaCl",
            "points": 2
        }, 
            {
            "question": "What is the powerhouse of the cell?",
            "choices": ["Cell membrane", "Mitochondria", "Nucleus", "Ribosome"],
            "correct_answer": "Mitochondria",
            "points": 2
        },
            {
            "question": "What is the atomic number of carbon?",
            "choices": ["4", "6", "8", "12"],
            "correct_answer": "6",
            "points": 2
        },
            {
            "question": "Which scientist developed the theory of general relativity?",
            "choices": ["Albert Einstein", "Isaac Newton", "Max Planck", "Niels Bohr"],
            "correct_answer": "Albert Einstein",
            "points": 2
        },
            {
            "question": "What is the name of the process by which plants make food?",
            "choices": ["Fermentation", "Osmosis", "Photosynthesis", "Respiration"],
            "correct_answer": "Photosynthesis",
            "points": 2
        }],
        "hard": [{
            "question": "Which elementary particle mediates the electromagnetic force?",
            "choices": ["Gluon", "Graviton", "Photon", "W boson"], 
            "correct_answer": "Photon",
            "points": 3
        }, 
            {
            "question": "What is the half-life of Carbon-14?",
            "choices": ["1,000 years", "5,730 years", "10,000 years", "50,000 years"],
            "correct_answer": "5,730 years",
            "points": 3
        },
            {
            "question": "What is the name of the process by which one element transforms into another through radioactive decay?",
            "choices": ["Fission", "Fusion", "Transmutation", "Ionization"],
            "correct_answer": "Transmutation",
            "points": 3
        },
            {
            "question": "Which subatomic particle has no electric charge?",
            "choices": ["Electron", "Neutron", "Positron", "Proton"],
            "correct_answer": "Neutron",
            "points": 3
        },
            {
            "question": "What is the name of the boundary between the Earth's crust and mantle?",
            "choices": ["Conrad discontinuity", "Gutenberg discontinuity", "Lehmann discontinuity", "Mohorovičić discontinuity"],
            "correct_answer": "Mohorovičić discontinuity",
            "points": 3
        }],
    }, 
    "Sports": {
        "easy": [{
            "question": "How many players per side are on the field in a standard soccer game?",
            "choices": ["9", "10", "11", "12"], 
            "correct_answer": "11",
            "points": 1
        }, 
            {
            "question": "In basketball, how many points is a free throw worth?",
            "choices": ["1", "2", "3", "4"],
            "correct_answer": "1",
            "points": 1
        },
            {
            "question": "How many players are on a baseball team on the field at one time?",
            "choices": ["7", "8", "9", "10"],
            "correct_answer": "9",
            "points": 1
        },
            {
            "question": "What sport is played at Wimbledon?",
            "choices": ["Badminton", "Cricket", "Squash", "Tennis"],
            "correct_answer": "Tennis",
            "points": 1
        },
            {
            "question": "In which sport would you perform a slam dunk?",
            "choices": ["Baseball", "Basketball", "Football", "Volleyball"],
            "correct_answer": "Basketball",
            "points": 1
        }],
        "medium": [{
            "question": "Which country has won the most FIFA World Cup tournaments?",
            "choices": ["Argentina", "Brazil", "Germany", "Italy"], 
            "correct_answer": "Brazil",
            "points": 2
        }, 
            {
            "question": "How many Grand Slam tennis tournaments are there per year?",
            "choices": ["2", "3", "4", "5"],
            "correct_answer": "4",
            "points": 2
        },
            {
            "question": "How long is a standard marathon in miles?",
            "choices": ["26.2", "24.2", "25.2", "27.2"],
            "correct_answer": "26.2",
            "points": 2
        },
            {
            "question": "In American football, how many points is a touchdown worth?",
            "choices": ["3", "4", "6", "7"],
            "correct_answer": "6",
            "points": 2
        },
            {
            "question": "Which country invented the sport of basketball?",
            "choices": ["England", "Jamaica", "United States", "Canada"],
            "correct_answer": "Canada",
            "points": 2
        }],
        "hard": [{
            "question": "On which surface is the French Open tennis tournament played?",
            "choices": ["Carpet", "Clay", "Grass", "Hard Court"], 
            "correct_answer": "Clay",
            "points": 3
        }, 
            {
            "question": "How many dimples does a regulation golf ball have?",
            "choices": ["256", "336", "366", "500"],
            "correct_answer": "336",
            "points": 3
        },
            {
            "question": "In which year were women first allowed to compete in the Olympic Games?",
            "choices": ["1896", "1920", "1928", "1900"],
            "correct_answer": "1900",
            "points": 3
        },
            {
            "question": "What is the diameter of a basketball hoop in inches?",
            "choices": ["16", "20", "18", "22"],
            "correct_answer": "18",
            "points": 3
        },
            {
            "question": "Which country has won the most Olympic gold medals in history?",
            "choices": ["China", "Great Britain", "Russia", "United States"],
            "correct_answer": "United States",
            "points": 3
        }],
    },
    "Technology": {
        "easy": [{
            "question": "What does 'HTTP' stand for?",
            "choices": ["High Transfer Text Protocol", "Hyperlink Transfer Protocol", "HyperText Transfer Protocol", "HyperText Transmission Protocol"], 
            "correct_answer": "HyperText Transfer Protocol",
            "points": 1
        }, 
            {
            "question": "What does 'www' stand for in a website address?",
            "choices": ["Wide World Web", "World Wide Web", "World Web Wide", "Web World Wide"],
            "correct_answer": "World Wide Web",
            "points": 1
        },
            {
            "question": "What company makes the iPhone?",
            "choices": ["Apple", "Google", "Microsoft", "Samsung"],
            "correct_answer": "Apple",
            "points": 1
        },
            {
            "question": "What does 'USB' stand for?",
            "choices": ["Universal System Bus", "Unified Serial Bus", "Universal Serial Bus", "Unified System Bus"],
            "correct_answer": "Universal Serial Bus",
            "points": 1
        },
            {
            "question": "Which company owns the Android operating system?",
            "choices": ["Apple", "Microsoft", "Samsung", "Google"],
            "correct_answer": "Google",
            "points": 1
        }],
        "medium": [{
            "question": "Who proposed the World Wide Web in 1989?",
            "choices": ["Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Vint Cerf"], 
            "correct_answer": "Tim Berners-Lee",
            "points": 2
        }, 
            {
            "question": "What programming language is most commonly used for web development?",
            "choices": ["C++", "Java", "JavaScript", "Python"],
            "correct_answer": "JavaScript",
            "points": 2
        },
            {
            "question": "What does 'AI' stand for in technology?",
            "choices": ["Automated Intelligence", "Artificial Intelligence", "Advanced Interface", "Automated Interface"],
            "correct_answer": "Artificial Intelligence",
            "points": 2
        },
            {
            "question": "Which company developed the Windows operating system?",
            "choices": ["Apple", "IBM", "Intel", "Microsoft"],
            "correct_answer": "Microsoft",
            "points": 2
        },
            {
            "question": "What does 'RAM' stand for in computing?",
            "choices": ["Random Access Memory", "Read Access Memory", "Remote Access Memory", "Rapid Access Memory"],
            "correct_answer": "Random Access Memory",
            "points": 2
        }],
        "hard": [{
            "question": "Moore's Law describes which trend?",
            "choices": ["Internet bandwidth doubling every 18 months", "Memory cost halving every year", "Processor speed doubling every year", "The number of transistors on an integrated circuit doubling approximately every two years"], 
            "correct_answer": "The number of transistors on an integrated circuit doubling approximately every two years",
            "points": 3
        }, 
            {
            "question": "What is the name of the first computer bug, literally found in a computer?",
            "choices": ["A beetle", "A cockroach", "A moth", "A spider"],
            "correct_answer": "A moth",
            "points": 3
        },
            {
            "question": "What does 'SQL' stand for?",
            "choices": ["Sequential Query Language", "Structured Query Language", "Simple Query Language", "Standard Query Language"],
            "correct_answer": "Structured Query Language",
            "points": 3
        },
            {
            "question": "Which programming language was the first to be developed?",
            "choices": ["Assembly", "COBOL", "FORTRAN", "LISP"],
            "correct_answer": "Assembly",
            "points": 3
        },
            {
            "question": "What is the name of the algorithm used by Google to rank web pages?",
            "choices": ["AlphaRank", "LinkRank", "PageRank", "WebRank"],
            "correct_answer": "PageRank",
            "points": 3
        }],
    },
    "TV Shows": {
        "easy": [{
            "question": "Which series stars the character Walter White?",
            "choices": ["Breaking Bad", "Mad Men", "The Sopranos", "The Wire"], 
            "correct_answer": "Breaking Bad",
            "points": 1
        }, 
            {
            "question": "What is the name of the high school in 'Saved by the Bell'?",
            "choices": ["Jefferson High", "Lincoln High", "Bayside High", "Valley High"],
            "correct_answer": "Bayside High",
            "points": 1
        },
            {
            "question": "Which animated show is set in the town of Springfield?",
            "choices": ["Futurama", "The Simpsons", "King of the Hill", "Family Guy"],
            "correct_answer": "The Simpsons",
            "points": 1
        },
            {
            "question": "What animated show features the Griffin family?",
            "choices": ["American Dad", "Bob's Burgers", "Family Guy", "The Simpsons"],
            "correct_answer": "Family Guy",
            "points": 1
        },
            {
            "question": "In 'Friends', what is the name of Ross's pet monkey?",
            "choices": ["Marcel", "Bubble", "Cappuccino", "Pierre"],
            "correct_answer": "Marcel",
            "points": 1
        }],
        "medium": [{
            "question": "Which long-running sci-fi series features a time-traveling character known as the Doctor?",
            "choices": ["Battlestar Galactica", "Doctor Who", "Stargate", "Star Trek"], 
            "correct_answer": "Doctor Who",
            "points": 2
        }, 
            {
            "question": "How many seasons did 'Game of Thrones' run for?",
            "choices": ["6", "7", "8", "9"],
            "correct_answer": "8",
            "points": 2
        },
            {
            "question": "Which TV show is set in the fictional Westeros?",
            "choices": ["Game of Thrones", "The Witcher", "Vikings", "The Last Kingdom"],
            "correct_answer": "Game of Thrones",
            "points": 2
        },
            {
            "question": "What is the name of the prison in 'Orange is the New Black'?",
            "choices": ["Litchfield Penitentiary", "Oswald State", "Riverbend Prison", "Shawshank Prison"],
            "correct_answer": "Litchfield Penitentiary",
            "points": 2
        },
            {
            "question": "Which streaming service produced 'The Crown'?",
            "choices": ["Amazon Prime", "Apple TV+", "Disney+", "Netflix"],
            "correct_answer": "Netflix",
            "points": 2
        }],
        "hard": [{
            "question": "In 'The Office' (US), what is the name of the paper company where characters work?",
            "choices": ["Dunder Mifflin", "Initech", "Prestige Worldwide", "Vandelay Industries"],
            "correct_answer": "Dunder Mifflin",
            "points": 3
        },
            {
            "question": "How many episodes are in the first season of 'The Wire'?",
            "choices": ["10", "11", "13", "12"],
            "correct_answer": "13",
            "points": 3
        },
            {
            "question": "Which TV show holds the record for most Emmy wins?",
            "choices": ["Game of Thrones", "Saturday Night Live", "The West Wing", "Breaking Bad"],
            "correct_answer": "Saturday Night Live",
            "points": 3
        },
            {
            "question": "In 'The Sopranos', what is Tony Soprano's psychiatrist's name?",
            "choices": ["Dr. Cusamano", "Dr. Scully", "Dr. Wegler", "Dr. Melfi"],
            "correct_answer": "Dr. Melfi",
            "points": 3
        },
            {
            "question": "Which show was the first to be entirely released at once on a streaming platform?",
            "choices": ["Arrested Development", "Orange is the New Black", "House of Cards", "Stranger Things"],
            "correct_answer": "House of Cards",
            "points": 3
        }]
    }
}

category_colors = {
    "Animals": "#e67e22",
    "Art": "#c0392b",
    "Astronomy & Space": "#4a235a",
    "Business & Economics": "#7b241c",
    "Famous Quotes": "#1f618d",
    "Food & Drink": "#cb4335",
    "Games": "#512e5f",
    "General Knowledge": "#2471a3",
    "Geography": "#7d6608",
    "Health & Medicine": "#196f3d",
    "History": "#784212",
    "Literature": "#7d3c98",
    "Movies": "#566573",
    "Music": "#a93226",
    "Mythology": "#76448a",
    "Pop Culture": "#8e44ad",
    "Science": "#0e6655",
    "Sports": "#922b21",
    "Technology": "#1a5276",
    "TV Shows": "#ca6f1e",
    "Random": "#2c2c2c",
}