# array and loops
# Make and object/function that should handle with studant structure declared below

studant = {
    "Bolsonaro Livre": {
        "notas": {
            "Matemática": {
                "1 bimestre": 8,
                "2 bimestre": 7.5,
                "3 bimestre": 6.75,
                "4 bimestre": 10,
            },
            "Biologia": {
                "1 bimestre": 5.78,
                "2 bimestre": 8.5,
                "3 bimestre": 9.75,
            }
        },
        "Apelido": "22"
    },
    "Lula Molusco": {
        "notas": {
            "Matemática": {
                "1 bimestre": 8,
                "2 bimestre": 7.5,
                "3 bimestre": 6.75,
                "4 bimestre": 10
            },
            "Biologia": {
                "1 bimestre": 5.78,
                "3 bimestre": 9.75,
                "3 bimestre": 9.75,
            }
        },
        "Apelido": "batman do pt"
    }
}
# 1.
# Create an object that can get average of notes for a given course
# e.g: average_of_grades(Studant.matematica) -> should return average of all grades declared
# note-reminder: If a course has fewer than 4 grades registered,
# always consider 0 for these pending grades and average them by 4


# 2.
# print(Studant) should return "Apelido"/"slug"
# to do it use __str__ method

# 3.
# Studant_1.matematica + Studant_2.matematica
# must return a list with the average of the grades with each
# pair of grades added pairwise, if one list is smaller
# than the other it adds up to 0
# e.g: [1,2,3,4] + [1,2,3,4] = [1+1/2, 2+2/3, 3+3/2, 4+4/2]


# Exercises level Thanos
# 1. on exercise no-3 grades should not be added together if the courses are
# different from each other

# 2. In each exercise, consider the case where the student took the
# recovery test in a given semester. This means that the grade for a
# given semester can be a list of up to 3 grades, where the final grade should be
# considered as the highest among them.
