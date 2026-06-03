"""Índice invertido de referencia, en memoria.

Implementación mínima y funcional de InvertedIndex para que cada modalidad pruebe
su pipeline HOY, sin esperar SPIMI ni Postgres. La versión final (construcción por
bloques en disco, persistencia) se monta encima manteniendo la misma firma.
"""
from __future__ import annotations

import math
from collections import defaultdict
from typing import Sequence

from .interfaces import InvertedIndex, Resultado


class IndiceEnMemoria(InvertedIndex):
    """Índice invertido simple: codeword -> [(doc_id, peso)], búsqueda por coseno.

    El histograma es un vector de floats de tamaño k (una posición por codeword).
    """

    def __init__(self) -> None:
        self._postings: dict[int, list[tuple[int, float]]] = defaultdict(list)
        self._normas: dict[int, float] = {}

    def add(self, doc_id: int, histograma: Sequence[float]) -> None:
        # Cada posición del histograma es un codeword; guardamos solo los != 0.
        for codeword, peso in enumerate(histograma):
            if peso:
                self._postings[codeword].append((doc_id, peso))
        self._normas[doc_id] = math.sqrt(sum(p * p for p in histograma))

    def search(self, consulta: Sequence[float], top_k: int = 10) -> list[Resultado]:
        # Producto punto recorriendo solo los codewords presentes en la consulta.
        scores: dict[int, float] = defaultdict(float)
        for codeword, peso_q in enumerate(consulta):
            if not peso_q:
                continue
            for doc_id, peso_d in self._postings.get(codeword, ()):
                scores[doc_id] += peso_q * peso_d

        norma_q = math.sqrt(sum(p * p for p in consulta)) or 1.0
        resultados = [
            Resultado(doc_id, score / (norma_q * (self._normas[doc_id] or 1.0)))
            for doc_id, score in scores.items()
        ]
        resultados.sort(key=lambda r: r.score, reverse=True)
        return resultados[:top_k]
