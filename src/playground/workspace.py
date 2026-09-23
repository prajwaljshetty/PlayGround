from pathlib import Path
import uuid
import json

from .filehandling import generate_keys, sign_manifest


class WorkSpace:

    def __init__(self):
        self.root = Path.cwd()
        self.playground = self.root / ".playground"
        self.manifest = self.root / "playground.manifest"

    def generate_workspace_id(self):
        return str(uuid.uuid4())

    def create_workspace(self, workspace_id):
        workspace = self.playground / "workspace" / workspace_id
        workspace.mkdir(parents=True, exist_ok=True)

    def create_manifest(self, workspace_id):
        private_key, _ = generate_keys()

        with self.manifest.open("w") as manifest:
            json.dump(
                {"workspace_id": workspace_id},
                manifest,
                indent=4
            )

        signature = sign_manifest(private_key, self.manifest)

    def is_seeded(self):
        return self.manifest.exists()

    def seed(self):
        workspace_id = self.generate_workspace_id()

        self.create_workspace(workspace_id)
        self.create_manifest(workspace_id)