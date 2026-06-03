# Núcleo del motor

Las interfaces están en [`interfaces.py`](interfaces.py) y **no se cambian sin avisar
al equipo**. Cada modalidad implementa su `Splitter`, `FeatureExtractor`, `Codebook` y
`CodebookBuilder` (hay stubs en `src/<modalidad>/pipeline.py`). El índice es común y ya
está: [`index.py`](index.py).

## Quién hace qué

- **Alejandro (núcleo):** define las firmas y entrega el índice común (`IndiceEnMemoria`
  ahora; la versión final con construcción por bloques se monta encima con la misma firma).
- **Cada integrante:** implementa el extractor + codebook de su modalidad. Nadie reescribe
  el índice.

## Contrato (lo único que tenés que respetar)

- Un **histograma** es una `list[float]` de tamaño **k** (una posición por codeword).
- Tu `Codebook.histogram(...)` devuelve ese vector.
- Lo metés al índice con `add(doc_id, histograma)` y buscás con `search(histograma, k)`.

## Ejemplo (corre sin dataset, solo stdlib)

```python
from src.core.index import IndiceEnMemoria

idx = IndiceEnMemoria()
idx.add(1, [0, 2, 0, 1])
idx.add(2, [1, 0, 0, 3])
idx.add(3, [0, 2, 0, 2])

for r in idx.search([0, 2, 0, 1], top_k=3):
    print(r.doc_id, round(r.score, 3))
# 1 1.0     (idéntico a la consulta)
# 3 0.949   (parecido)
# 2 0.424
```

Mientras armás tu pipeline, probá con histogramas a mano como estos: no necesitás el
dataset ni Postgres para validar que tu código engancha con el índice.
