from pathlib import Path
import uuid
import json

from .filehandling import generate_keys, sign_manifest , encode_bytes , write_file


class WorkSpace:

    def __init__(self):
        self.root = Path.cwd()
        # Directory
        self.playground = self.root / ".playground"
        self.meta = self.root / ".playground-meta"

        # Files
        self.manifest = self.meta / "manifest.playground"
        self.proof = self.meta / "proof.playground"

    def generate_workspace_id(self):
        return str(uuid.uuid4())

    def create_workspace(self, workspace_id):
        workspace = self.playground / "workspace" / workspace_id
        workspace.mkdir(parents=True, exist_ok=True)

    def create_manifest(self, workspace_id):
        self.meta.mkdir(parents=True, exist_ok=True)

        private_key, public_key = generate_keys()

        with self.manifest.open("w") as manifest:
            json.dump(
                {"workspace_id": workspace_id},
                manifest,
                indent=4
            )

        signature = sign_manifest(private_key, self.manifest)

        proof = {
            "public_key": encode_bytes(public_key.public_bytes_raw()),
            "signature": encode_bytes(signature)
        }

        write_file( self.proof , json.dumps(proof, indent=4) )
        write_file( self.playground / "private.key" , encode_bytes(private_key.private_bytes_raw()))

    def is_seeded(self):
        return self.manifest.exists()

    def seed(self):
        workspace_id = self.generate_workspace_id()

        self.create_workspace(workspace_id)
        self.create_manifest(workspace_id)