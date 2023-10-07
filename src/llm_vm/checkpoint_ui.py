import tkinter as tk
from checkpoint_manager import CheckpointManager

class CheckpointUI:
    def __init__(self, checkpoint_dir):
        self.manager = CheckpointManager(checkpoint_dir)
        self.root = tk.Tk()
        def create_ui(self):
            def save_checkpoint():
                state = tk.simpledialog.askstring("Save Checkpoint", "Enter the state:")
                filename = tk.simpledialog.askstring("Save Checkpoint", "Enter the filename:")
                self.manager.save(state, filename)
            save_button = tk.Button(self.root, text="Save Checkpoint", command=save_checkpoint)
            save_button.pack()
        
            def load_checkpoint():
                filename = tk.simpledialog.askstring("Load Checkpoint", "Enter the filename:")
                state = self.manager.load(filename)
                tk.messagebox.showinfo("Load Checkpoint", f"State: {state}")
            load_button = tk.Button(self.root, text="Load Checkpoint", command=load_checkpoint)
            load_button.pack()
        
            def list_checkpoints():
                checkpoints = self.manager.list_checkpoints()
                tk.messagebox.showinfo("List Checkpoints", '\n'.join(checkpoints))
            list_button = tk.Button(self.root, text="List Checkpoints", command=list_checkpoints)
            list_button.pack()
        
            def delete_checkpoint():
                filename = tk.simpledialog.askstring("Delete Checkpoint", "Enter the filename:")
                self.manager.delete_checkpoint(filename)
            delete_button = tk.Button(self.root, text="Delete Checkpoint", command=delete_checkpoint)
            delete_button.pack()

if __name__ == "__main__":
    ui = CheckpointUI('./checkpoints')
    ui.root.mainloop()
