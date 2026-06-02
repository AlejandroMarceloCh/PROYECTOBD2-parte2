"""Pipeline de AUDIO — owner: Integrante 2.

Implementa las interfaces de `src.core.interfaces` para la modalidad audio:
- Splitter de tracks en segmentos de ~7.5 s.
- FeatureExtractor con MFCC por ventana.
- CodebookBuilder acústico (MiniBatchKMeans sobre los MFCC).
- Cuantización de cada segmento a histograma de palabras acústicas.
"""
