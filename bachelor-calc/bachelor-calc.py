class Contestant():
    def __init__(self, n:str, rose:bool, place:int, fir:bool) -> None:    
        self.name = n
        self.got_a_rose = rose # are they still in true-yes, false-no
        self.placement = place
        self.first_impression_rose = fir

def find_placement(contestant_str):
    if "-next" in contestant_str:
        return 11

    # Check for "-# or -##" anywhere in the string
    for i in range(len(contestant_str) - 1):
        # Check for "-#"
        if contestant_str[i] == '-' and contestant_str[i+1].isdigit():
            # If there's a next digit, append it
            if i+2 < len(contestant_str) and contestant_str[i+2].isdigit():
                return int(contestant_str[i+1:i+3])
            else:
                return int(contestant_str[i+1])

    return 0

def read_contestants(filename):
    with open(filename, 'r') as file:
        contestants = file.readlines()

    contestant_list = []
    for contestant in contestants:
        contestant = contestant.replace("\n", "")

        contestant_list.append(Contestant(
            contestant.split("-")[0],
            "-out" not in contestant,
            find_placement(contestant),
            "-FIR" in contestant.upper()
            )
        )

    return contestant_list


def score_contestant_max(rank:int, contestant:Contestant) -> int:
    if not contestant.got_a_rose and rank != 11 and contestant.placement == 0:
        return 0

    if rank == 1:
        if contestant.first_impression_rose:
            return 50 + 5
        return 50
    elif rank == 2:
        return 25
    elif rank == 3:
        return 20
    elif rank == 4:
        return 15
    elif rank == 5:
        return 10
    elif 6 <= rank <= 10:
        return 5
    elif rank == 11:  # Next bachelorette
        return 30
    return 0


def score_contestant_min(rank:int, contestant:Contestant) -> int:
    # rank - where an individual put them on their list
    # contestant.placement - where they actually ended up
    fir = 5 if rank == 1 and contestant.first_impression_rose else 0

    if rank == 1 and contestant.placement == 1:
        return 50 + fir
    elif rank <= 2 and 0 < contestant.placement <= 2:
        return 25 + fir
    elif rank <= 3 and 0 < contestant.placement <= 3:
        return 20 + fir
    elif rank <= 4 and 0 < contestant.placement <= 4:
        return 15 + fir
    elif rank <= 5 and 0 < contestant.placement <= 5:
        return 10 + fir
    elif 6 <= rank <= 10 and 0 < contestant.placement <= 10:
        return 5 + fir
    elif rank == 11 and contestant.placement == 11: # Next bachelorette
        return 30

    return 0 + fir


def get_contestant_by_name(name:str, contestants:list[Contestant]):
    for contestant in contestants:
        if contestant.name == name:
            return contestant
    return None


def process_rankings(filename:str, contestants_list:list[Contestant]):
    with open(filename, 'r') as file:
        lines = file.readlines()

    owner_scores = {}
    current_owner = None
    current_list = []
    rank = 0

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        if 'name:' in stripped:
            # This is the owner's name
            if current_owner:
                # Score the previous list
                owner_scores[current_owner] = [
                    sum([score_contestant_max(rank, contestant) for rank, contestant in current_list]),
                    sum([score_contestant_min(rank, contestant) for rank, contestant in current_list])
                ]
                current_list = []
                rank = 0
            # remove "name:"
            current_owner = stripped.split(" ")[1]
        else:
            # This is a contestant rank
            rank += 1
            contestant_name = stripped.split()[-1]
            contestant = get_contestant_by_name(contestant_name, contestants_list)
            if contestant == None: raise Exception(f"Incorrect contestant name in {current_owner}'s ranking")
            current_list.append((rank, contestant))

    # Don't forget to score the last list
    if current_owner:
        owner_scores[current_owner] = [
            sum([score_contestant_max(rank, contestant) for rank, contestant in current_list]),
            sum([score_contestant_min(rank, contestant) for rank, contestant in current_list])
        ]

    return owner_scores


# Assumes 'contestants.txt' and 'rankings.txt' exist and are correctly formatted
def main():
    print("{:<}  {:^27}  {:>}".format("🌹❤", "Bachelor Score Generator", "❤🌹"))
    contestants = read_contestants("contestants.txt")
    scores = process_rankings("rankings.txt", contestants)
    print("{:<12}  {:<12}  {:<12}".format("Name", "Max Score", "Min Score"))
    for owner, scores in scores.items():
        print("{:<12}  {:<12}  {:<12}".format(owner, scores[0], scores[1]))


if __name__ == "__main__":
    main()
