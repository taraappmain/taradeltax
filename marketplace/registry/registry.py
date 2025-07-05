# File: marketplace/registry.py
import os
import json

class SkillRegistry:
    """
    Discovers and loads skill metadata from subdirectories.
    Each subdirectory under 'marketplace/' that contains a 'skill.json' 
file
    will be registered as a skill.
    """
    def __init__(self, base_dir=None):
        # Determine registry base directory
        if base_dir is None:
            base_dir = os.path.dirname(__file__)
        self.base_dir = base_dir
        self.skills = {}
        self._discover_skills()

    def _discover_skills(self):
        # Scan each subfolder for skill.json
        for name in os.listdir(self.base_dir):
            folder = os.path.join(self.base_dir, name)
            if os.path.isdir(folder):
                meta_path = os.path.join(folder, 'skill.json')
                if os.path.isfile(meta_path):
                    try:
                        with open(meta_path, 'r', encoding='utf-8') as f:
                            spec = json.load(f)
                        # Validate minimal fields
                        if 'name' in spec and 'ui' in spec:
                            self.skills[spec['name']] = spec
                    except Exception as e:
                        print(f"Warning: Failed to load skill metadata 
from {meta_path}: {e}")

    def list_skills(self):
        """Return list of skill metadata dictionaries."""
        return list(self.skills.values())

    def get_skill(self, name):
        """Return metadata for skill with given name."""
        return self.skills.get(name)

# Example usage:
# registry = SkillRegistry()
# skills = registry.list_skills()
# for skill in skills:
#     print(skill['name'], skill.get('description'))

