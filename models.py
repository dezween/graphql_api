# models.py

class Character:
    def __init__(self, name, faculty, description, wand, boggart, patronus):
        self.name = name
        self.faculty = faculty
        self.description = description
        self.wand = wand
        self.boggart = boggart
        self.patronus = patronus


# Фиктивные данные о персонажах
characters_data = {
    "harry_potter": Character(
        name="Harry Potter",
        faculty="Gryffindor",
        description="The main protagonist of the series.",
        wand="Holly, 11', with a phoenix feather core",
        boggart="Dementor",
        patronus="Stag",
    ),
    "hermione_granger": Character(
        name="Hermione Granger",
        faculty="Gryffindor",
        description="One of Harry's best friends and top students at Hogwarts.",
        wand="Vine, 10¾', with a dragon heartstring core",
        boggart="Failure",
        patronus="Otter",
    ),
    "ron_weasley": Character(
        name="Ron Weasley",
        faculty="Gryffindor",
        description="Harry's best friend and a member of the Weasley family.",
        wand="Willow, 14', with a unicorn hair core",
        boggart="Spiders",
        patronus="Jack Russell Terrier",
    ),
    "albus_dumbledore": Character(
        name="Albus Dumbledore",
        faculty="Gryffindor",
        description="Headmaster of Hogwarts School of Witchcraft and Wizardry.",
        wand="Elder, 15', with a Thestral tail hair core",
        boggart="The corpse of his sister Ariana",
        patronus="Phoenix",
    ),
    "severus_snape": Character(
        name="Severus Snape",
        faculty="Slytherin",
        description="The Potions Master at Hogwarts and a complex character.",
        wand="Aspen, 10¼', with a unicorn hair core",
        boggart="Neville Longbottom telling him he is his greatest fear",
        patronus="Doe",
    ),
    "luna_lovegood": Character(
        name="Luna Lovegood",
        faculty="Ravenclaw",
        description="A quirky and unique student at Hogwarts with a keen interest in magical creatures.",
        wand="Unknown",
        boggart="Unknown",
        patronus="Hare",
    ),
    "neville_longbottom": Character(
        name="Neville Longbottom",
        faculty="Gryffindor",
        description="A loyal friend of Harry, Ron, and Hermione, who grows into a courageous leader.",
        wand="Cherry, 13', with a unicorn hair core",
        boggart="Professor Snape",
        patronus="Non-corporeal (Determined to be a Great White Stag)",
    ),
    "ginny_weasley": Character(
        name="Ginny Weasley",
        faculty="Gryffindor",
        description="Ron's younger sister, a skilled witch who becomes a member of Dumbledore's Army.",
        wand="Yew, 9', with a core of unknown substance",
        boggart="A corpse of Harry",
        patronus="Horse",
    ),
    "draco_malfoy": Character(
        name="Draco Malfoy",
        faculty="Slytherin",
        description="A rival of Harry and member of the wealthy Malfoy family.",
        wand="Hawthorn, 10', with a unicorn hair core",
        boggart="Voldemort",
        patronus="None",
    ),
    "dobby": Character(
        name="Dobby",
        faculty="None",
        description="A house-elf who served the Malfoy family and later Harry Potter.",
        wand="None",
        boggart="Unknown",
        patronus="None",
    ),
    "fred_weasley": Character(
        name="Fred Weasley",
        faculty="Gryffindor",
        description="One of the mischievous Weasley twins, known for their pranks and jokes.",
        wand="Unknown",
        boggart="Unknown",
        patronus="Non-corporeal",
    ),
    "george_weasley": Character(
        name="George Weasley",
        faculty="Gryffindor",
        description="The other half of the Weasley twins duo, known for their clever inventions.",
        wand="Unknown",
        boggart="Unknown",
        patronus="Non-corporeal",
    ),
    "remus_lupin": Character(
        name="Remus Lupin",
        faculty="Gryffindor",
        description="A werewolf and former Defense Against the Dark Arts teacher at Hogwarts.",
        wand="Cypress, 10¼', with a unicorn hair core",
        boggart="Full moon",
        patronus="Wolf",
    ),
    "sirius_black": Character(
        name="Sirius Black",
        faculty="Gryffindor",
        description="Harry's godfather and an animagus who can turn into a large black dog.",
        wand="Unknown",
        boggart="Dementor",
        patronus="Unknown",
    ),
    "minerva_mcgonagall": Character(
        name="Minerva McGonagall",
        faculty="Gryffindor",
        description="Deputy Headmistress of Hogwarts and Transfiguration professor.",
        wand="Fir, 9¼', with a dragon heartstring core",
        boggart="Voldemort",
        patronus="Cat",
    ),
    "rubeus_hagrid": Character(
        name="Rubeus Hagrid",
        faculty=None,
        description="The gamekeeper and Keeper of Keys and Grounds at Hogwarts, as well as a loyal friend to Harry.",
        wand="Oak, 16', with a core of unknown substance",
        boggart="Aragog",
        patronus="None",
    ),
    "tom_riddle": Character(
        name="Tom Riddle",
        faculty="Slytherin",
        description="The main antagonist of the series, later known as Lord Voldemort.",
        wand="Yew, 13½', with a phoenix feather core",
        boggart="His own corpse",
        patronus="None",
    ),
    "alastor_moody": Character(
        name="Alastor Moody",
        faculty="None",
        description="A famous Auror with a magical eye who teaches Defense Against the Dark Arts at Hogwarts.",
        wand="Unknown",
        boggart="Lord Voldemort",
        patronus="None",
    ),
    "dolores_umbridge": Character(
        name="Dolores Umbridge",
        faculty="None",
        description="A cruel and authoritarian Ministry official who becomes Hogwarts High Inquisitor.",
        wand="Birch, 8', with a dragon heartstring core",
        boggart="Unknown",
        patronus="None",
    ),
    "cedric_diggory": Character(
        name="Cedric Diggory",
        faculty="Hufflepuff",
        description="A popular and talented student from Hufflepuff who competes in the Triwizard Tournament.",
        wand="Ash, 12¼', with a unicorn hair core",
        boggart="Unknown",
        patronus="Non-corporeal",
    ),
    
}
