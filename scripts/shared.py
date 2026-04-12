"""Shared constants and utilities across pipeline scripts."""

import re
from pathlib import Path

# Prefixes to always skip (non-wiki content)
SKIP_DOC_PREFIXES = ("events/", "status/")

# Slug patterns to skip during sync/convert (low-value auto-generated lists)
# These are huge tables that waste tokens and don't provide conceptual docs
SKIP_SLUG_PATTERNS = [
    r"^modules_avx",      # modules_avx, modules_avx2, modules_avx512
    r"^modules_sse",      # modules_sse3
    r"^modules_specific", # modules_specific_to_niagara
    r"^wheels",           # wheels3_6 through wheels3_14
    r"^sidebar-",         # sidebar navigation fragments
]
_SKIP_SLUG_RE = [re.compile(p, re.IGNORECASE) for p in SKIP_SLUG_PATTERNS]


def should_skip_doc(doc_key: str, doc_state: dict = None) -> bool:
    """Check if a document should be skipped for sync/convert.
    
    Skips:
    - events/ and status/ prefixes
    - Auto-generated module/wheel list pages
    - Empty files (0 bytes)
    """
    if doc_key.startswith(SKIP_DOC_PREFIXES):
        return True
    
    slug = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    for pattern in _SKIP_SLUG_RE:
        if pattern.match(slug):
            return True
    
    # Skip empty files
    if doc_state:
        path = doc_state.get("path", "")
        if path:
            # Handle both absolute and relative paths
            p = Path(path)
            if not p.is_absolute():
                p = Path(__file__).parent.parent / path
            if p.exists() and p.stat().st_size == 0:
                return True
    
    return False

# Wiki category -> directory name
# Only covers the 14 categories that the MediaWiki actually assigns.
CATEGORY_MAP = {
    # Getting started
    "connecting": "getting-started",
    "se connecter": "getting-started",

    # Running jobs
    "slurm": "running-jobs",

    # Software (parent)
    "software": "software",

    # Software sub-categories
    "computationalchemistry": "software/chemistry",
    "biomolecularsimulation": "software/molecular-sim",
    "ai and machine learning": "software/ai-ml",
    "bioinformatics": "software/bioinformatics",
    "cvmfs": "software/cvmfs",
    "user installed software": "software/user-installed",

    # Cloud
    "cloud": "cloud",
    "cc-cloud": "cloud",

    # Cross-cuts
    "tutorials": "tutorials",
    "policy": "policies",
}

