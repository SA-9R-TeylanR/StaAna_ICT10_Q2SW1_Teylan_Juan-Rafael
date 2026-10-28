from pyscript import document

# Python list of members
members = [
    "Pikachu Poke", "Charizard Poke", "Mewtwo Poke",
    "Mew Poke", "Blastoise Poke", "Eevee Poke",
    "Bulbasaur Poke", "Squirtle Poke", "Charmander Poke",
    "Gengar Poke", "Lucario Poke", "Snorlax Poke",
    "Jigglypuff Poke", "Greninja Poke", "Rayquaza Poke"
]


def add_member(event):
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    full_name = first + " " + last

    is_member = full_name in members

    messages = [
        "Sorry " + full_name + ", your name is not on the list.",
        "Congratulations " + full_name + "! You are now part of the ICT club."
    ]

    document.getElementById("output").innerText = messages[is_member]