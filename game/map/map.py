import cv2
from game.position import Position
from biome import Biome
from zone import Zone

HEATMAPS_PATH = "assets/map/heatmap_1400/components"

class Map:
    district_map = cv2.imread(f"{HEATMAPS_PATH}/district_map.png", cv2.IMREAD_GRAYSCALE)
    biome_map = cv2.imread(f"{HEATMAPS_PATH}/biome_map.png", cv2.IMREAD_GRAYSCALE)
    zone_map = cv2.imread(f"{HEATMAPS_PATH}/zone_map.png", cv2.IMREAD_GRAYSCALE)

    def __init__(self, folder: str):
        self.folder = folder

    def which_district(self, pos: Position):
        return self.district_map[pos.x, pos.y]

    def which_biome(self, pos: Position):
        return Biome(self.biome_map[pos.x, pos.y])

    def which_zone(self, pos: Position):
        return Zone(self.zone_map[pos.x, pos.y])
