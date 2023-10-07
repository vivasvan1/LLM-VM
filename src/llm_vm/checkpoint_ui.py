import tkinter as tk
from checkpoint_manager import CheckpointManager

class CheckpointUI:
    def __init__(self, checkpoint_dir):
        self.manager = CheckpointManager(checkpoint_dir)
        self.root = tk.Tk()
        self.create_ui()

    def create_ui(self):
        def save_checkpoint(self):
            state = tk.simpledialog.askstring("Save Checkpoint", "Enter the state:")
            filename = tk.simpledialog.askstring("Save Checkpoint", "Enter the filename:")
            self.manager.save(state, filename)
    
        def load_checkpoint(self):
            filename = tk.simpledialog.askstring("Load Checkpoint", "Enter the filename:")
            state = self.manager.load(filename)
            tk.messagebox.showinfo("Load Checkpoint", f"State: {state}")
    
        def list_checkpoints(self):
            checkpoints = self.manager.list_checkpoints()
            tk.messagebox.showinfo("List Checkpoints", '\n'.join(checkpoints))
    
        def delete_checkpoint(self):
            filename = tk.simpledialog.askstring("Delete Checkpoint", "Enter the filename:")
            self.manager.delete_checkpoint(filename)

if __name__ == "__main__":
    ui = CheckpointUI('./checkpoints')
    ui.root.mainloop()
