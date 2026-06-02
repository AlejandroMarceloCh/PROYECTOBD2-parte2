"""Persistencia y comparativas PostgreSQL — owner: Integrante 3.

- Esquema y carga (tracks, codebook, histogramas).
- Comparativa de texto: GIN/GiST + full-text search.
- Comparativa de audio e imagen: pgvector con índice HNSW o IVF.
- Deja los índices nativos listos; cada dueño de modalidad corre su propio benchmark.
"""
