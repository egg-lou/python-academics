def print_hymn():
    hymn = (
        "\nPUP Hymn\n"
        "Sintang Paaralan\n"
        "Tanglaw ka ng bayan\n"
        "Pandayan ng isip ng kabataan\n"
        "Kami ay dumating nang salat sa yaman\n"
        "Hanap na dunong ay iyong alay\n"
        "Ang layunin mong makatao\n"
        "Dinarangal ang Pilipino\n"
        "Ang iyong aral, diwa, adhikang taglay\n"
        "PUP, aming gabay\n"
        "Paaralang dakila\n"
        "PUP, pinagpala\n"
        "Gagamitin ang karunungan\n"
        "Mula sa iyo, para sa bayan\n"
        "Ang iyong aral, diwa, adhikang taglay\n"
        "PUP, aming gabay\n"
        "Paaralang dakila\n"
        "PUP, pinagpala\n"
    )
    lines = hymn.split('\n')
    max_len = max(len(line) for line in lines)
    hymn = "\n".join(line.center(max_len) for line in lines)

    print(hymn)


if __name__ == "__main__":
    print_hymn()
