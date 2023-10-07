import argparse
import json
from checkpoint_manager import CheckpointManager

def main():
    parser = argparse.ArgumentParser(description='Manage training checkpoints.')
    subparsers = parser.add_subparsers(dest='command')

    save_parser = subparsers.add_parser('save', help='Save a checkpoint.')
    save_parser.add_argument('state', type=json.loads, help='The state to be saved (as a JSON string).')
    save_parser.add_argument('filename', help='The filename for the checkpoint.')

    load_parser = subparsers.add_parser('load', help='Load a checkpoint.')
    load_parser.add_argument('filename', help='The filename of the checkpoint.')

    delete_parser = subparsers.add_parser('delete', help='Delete a checkpoint.')
    delete_parser.add_argument('filename', help='The filename of the checkpoint.')

    list_parser = subparsers.add_parser('list', help='List all checkpoints.')

    args = parser.parse_args()

    checkpoint_dir = './checkpoints'
    manager = CheckpointManager(checkpoint_dir)

    if args.command == 'save':
        manager.save(args.state, args.filename)
    elif args.command == 'load':
        print(manager.load(args.filename))
    elif args.command == 'delete':
        manager.delete_checkpoint(args.filename)
    elif args.command == 'list':
        print('\n'.join(manager.list_checkpoints()))

if __name__ == '__main__':
    main()
