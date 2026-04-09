"""Shared constants and utilities across pipeline scripts."""

# Category mapping - wiki category -> directory name
# Used by download-wiki.py for source file paths and convert-to-mkdocs.py for output paths
CATEGORY_MAP = {
    "software": "software",
    "computationalchemistry": "software/chemistry",
    "biomolecularsimulation": "software/molecular-sim",
    "ai and machine learning": "software/ai-ml",
    "bioinformatics": "software/bioinformatics",
    "cloud": "cloud",
    "cc-cloud": "cloud",
    "slurm": "scheduling",
    "connecting": "getting-started",
    "se connecter": "getting-started",
    "cvmfs": "software/cvmfs",
    "tutorials": "tutorials",
    "policy": "policies",
    "user installed software": "software/user-installed",
}


def category_to_dir(cat):
    """Map a wiki category name to a directory name."""
    return CATEGORY_MAP.get(cat.lower(), "general")
