class VotingSystem:
    def __init__(self, candidates):
        self.candidates = candidates
        self.votes = {candidate: 0 for candidate in candidates}

    def display_candidates(self):
        print("Candidates:")
        for candidate in self.candidates:
            print(f"- {candidate}")

    def vote(self, candidate):
        if candidate in self.candidates:
            self.votes[candidate] += 1
            print(f"Vote for {candidate} recorded.")
        else:
            print(f"Invalid candidate: {candidate}. Please choose a valid candidate.")

    def display_results(self):
        print("Voting Results:")
        for candidate, votes in self.votes.items():
            print(f"{candidate}: {votes} votes")


def main():
    candidates = ["Candidate 1", "Candidate 2", "Candidate 3"]
    voting_system = VotingSystem(candidates)

    while True:
        print("\n=== Mini Voting System ===")
        print("1. Display Candidates")
        print("2. Vote for a Candidate")
        print("3. Display Voting Results")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            voting_system.display_candidates()
        elif choice == "2":
            candidate = input("Enter the candidate you want to vote for: ")
            voting_system.vote(candidate)
        elif choice == "3":
            voting_system.display_results()
        elif choice == "4":
            print("Exiting the voting system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
