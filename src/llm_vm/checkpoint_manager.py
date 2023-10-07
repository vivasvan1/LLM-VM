import os
import json

class CheckpointManager:
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = checkpoint_dir

    def save(self, state, filename):
        with open(os.path.join(self.checkpoint_dir, filename), 'w') as f:
            json.dump(state, f)

    def load(self, filename):
        with open(os.path.join(self.checkpoint_dir, filename), 'r') as f:
            state = json.load(f)
        return state

    def list_checkpoints(self):
        return os.listdir(self.checkpoint_dir)

    def delete_checkpoint(self, filename):
        os.remove(os.path.join(self.checkpoint_dir, filename))
