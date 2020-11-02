def coder(message: str, number_of_tracks: int) -> str:
    if number_of_tracks < 2:
        raise Exception("Number of tracks must be greater than 2")
    track = 0
    direction = 1
    coded_message = ['' for _ in range(number_of_tracks)]
    for sign in message:
        coded_message[track] += sign
        track += direction
        if track == number_of_tracks - 1 or track == 0:
            direction = -direction

    return ''.join([item for sublist in coded_message for item in sublist])


def decoder(message: str, number_of_tracks: int) -> str:
    if number_of_tracks < 2:
        raise Exception("Number of tracks must be greater than 2")
    track = 0
    direction = 1
    tracks = ['' for _ in range(number_of_tracks)]
    for _ in message:
        tracks[track] += "-"
        track += direction
        if track == number_of_tracks - 1 or track == 0:
            direction = -direction

    counter = 0
    index = 0
    decoded_tracks = ['' for _ in range(number_of_tracks)]
    for t in tracks:
        decoded_tracks[index] = message[counter:(counter + len(t))]
        counter += len(t)
        index += 1

    decoded_message = ""
    track = 0
    direction = 1
    for _ in message:
        decoded_message += decoded_tracks[track][0]
        decoded_tracks[track] = decoded_tracks[track][1:]
        track += direction
        if track == number_of_tracks - 1 or track == 0:
            direction = -direction

    return decoded_message


def main():
    print(decoder("WYADIZSBRRETSTHDECEAWKCZSZIMION", 5), coder("WITAMWSZYSTKICHBARDZOSERDECZNIE", 5))


if __name__ == "__main__":
    main()
