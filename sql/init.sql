-- Inicialización de la base multimodal.
-- Se ejecuta una sola vez al crear el contenedor (docker-entrypoint-initdb.d).

CREATE EXTENSION IF NOT EXISTS vector;    -- pgvector (comparativa de audio e imagen)
CREATE EXTENSION IF NOT EXISTS pg_trgm;   -- soporte GIN/GiST sobre texto

-- Esquema base. Cada área lo afina según necesite (ver docs/PLAN.md).

-- Metadatos de track (provienen de la metadata de FMA: tracks.csv, raw_tracks.csv,
-- raw_artists.csv). Sostiene la modalidad texto y el ground truth de géneros.
CREATE TABLE IF NOT EXISTS tracks (
    id          INTEGER PRIMARY KEY,
    titulo      TEXT,
    artista     TEXT,
    album       TEXT,
    genero_top  TEXT,          -- género de primer nivel (16 raíces) -> ground truth
    generos     TEXT,          -- subgéneros / jerarquía
    tags        TEXT,
    bio         TEXT,          -- biografía del artista (enriquece el corpus textual)
    descripcion TEXT
);

-- Codebook compartido. modalidad = 'texto' | 'audio' | 'imagen'.
CREATE TABLE IF NOT EXISTS codebook (
    id          SERIAL PRIMARY KEY,
    modalidad   TEXT    NOT NULL,
    codeword_id INTEGER NOT NULL,
    centroide   REAL[]            -- centroide del clustering (audio/imagen); NULL para texto
);

-- Histograma de codewords por chunk (representación compacta).
-- En la rama pgvector el histograma de audio/imagen se migra a tipo vector(k).
CREATE TABLE IF NOT EXISTS histogramas (
    chunk_id   TEXT,            -- p.ej. '<track_id>:<segmento>' (audio) o '<track_id>' (texto)
    track_id   INTEGER REFERENCES tracks(id),
    modalidad  TEXT NOT NULL,
    histograma REAL[]
);
