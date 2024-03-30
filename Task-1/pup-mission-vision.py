def print_mvc():
    mvc = (
        "PUP MISSION \n Ensuring inclusive and\n equitable quality education\n and promoting lifelong learning\n opportunities through a re-engineered\n polytechnic university by committing\n to: "
        "provide democratized access to educational\n opportunities for the holistic development of\n individuals with global perspective"
        "offer industry-oriented\n curricula that produce\n highly-skilled professionals"
        "with managerial\n and technical capabilities and a strong sense of\n public service for nation building"
        "embed a culture\n of research and innovation"
        "continuously develop faculty\n and employees with the highest level of professionalism"
        "engage\n public and private institutions and other stakeholders for the\n attainment of social development goal"
        "establish a strong presence and\n impact in the international academic community.\n"

        "PUP VISION \n Clearing the paths while laying new foundations to transform the\n Polytechnic University of the Philippines into epistemic community. \n"

        "CORE VALUES\n Integrity and Accountability, Nationalism,\n Spirituality Passion for learning and Innovation, Inclusivity,\n Respect for Human Rights and the Environment, Excellence, Democary."
    )

    lines = mvc.split("\n")
    max_length = max(len(line) for line in lines)
    mcenter = "\n".join(line.center(max_length) for line in lines)

    print(mcenter)


if __name__ == "__main__":
    print_mvc()
