# Plan del equipo — Proyecto 2 (Sistema Multimodal)

Equipo de **4 integrantes**. Dataset: **Free Music Archive (FMA)**, versión `medium`.
Apps: **App1 (identificación de audio, tipo Shazam)** + **App2 (búsqueda por texto)**.
Modalidades: **audio (MFCC)** y **texto (TF-IDF)** como centrales; **imagen (SIFT)** como MVP.

Versión formal y detallada: [`plan_trabajo.pdf`](plan_trabajo.pdf) (fuente `plan_trabajo.tex`).

## División del trabajo

| Integrante | Área | Responsabilidad | Carpeta(s) |
|-----------|------|-----------------|------------|
| **Alejandro Marcelo** | **Núcleo + Apps + Backend + Eval** | Interfaces comunes (`Splitter/Extractor/Codebook/InvertedIndex`), índice invertido genérico, App1 + App2, API FastAPI, banco de pruebas 1K/10K/100K, Docker, scraper de portadas, coordinación. | `src/core`, `src/apps`, `backend/`, `eval/`, `docker-compose.yml` |
| **Integrante 1** | **Texto** | Preproceso (tokenizar, stopwords, stemming), codebook lingüístico (top-k), TF-IDF, construcción del índice por bloques (fusión k-way / SPIMI), comparativa GIN/GiST. | `src/text` |
| **Integrante 2** | **Audio** | Segmentación (~7.5 s), MFCC por ventana, codebook acústico (MiniBatchKMeans), histogramas, comparativa pgvector. Extracción pesada en Colab. | `src/audio` |
| **Integrante 3** | **Imagen + DB** | SIFT, palabras visuales, BoVW sobre portadas; esquema PostgreSQL (tracks, codebook, histogramas), pgvector, índices nativos para las comparativas. | `src/image`, `src/db`, `sql/` |

### Transversal (los 4)

- **Evaluación:** cada uno corre el benchmark de su módulo (cargas 1K/10K/100K);
  Alejandro consolida los gráficos en `eval/`.
- **Informe (README/Wiki):** cada uno redacta la sección de su módulo; Alejandro
  consolida arquitectura y evaluación.
- **GitHub Projects:** cada uno crea y cierra sus propios issues → contribución balanceada.

## Dependencia clave

**Alejandro fija las interfaces de `src/core` primero.** Mientras esas firmas no
cambien, los 4 trabajan en paralelo sin bloquearse. Las apps y la evaluación dependen
de que los tres pipelines estén persistidos (contrato de entrega acordado al inicio).

## Orden por fases (dependencias, no fechas)

0. **Acuerdos de diseño** (todos): chunk por modalidad, esquema DB, protocolo experimental.
1. **Pipelines por modalidad** (paralelo): texto ‖ audio ‖ imagen.
2. **Persistencia + comparativas** Postgres: GIN/GiST + pgvector.
3. **Apps + backend + demo.**
4. **Evaluación 1K/10K/100K + informe.**
5. **Presentación.**

## Estrategia de commits

- **Commits pequeños y diarios** (se evalúa cantidad y constancia).
- Una rama por feature: `feat/audio-mfcc`, `feat/texto-tfidf`, … → PR a `main`.
- Cada tarea = un issue; cerrarlo desde el commit/PR (`closes #N`).
- Mensajes claros en español: `feat(audio): extracción MFCC por segmento`.
