"""Pipeline de IMAGEN — owner: Integrante 3.

Implementa las interfaces de `src.core.interfaces` para la modalidad imagen
(portadas de álbum de FMA, modalidad MVP):
- FeatureExtractor con SIFT (cv2.SIFT_create): keypoints + descriptores 128-D.
- CodebookBuilder con K-Means / MiniBatchKMeans sobre los descriptores (visual words).
- Histograma de palabras visuales por portada (bag-of-visual-words).
"""
