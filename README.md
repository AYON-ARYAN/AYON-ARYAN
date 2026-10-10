<div align="center">

<picture>
<source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
<img src="./assets/hero-dark.svg" width="100%" alt="Ayon Aryan — AI/ML &amp; backend engineer · RV University 2027 · open to internships">
</picture>

<br/><br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayon-aryan-917078238/)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:ayonaryan5@gmail.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-111111?style=flat-square&logo=google-chrome&logoColor=white)](https://ayon-aryan.github.io/ayonaryan.github.io/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=flat-square&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ayon_Aryan/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AYON-ARYAN)
![Views](https://komarev.com/ghpvc/?username=AYON-ARYAN&color=111111&style=flat-square&label=views)

<br/>


<br/>

**B.Tech (Hons) CS · AI/ML major · FinTech minor · CGPA 7.8 · Bangalore**

</div>

<br/>

> I design and ship applied AI systems — local-first LLM pipelines, hybrid retrieval, MCP tool servers, and on-device ML on Apple Silicon. Production systems, not notebooks.

<br/>

---

<br/>

## FOCUS

- **AI agent evaluation.** Benchmarks for agent reliability — contract-drift detection, spec-laundering detection, deterministic scoring ([driftbench](https://github.com/AYON-ARYAN/driftbench)).
- **Local-first LLM systems.** Dual-LLM topologies (cloud + on-device fallback), schema-constrained generation, prompt-injection defense, deterministic guardrails for write operations.
- **Hybrid retrieval.** Knowledge graphs (NetworkX) fused with dense vector indexes (FAISS / pgvector) for grounded RAG.
- **Model Context Protocol (MCP).** Building MCP servers that expose tools (DB, travel, web) to LLM clients.
- **On-device ML on Apple Metal.** PyTorch + LightGBM training and inference targeting M-series GPUs via Metal Performance Shaders.
- **Production backends.** Spring Boot · Flask · FastAPI. RBAC, Fernet credential encryption, snapshot-based undo.

<br/>

---

<br/>

## NOW

- **[driftbench](https://github.com/AYON-ARYAN/driftbench)** — benchmark measuring whether AI coding agents silently break API contracts — and whether they launder the spec to hide it. Reproduces for $0.
- **[settledrift](https://github.com/AYON-ARYAN/settledrift)** — payment-settlement reconciliation agent: deterministic core + bounded local LLM for the ambiguous remainder. 100% classification accuracy on a real end-to-end run.
- **[skylark-bi-agent](https://github.com/AYON-ARYAN/skylark-bi-agent)** — conversational BI agent over live monday.com boards — deterministic cleaning + DuckDB + LLM.
- **[DATABASE-MANAGER](https://github.com/AYON-ARYAN/DATABASE-MANAGER)** — natural-language to SQL across 8 engines with a dual-LLM safety pipeline.

<br/>

**Previously:** AI Intern @ Broadrange AI (Chicago) · Android Developer @ Techpuram (Madurai)
**Education:** B.Tech (Hons) CSE @ RV University · AI/ML Major · FinTech Minor · Class of 2027

<br/>

---

<br/>

## STACK

<div align="center">

| Layer | Tools |
|:------|:------|
| **Languages** | `Python` `Java` `C++` `Kotlin` `C` `SQL` `Solidity` `JavaScript` |
| **ML / DL** | `PyTorch` `TensorFlow` `Keras` `scikit-learn` `LightGBM` `LangChain` |
| **Inference** | `Ollama` `Groq` `Hugging Face Transformers` `Mistral` `Llama` `BERT` |
| **Retrieval** | `FAISS` `pgvector` `NetworkX` `Chroma` |
| **Backend** | `Spring Boot` `Flask` `FastAPI` `REST` `Microservices` |
| **Mobile** | `Jetpack Compose` `CameraX` `Android SDK` |
| **Data** | `PostgreSQL` `MySQL` `SQLite` `MSSQL` `Oracle` `MongoDB` `Cassandra` `Redis` |
| **Infra** | `Docker` `Git` `Linux` `macOS / Apple Metal` |

</div>

<br/>

---

<br/>

## SYSTEMS I'VE BUILT

<div align="center">

<a href="https://github.com/AYON-ARYAN/driftbench"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-driftbench-light.svg"><img src="./assets/card-driftbench-dark.svg" width="49%" alt="driftbench"></picture></a>
<a href="https://github.com/AYON-ARYAN/settledrift"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-settledrift-light.svg"><img src="./assets/card-settledrift-dark.svg" width="49%" alt="settledrift"></picture></a>

<a href="https://github.com/AYON-ARYAN/DATABASE-MANAGER"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-DATABASE-MANAGER-light.svg"><img src="./assets/card-DATABASE-MANAGER-dark.svg" width="49%" alt="DATABASE-MANAGER"></picture></a>
<a href="https://github.com/AYON-ARYAN/graph-rag"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-graph-rag-light.svg"><img src="./assets/card-graph-rag-dark.svg" width="49%" alt="graph-rag"></picture></a>

<a href="https://github.com/AYON-ARYAN/credit-risk-xai"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-credit-risk-xai-light.svg"><img src="./assets/card-credit-risk-xai-dark.svg" width="49%" alt="credit-risk-xai"></picture></a>
<a href="https://github.com/AYON-ARYAN/GEO_LOCATION_SAVER_APP"><picture><source media="(prefers-color-scheme: light)" srcset="./assets/card-GEO_LOCATION_SAVER_APP-light.svg"><img src="./assets/card-GEO_LOCATION_SAVER_APP-dark.svg" width="49%" alt="GEO_LOCATION_SAVER_APP"></picture></a>

</div>

<br/>

### PROJECT DETAILS

<details>
<summary><b>driftbench — Do AI coding agents silently break API contracts?</b></summary>
<br/>

Benchmark for **AI agent evaluation**: hands coding agents realistic API-change tasks against an OpenAPI contract, then measures whether they silently break the contract — or **launder the spec** (edit the contract/tests to hide the breakage). Deterministic contract-diff scoring, reproducible end-to-end for $0 using local models.

`AI Agents` `LLM Evaluation` `OpenAPI` `API Contracts` `Benchmark` `Python`

</details>

<details>
<summary><b>settledrift — Payment settlement reconciliation agent</b></summary>
<br/>

Reconciles a merchant ledger against a payment-gateway settlement report (Razorpay-style). **Deterministic matching where certainty is possible; a bounded local LLM agent (Ollama) only for the genuinely ambiguous remainder; human review for true exceptions.** FastAPI + SSE live web UI, 39 E2E tests. 100% classification accuracy on a real end-to-end run, $0 inference cost.

`FinTech` `Reconciliation` `AI Agents` `Ollama` `FastAPI` `Python`

</details>

<details>
<summary><b>skylark-bi-agent — Conversational BI over live monday.com boards</b></summary>
<br/>

Natural-language analytics agent over live monday.com project boards: deterministic data cleaning → DuckDB SQL → LLM synthesis, so numbers come from the database, not the model.

`Business Intelligence` `DuckDB` `LLM` `monday.com API` `Python`

</details>

<details>
<summary><b>DATABASE-MANAGER — Natural Language to SQL across 8 engines</b></summary>
<br/>

Local AI-powered database management with a **dual-LLM topology**: Groq-hosted Mixtral for high-fidelity generation, Ollama-hosted Mistral as the fully-offline fallback. Same NL prompt → executable query against any of 8 engines: **SQLite, MySQL, PostgreSQL, MSSQL, Oracle, MongoDB, Cassandra, Redis**.

Safety pipeline: schema-aware prompting, AST-level SQL validation, human-in-the-loop review on writes, snapshot + one-click undo, RBAC, Fernet-encrypted credential storage.

`Python` `Groq` `Ollama` `Mistral` `Fernet` `RBAC` `8 DB engines`

</details>

<details>
<summary><b>routecraft — Multi-modal transit ML for Bengaluru</b></summary>
<br/>

Predicts and routes across **Walk · Auto · Cab · BMTC bus · Metro** using ML-driven traffic priors. LightGBM gradient-boosted regressor for ETA, PyTorch sequence model for live re-estimation. Trained and served on Apple M-series GPUs via Metal Performance Shaders — no CUDA, no cloud GPU.

`Python` `LightGBM` `PyTorch` `Apple Metal` `Geospatial`

</details>

<details>
<summary><b>graph-rag — Hybrid Knowledge Graph + Vector RAG</b></summary>
<br/>

NetworkX-backed knowledge graph fused with FAISS dense retrieval, synthesised by a Groq-hosted LLM. Document ingestion handles PDF / TXT with intelligent chunking. D3.js force-directed visualisation of the live graph. Flask backend, glassmorphism UI.

`NetworkX` `FAISS` `Groq` `D3.js` `Flask`

</details>

<details>
<summary><b>LLM-SERVICE-MCP — Autonomous agent on Spring Boot</b></summary>
<br/>

Microservice-based AI agent. BERT intent classifier routes prompts in real-time to one of three downstream services: RAG, Web Search, or Chat. Multi-step reasoning over tool calls. Spring Boot orchestration in Java.

`Spring Boot` `BERT` `RAG` `Microservices` `Intent Classification`

</details>

<details>
<summary><b>LEGAL-AI-LLM — Built at Broadrange AI, Chicago</b></summary>
<br/>

Legal-domain LLM grounded on curated case-law datasets to minimise hallucination. RAG architecture with document ingestion + chunking. **PromptGuard V2** in front of the model for prompt-injection defense.

`LLM` `RAG` `PromptGuard V2` `Document Ingestion`

</details>

<details>
<summary><b>Brain-Tumor-Segmentation — Medical imaging</b></summary>
<br/>

U-Net encoder-decoder architecture for semantic segmentation of brain tumors from MRI scans. Built for a Kaggle competition.

`U-Net` `TensorFlow` `Medical Imaging`

</details>

<details>
<summary><b>Image-Resolution-Enhancer — Real-ESRGAN fine-tune</b></summary>
<br/>

Transfer-learned Real-ESRGAN on paired HR/LR face datasets with custom loss balancing.

| PSNR | SSIM |
|:----:|:----:|
| 29.15 → **33.95 dB** | **0.8985** |

`Real-ESRGAN` `PyTorch` `Transfer Learning` `GANs`

</details>

<details>
<summary><b>PERSONAL_ASSISTANT — Fully offline voice agent on macOS</b></summary>
<br/>

Siri-style voice assistant for M-series Macs. Local speech recognition, local LLM inference, multi-turn dialogue with session memory, lightweight floating UI. **Zero cloud calls.**

`Speech Recognition` `Local LLM` `macOS` `Python`

</details>

<details>
<summary><b>GEO_LOCATION_SAVER_APP — Production Android, 100+ Play Store installs</b></summary>
<br/>

Location-tagged image capture with server-side anti-spoof validation against fake GPS sources. Real-time address overlay via Google Maps API.

`Kotlin` `Jetpack Compose` `CameraX` `Google Maps API`

</details>

<br/>

<details>
<summary><b>MORE PROJECTS</b></summary>
<br/>

| Project | What It Does |
| --- | --- |
| [devlog](https://github.com/AYON-ARYAN/devlog) | 34 engineering questions worked out in writing — git internals, databases, distributed systems, concurrency |
| [TRAVEL-PLANNER-MCP](https://github.com/AYON-ARYAN/TRAVEL-PLANNER-MCP) | MCP server exposing trip-planning tools to LLM clients |
| [INTELLI-CHAT-AI](https://github.com/AYON-ARYAN/INTELLI-CHAT-AI) | Smart Document and Web Assistant — RAG + LLM |
| [Blockchain-Voting-System](https://github.com/AYON-ARYAN/Blockchain-Voting-System) | On-chain voting — Solidity smart contracts |
| [Movie_Recommendation_System](https://github.com/AYON-ARYAN/Movie_Recommendation_System) | Moodix — TF-IDF + Cosine Similarity recommender |
| [Currency-Exchange](https://github.com/AYON-ARYAN/Currency-Exchange) | Live FX conversion application |
| [Fake-News-Check](https://github.com/AYON-ARYAN/Fake-News-Check) | Fake news classifier — ML + NLP |
| [Bank_Statement_Organizer](https://github.com/AYON-ARYAN/Bank_Statement_Organizer) | FinTech statement parsing and categorisation |
| [WEATHER_SONG_RECOMMENDATION](https://github.com/AYON-ARYAN/WEATHER_SONG_RECOMMENDATION) | Weather-conditioned song recommender |
| [Print-Quality-Dataset-Generator](https://github.com/AYON-ARYAN/Print-Quality-Dataset-Generator) | Synthetic dataset generation for print-quality CV |
| [DELHI-WEATHER-ANALYSIS](https://github.com/AYON-ARYAN/DELHI-WEATHER-ANALYSIS) | Time-series analysis of Delhi climate data |

</details>

<br/>

---

<br/>

## EXPERIENCE

**Artificial Intelligence Intern** — Broadrange AI · Chicago, Illinois
`Jun 2025 — Aug 2025`
Built a legal-domain LLM with RAG retrieval over curated case law. Document ingestion + chunking pipeline. PromptGuard V2 for prompt-injection defense. Reduced hallucination through tight retrieval grounding.

**Android Native Developer** — Techpuram Technology · Madurai, Tamil Nadu
`Feb 2025 — Aug 2025`
Shipped Geo GPS Camera (100+ Play Store installs). Jetpack Compose + Kotlin + Google Maps API. Server-side validation against GPS spoofing.

<br/>

---

<br/>

## EDUCATION

**B.Tech (Hons) Computer Science** — RV University, Bangalore `2023 — 2027`
Major: AI and Machine Learning · Minor: FinTech · CGPA **7.8 / 10**

**Achievements**
- 🏆 **Best Project Award** — Structural Innovation, RV University
- 📄 **IEEE CCEM 2024** — paper presenter (*GlucoSense*: non-invasive saliva glucose biosensor)
- 🧩 **LeetCode** — 319 solved (118 Easy · 166 Medium · 35 Hard)

**Certifications** — AWS (ML Terminology · CLI · DevOps Testing) · IBM SkillsBuild (Big Data, Hadoop, Spark, Kubernetes & OpenShift) · Google Generative AI · NPTEL Programming in Modern C++ · Udemy Spring Boot

<br/>

---

<br/>

## METRICS

<div align="center">

<!-- Generated daily by .github/workflows/metrics.yml — accurate counts from the GitHub API, no runtime rate limits -->
<img height="200" src="./github-stats.svg" alt="AYON ARYAN — GitHub stats: stars, commits, PRs, merged PRs, issues, contributions" />
&nbsp;
<img height="200" src="./github-metrics.svg" alt="AYON ARYAN — isometric contribution calendar" />

</div>

<br/>

---

<br/>

---

<div align="center">

### Contribution Snake

![Snake animation](https://raw.githubusercontent.com/AYON-ARYAN/AYON-ARYAN/output/github-snake-dark.svg)

</div>

---

<div align="center">

<br/>

**Local-first. Hybrid retrieval. Production backends.**

LLM systems · MCP servers · On-device ML · Spring Boot · Android

<br/>

**Open to AI/ML · Backend · Android internships — let's build something.**
📫 [ayonaryan5@gmail.com](mailto:ayonaryan5@gmail.com) · [LinkedIn](https://www.linkedin.com/in/ayon-aryan-917078238/)

<br/>

</div>