# Title keywords -> directory
# Catches the 635+ docs that have no wiki category.
# Order matters: first match wins.  More specific patterns come first.
_TITLE_RULES = [
    # Clusters / systems
    (r"^(cedar|graham|narval|béluga|beluga|niagara|arbutus|trillium|monarq|hélios|helios"
     r"|vulcan|siku|killarney|nibi|rorqual|tamia|hpc4health|mp2)$", "clusters"),
    (r"(national_systems|systems_overview|infrastructure_renewal|migration|transition_from)", "clusters"),

    # Storage & data
    (r"(storage|file_management|filesystem|scratch|nearline|lustre|quota|globus|rsync"
     r"|transferring_files|archiving|tar$|dar$|data_backup|data_management|data_protection"
     r"|handling_large_collections|sharing_data|diskusage|parallel_i_o|mpi-io"
     r"|using_a_new_empty_volume|using_swift|project_layout|readme_files)", "storage-and-data"),

    # Running jobs
    (r"(running_jobs|job_submission|advanced_job|best_practices_for_job|monitoring_jobs"
     r"|managing_slurm|what_is_a_scheduler|scheduling_policy|meta-farm|glost|gnu_parallel"
     r"|scalability|prolonging_terminal|points_de_contrôle|checkpoint"
     r"|estimer_et_prévenir|resource_allocation|paice_allocation"
     r"|using_a_resource_allocation)", "running-jobs"),

    # Getting started / accounts / access
    (r"(getting_started|apply_for_a_ccdb|account_renewal|multifactor_authentication"
     r"|ssh_tunnelling|ssh_security|ssh_host_keys|securing_your_account|linux_introduction"
     r"|frequently_asked_questions|cybersecurity|configuring_wsl|automation_in_the_context"
     r"|changing_username|user_roles|windows_subsystem|acknowledging"
     r"|migrating_between_clusters|ha_fip)", "getting-started"),

    # Cloud
    (r"(security_corrections_for_virtual_machines|building_a_web_portal"
     r"|nextcloud|using_a_new_empty_volume_on_a)", "cloud"),

    # AI / ML
    (r"(huggingface|large_language_model|llm|deepspeed|vllm|mlflow|rapids|faiss"
     r"|imagenet|voxceleb|ml_performance|interpretable_ai|tensorboard"
     r"|tutoriel_apprentissage_machine|mxnet|optuna)", "software/ai-ml"),

    # Quantum computing
    (r"(qiskit|pennylane|snowflurry|cirq|classiq|quantumatk"
     r"|informatique_quantique|transpileur_quantique)", "software/quantum"),

    # Containers
    (r"(apptainer|singularity|biorepo_containers|using_conda_in_apptainer)", "software/containers"),

    # Interactive / visualization
    (r"(jupyterhub|jupyterlab|jupyternotebook|open_ondemand|vnc"
     r"|testing_with_graphics|visual_studio_code)", "interactive"),

    # Programming & dev tools
    (r"^(c|fortran|rust|python|r$)", "programming"),
    (r"(openmp|openacc|pthreads|cuda|nccl|multi-instance_gpu|nvprof|nvtop"
     r"|debugging_and_profiling|gdb|pgdbg|gprof|make$|cmake|autotools|easybuild"
     r"|build_tools|gcc_c|mpi4py|version_control|programming_guide"
     r"|blas_and_lapack|modules$|modules_avx|modules_sse|modules_specific"
     r"|standard_software_environments|recent_changes_to_the_software"
     r"|available_software|available_python_wheels|wheels[23])", "programming"),

    # Support
    (r"(technical_support|system_status|frequently_asked_questions_about_the_ccdb"
     r"|self-paced_courses|formation$|écolecq)", "support"),

    # Policies / RAC
    (r"(rac_|rapid_access_service|rpp_annual|scratch_purging_policy"
     r"|acknowledging_the_alliance)", "policies"),

    # Bioinformatics software not caught by wiki category
    (r"^(bioinformatics|fasttree|mafft|metaphlan|parasail|mrbayes|cellranger"
     r"|galaxy|gbrowse|freesurfer|parabricks)$", "software/bioinformatics"),

    # Chemistry / physics software not caught by wiki category
    (r"^(dalton|openmolcas|rdkit|subatomicphysics)$", "software/chemistry"),

    # Scientific / domain software (general software bucket)
    (r"^(dask|dedalus|dl_poly|firedrake|moose|opencv|pykeops|wrf|sas|stata"
     r"|sqlite|aiida|fir|me_modelling|gis|mist|cesm|computational_fluid_dynamics"
     r"|mii|metrix|uv)$", "software"),

    # Cluster-specific pages
    (r"(monarq_en-ca|trillium_quickstart)", "clusters"),

    # Getting started extras
    (r"(installing_software_in_your_home_directory|access_to_files|advanced_jupyter"
     r"|humanities_and_social_sciences|astronomy_and)", "getting-started"),

    # Archived / past events
    (r"(événements_passés|covid19)", "support"),

    # NUMA, HPC internals
    (r"(non-uniform_memory_access|numa)", "programming"),
]

# Pre-compile patterns
_TITLE_RULES_COMPILED = [(re.compile(pat, re.IGNORECASE), dest) for pat, dest in _TITLE_RULES]


def category_to_dir(cat):
    """Map a wiki category name to a directory name."""
    return CATEGORY_MAP.get(cat.lower(), "general")


def categorize_doc(doc_key, wiki_categories):
    """Determine directory for a doc using wiki categories, then title fallback.

    Returns the directory string (e.g. "software/ai-ml", "running-jobs", "general").
    """
    if wiki_categories:
        return category_to_dir(wiki_categories[0])

    title = doc_key.split("/")[-1] if "/" in doc_key else doc_key
    for pattern, dest in _TITLE_RULES_COMPILED:
        if pattern.search(title):
            return dest

    return "general"
