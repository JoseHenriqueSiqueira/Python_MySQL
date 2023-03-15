import random
# Listas de palavras para compor os nomes dos livros
adjectives = ["Crazy", "Lonely", "Mysterious", "Forgotten", "Lost", "Magical", "Enchanted", "Dark", "Famous", "Ancient"]
nouns = ["Castle", "Mountain", "Island", "Forest", "Maze", "River", "Cave", "Desert", "Library", "Temple"]
titles = ["Chronicles", "Adventures", "Journeys", "Tales", "Legends", "Mysteries", "Secrets", "Enigmas", "Myths", "Histories"]

# Função para gerar um nome de livro aleatório
def generate_book_title():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    title = random.choice(titles)
    return f"{adjective} {noun} {title}"