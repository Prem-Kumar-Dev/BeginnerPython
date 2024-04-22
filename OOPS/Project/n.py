import tkinter as tk
from tkinter import messagebox

class Candidate:
    def _init_(self, name):
        self.name = name
        self.votes = 0

    def get_name(self):
        return self.name

    def get_votes(self):
        return self.votes

    def add_vote(self):
        self.votes += 1


class VotingSystem:
    def _init_(self):
        self.candidates = {}

    def add_candidate(self, candidate):
        self.candidates[candidate.get_name()] = candidate

    def vote_for_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name].add_vote()
            messagebox.showinfo("Success", f"Vote for {candidate_name} recorded successfully!")
        else:
            messagebox.showerror("Error", f"Candidate {candidate_name} not found.")

    def display_results(self):
        result = "Voting Results:\n"
        for candidate_name, candidate in self.candidates.items():
            result += f"{candidate_name}: {candidate.get_votes()} votes\n"
        messagebox.showinfo("Results", result)


def vote_candidate():
    candidate_name = candidate_entry.get()
    voting_system.vote_for_candidate(candidate_name)


def display_results():
    voting_system.display_results()


# Example usage:
voting_system = VotingSystem()

# Adding candidates
candidate1 = Candidate("Candidate 1")
candidate2 = Candidate("Candidate 2")
voting_system.add_candidate(candidate1)
voting_system.add_candidate(candidate2)

# GUI
root = tk.Tk()
root.title("Online Voting System")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter candidate name:")
label.grid(row=0, column=0)

candidate_entry = tk.Entry(frame)
candidate_entry.grid(row=0, column=1)

vote_button = tk.Button(frame, text="Vote", command=vote_candidate)
vote_button.grid(row=1, column=0, columnspan=2, pady=5)

results_button = tk.Button(frame, text="Display Results", command=display_results)
results_button.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()