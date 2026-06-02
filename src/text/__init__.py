"""Pipeline de TEXTO — owner: Integrante 1.

Implementa las interfaces de `src.core.interfaces` para la modalidad texto:
- Splitter: un documento de metadata por track (título, artista, género, tags, bio).
- FeatureExtractor con TF-IDF.
- CodebookBuilder lingüístico (tokenizar, normalizar, stopwords, stemming, top-k).
- InvertedIndex con construcción por bloques en disco (fusión k-way / SPIMI).
"""
