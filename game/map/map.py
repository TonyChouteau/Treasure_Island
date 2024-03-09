import cv2
import numpy as np
from game.position import Position
from game.map.biome import Biome
from game.map.zone import Zone

HEATMAPS_PATH = "assets/map/heatmap_1400/components"


class Map:
    district_map: np.ndarray = cv2.imread(f"{HEATMAPS_PATH}/district_map.png", cv2.IMREAD_GRAYSCALE)
    biome_map: np.ndarray = cv2.imread(f"{HEATMAPS_PATH}/biome_map.png", cv2.IMREAD_GRAYSCALE)
    zone_map: np.ndarray = cv2.imread(f"{HEATMAPS_PATH}/zone_map.png", cv2.IMREAD_GRAYSCALE)

    treasure: Position

    def __init__(self, folder: str):
        self.folder = folder

    def which_district(self, point: Position) -> int:
        return self.district_map[point.x, point.y]

    def which_biome(self, point: Position) -> Biome:
        return Biome(self.biome_map[point.x, point.y])

    def which_zone(self, point: Position) -> Zone:
        return Zone(self.zone_map[point.x, point.y])
