# Sistema Multimodal de Recuperación y Búsqueda

Proyecto 2 — Base de Datos 2 (UTEC, ciclo 2026-1).

Motor unificado que indexa y busca **texto, audio e imagen** bajo un mismo
paradigma: **split → extracción de features → codebook → índice invertido**. Se
compara la implementación propia (índice invertido + codebook) contra las técnicas
nativas de PostgreSQL: **GIN/GiST** para texto y **pgvector** para vectores
(audio e imagen).

Dataset: *Free Music Archive* (FMA), versión `medium` (~25K tracks). Es el único
dataset del enunciado con audio crudo real (mp3), lo que permite extraer MFCC propios.

## Aplicaciones

1. **Identificación de audio (tipo Shazam)** — subir un fragmento de audio y
   recuperar los tracks más parecidos.
2. **Búsqueda por texto** — una consulta en lenguaje natural ("jazz acústico")
   devuelve tracks por género y tags.

## Arquitectura

| Etapa      | Texto                            | Audio                                | Imagen                       |
|------------|----------------------------------|--------------------------------------|------------------------------|
| Split      | documento de metadata por track  | segmentos de ~7.5 s                  | portada de álbum             |
| Extracción | TF-IDF                           | MFCC por ventana                     | SIFT                         |
| Codebook   | top-k lingüístico                | MiniBatchKMeans (palabras acústicas) | K-Means (palabras visuales)  |
| Índice     | índice invertido (construcción k-way) | histograma de palabras acústicas | histograma de visual words |

El audio y el texto son las modalidades centrales; la imagen entra como MVP (las
portadas son por álbum, ~15K únicas, así que la búsqueda visual devuelve álbumes).

## Stack

Python 3.10 · PostgreSQL 16 + pgvector · FastAPI · scikit-learn (MiniBatchKMeans) ·
librosa (MFCC) · OpenCV-contrib (SIFT) · NLTK · Google Colab (procesamiento pesado).

## Cómo correr

```bash
# 1. Base de datos (Postgres + pgvector)
docker compose up -d

# 2. Entorno Python
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Dataset
#    ver data/download.md
```

## Estructura

```
src/core/    interfaces comunes (split, extract, codebook, índice)
src/text/    pipeline de texto (TF-IDF, construcción k-way del índice)
src/audio/   pipeline de audio (MFCC, palabras acústicas)
src/image/   pipeline de imagen (SIFT, bag-of-visual-words)
src/db/      persistencia PostgreSQL + comparativas (GIN/GiST, pgvector)
src/apps/    App1 (identificación de audio) y App2 (búsqueda por texto)
backend/     API FastAPI
frontend/    UI mínima
eval/        benchmarks (1K/10K/100K) y gráficos
```

El plan formal del equipo está en [`docs/plan_trabajo.pdf`](docs/plan_trabajo.pdf)
(fuente en `docs/plan_trabajo.tex`); el resumen de la división, en
[`docs/PLAN.md`](docs/PLAN.md).
