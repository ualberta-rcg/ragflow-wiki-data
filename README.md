# University of Alberta - RAGFlow Wiki Data  

![Kubernetes](https://img.shields.io/badge/Kubernetes-1.24+-green?style=flat-square)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

**Maintained by:** Rahim Khoja ([khoja1@ualberta.ca](mailto:khoja1@ualberta.ca))

---

## Description

Kubernetes deployment configuration for **Open WebUI** on the Vulcan RKE2 cluster. Production-hardened with Qdrant vector database, PostgreSQL, Redis, OAuth/OIDC authentication, and Kubeflow inference endpoints.

**Key Features:**
- **Auto-scaling deployment** (2-15 replicas via HPA) with zero-downtime rolling updates and pod anti-affinity
- **Qdrant** vector database for scalable RAG embeddings (Helm-deployed)
- **PostgreSQL 16** for application data
- **Redis** for session management and websocket coordination
- **OAuth/OIDC** authentication via Digital Research Alliance of Canada
- **RAG** with hybrid search, BGE-M3 embeddings, and reranking via Kubeflow inference
- **Apache Tika** for document extraction with HPA (1-4 replicas)
- **NetworkPolicies** restricting backend access to OpenWebUI pods only
- **Traefik IngressRoute** with ServersTransport for WebSocket/streaming support

---

## Architecture

### Services
| Service | Image | Replicas | Purpose |
|---|---|---|---|
| Open WebUI | `ghcr.io/open-webui/open-webui:latest` | 2-15 (HPA) | Main application |
| Qdrant | `qdrant/qdrant` (Helm) | 5 (clustered) | Vector database for RAG |
| PostgreSQL | `postgres:16` | 1 | Application database |
| Redis | `redis:latest` | 1 | Sessions, websockets, cache |
| Apache Tika | `apache/tika:latest-full` | 1-4 (HPA) | Document extraction |

### Infrastructure
- **Namespace:** `openwebui`
- **Storage:** NFS-backed PVCs via `nfs-client` StorageClass
- **Ingress:** Traefik IngressRoute with ServersTransport (300s timeouts, HTTP/2 disabled for WebSocket)
- **TLS:** cert-manager with Let's Encrypt DNS validation



---

## References

* [Digital Research Alliance of Canada](https://alliancecanada.ca/)
* [PAICE (Pan-Canadian AI Compute Environment)](https://alliancecan.ca/en/services/advanced-research-computing/pan-canadian-ai-compute-environment-paice)
* [Research Computing Group](https://www.ualberta.ca/en/information-services-and-technology/research-computing/index.html)

---

## Support

Many Bothans died to bring us this information. This project is provided as-is, but reasonable questions may be answered based on my coffee intake or mood. ;)

Feel free to open an issue or email **[khoja1@ualberta.ca](mailto:khoja1@ualberta.ca)** or **[kali2@ualberta.ca](mailto:kali2@ualberta.ca)** for U of A related deployments.

---

## License

This project is released under the **MIT License** — see [LICENSE](./LICENSE) for details.

---

## About University of Alberta Research Computing

The [Research Computing Group](https://www.ualberta.ca/en/information-services-and-technology/research-computing/index.html) supports high-performance computing, data-intensive research, and advanced infrastructure for researchers at the University of Alberta and across Canada.







































# 

Pipeline for syncing Alliance HPC documentation to RAGFlow and publishing as an MkDocs site.

## Structure

```
docs/                # Source documents (.txt from MediaWiki API)
completions/         # Generated Q&A pairs (page + chunk level)
mkdocs-site/         # MkDocs Material site (docs/ subfolder has .md output)
config/              # processing-state.json, tags.json
scripts/             # Pipeline scripts
```

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables (or use GitHub Actions secrets):
- `RAGFLOW_API_KEY`
- `RAGFLOW_BASE_URL`
- `GOOGLE_API_KEY`

## Usage

Run the full pipeline via GitHub Actions (`full-pipeline.yml`) or locally:

```bash
source venv/bin/activate
python scripts/download-wiki.py
python scripts/sync-ragflow.py
python scripts/convert-to-mkdocs.py
python scripts/fix-mkdocs-links.py
python scripts/generate-homepage.py
python scripts/generate-completions.py
```
