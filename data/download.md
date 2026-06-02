# Descarga del dataset

Usamos *Free Music Archive* (FMA) — repo oficial <https://github.com/mdeff/fma>.
Versión **`medium`** (~25K tracks, ~22 GB) para desarrollo.

> Los enlaces de descarga están en el README de `mdeff/fma`. Los mirrors oficiales
> (servidor de la EPFL) son los de abajo; si cambian, tomar la URL del repo.

## Audio (fma_medium)

```bash
# Audio crudo (mp3). Pesado: se procesa en Google Colab, no en local.
curl -O https://os.unil.cloud.switch.ch/fma/fma_medium.zip
unzip fma_medium.zip -d data/fma
```

## Metadata (fma_metadata)

```bash
curl -O https://os.unil.cloud.switch.ch/fma/fma_metadata.zip
unzip fma_metadata.zip -d data/fma
```

Archivos clave de la metadata: `tracks.csv`, `raw_tracks.csv` (campos `track.comment`,
`track.information`), `raw_artists.csv` (`artist.bio`), `genres.csv` (jerarquía de los
161 géneros — ground truth para recall).

## Portadas (imagen, MVP)

Se scrapean del sitio de FMA — son por álbum (~15K únicas). El scraper vive en `src/apps`
(owner: Alejandro).

## Estructura esperada

```
data/fma/
├── fma_medium/      # <id>.mp3 (audio crudo, NO se versiona)
└── fma_metadata/    # tracks.csv, raw_tracks.csv, raw_artists.csv, genres.csv
```

El audio, las portadas y los CSV **no se versionan** (ya están en `.gitignore`).
