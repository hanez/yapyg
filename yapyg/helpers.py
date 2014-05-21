# Copyright (c) 2014 Raihan Kibria
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
Helpers for recurring tasks
"""

import entities
import screen
import collisions

def create_screen_wall(state, base_name, thickness=1, top=True, bottom=True, left=True, right=True, color=(1,0,0)):
    """
    TODO
    """
    pass

def create_collision_box(state, base_name, pos, size, thickness=1, top=True, bottom=True, left=True, right=True, color=(1,0,0)):
    """
    TODO
    """
    ENT_TOPWALL = base_name + "_top"
    ENT_LEFTWALL = base_name + "_left"
    ENT_RIGHTWALL = base_name + "_right"
    ENT_BOTTOMWALL = base_name + "_bottom"

    # scr_width = screen.get_width(state)
    # scr_height = screen.get_height(state)
    tile_size = screen.get_tile_size(state)

    horizontal_wall_width_px = size[0] * tile_size
    vertical_wall_height_px = size[1] * tile_size

    if top:
        entities.insert(state,
            ENT_TOPWALL,
            {
                "*": {
                    "textures": [("rectangle",
                        horizontal_wall_width_px,
                        thickness * tile_size,
                        color[0], color[1], color[2],)],
                },
            },
            [pos[0], pos[1] + size[1] - thickness],
            0)
        collisions.add(state, ENT_TOPWALL, ["rectangle", horizontal_wall_width_px / tile_size, thickness], False)

    if bottom:
        entities.insert(state,
            ENT_BOTTOMWALL,
            {
                "*": {
                    "textures": [("rectangle",
                        horizontal_wall_width_px,
                        thickness * tile_size,
                        color[0], color[1], color[2],)],
                },
            },
            [pos[0], pos[1]],
            0)
        collisions.add(state, ENT_BOTTOMWALL, ["rectangle", horizontal_wall_width_px / tile_size, thickness], False)

    if left:
        entities.insert(state,
            ENT_LEFTWALL,
            {
                "*": {
                    "textures": [("rectangle",
                        thickness * tile_size,
                        vertical_wall_height_px,
                        color[0], color[1], color[2],)],
                },
            },
            [pos[0], pos[1]],
            0)
        collisions.add(state, ENT_LEFTWALL, ["rectangle", thickness, vertical_wall_height_px / tile_size], False)

    if right:
        entities.insert(state,
            ENT_RIGHTWALL,
            {
                "*": {
                    "textures": [("rectangle",
                        thickness * tile_size,
                        vertical_wall_height_px,
                        color[0], color[1], color[2],)],
                },
            },
            [pos[0] + size[0] - thickness, pos[1]],
            0)
        collisions.add(state, ENT_RIGHTWALL, ["rectangle", thickness, vertical_wall_height_px / tile_size], False)
